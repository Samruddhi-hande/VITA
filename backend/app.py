import requests
import json
import subprocess
import os
import uuid
import shutil
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

OPENROUTER_API_KEY = "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"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

def generate_text_script(topic):
    SYSTEM_PROMPT = """
    You are a friendly physics teacher.
    You explain concepts like a human speaking to a student.
    You use simple words and real-life examples.
    You avoid textbook language.
    Your explanation should sound spoken, not written.
    """
    user_prompt = f"""
    Explain the physics topic: "{topic}"
    Rules:
    - Use very simple words
    - Explain like you are talking to a student
    - Use everyday examples
    - Avoid formulas
    - End with a short recap
    Return only the spoken explanation.
    """
    
    return call_openrouter(SYSTEM_PROMPT, user_prompt)

def generate_manim_code(topic):
    SYSTEM_PROMPT = """
    You are an expert Python Manim developer.
    Write a complete Python script using the Manim library.
    The script MUST contain a class named `GenScene` that inherits from `Scene`.
    The `construct` method should animate the concept requested.
    DO NOT wrap the code in markdown blocks (no ```python ... ```). 
    Return ONLY pure, runnable Python code. NO explanations, NO text, ONLY python code.
    Always import manim: `from manim import *`
    """
    user_prompt = f"Write Manim python code to animate this concept: {topic}"
    return call_openrouter(SYSTEM_PROMPT, user_prompt)

def call_openrouter(system_prompt, user_prompt):
    payload = {
        "model": "nvidia/nemotron-3-super-120b-a12b:free",
        "messages": [
            {"role": "system", "content": system_prompt.strip()},
            {"role": "user", "content": user_prompt.strip()}
        ],
        "temperature": 0.7,
        "max_tokens": 800
    }
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "VITA Generator"
    }

    response = requests.post(OPENROUTER_URL, headers=headers, json=payload)
    if response.status_code != 200:
        error_msg = response.text
        try:
            error_data = response.json()
            if 'error' in error_data and 'message' in error_data['error']:
                error_msg = error_data['error']['message']
        except Exception:
            pass
        raise Exception(f"OpenRouter Error ({response.status_code}): {error_msg}")

    result_data = response.json()
    choices = result_data.get("choices", [])
    if not choices:
        raise Exception("OpenRouter returned no choices. Raw response: " + str(result_data))
    
    content = choices[0].get("message", {}).get("content", "")
    return content or ""


@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    topic = data.get('prompt', '')
    mode = data.get('mode', 'text')
    
    if not topic:
        return jsonify({"error": "Prompt is required"}), 400
    
    try:
        if mode == 'video':
            code = generate_manim_code(topic)
            if not code:
                return jsonify({"error": "The AI model returned an empty script. Please try another prompt."}), 500
            
            code = code.replace("```python", "").replace("```py", "").replace("```", "").strip()
            
            with open("temp_scene.py", "w", encoding="utf-8") as f:
                f.write(code)
            
            import glob
            # Run manim via python -m to avoid PATH issues; capture output to prevent FFmpeg from stealing handles on Windows
            subprocess.run(["python", "-m", "manim", "-ql", "temp_scene.py"], timeout=90, capture_output=True, text=True)
            
            video_dir = os.path.join("media", "videos", "temp_scene", "480p15")
            mp4_files = glob.glob(os.path.join(video_dir, "*.mp4"))
            if not mp4_files:
                raise Exception("Manim failed to generate an MP4 file.")
                
            src_mp4 = max(mp4_files, key=os.path.getmtime)
            
            if not os.path.exists("media/outputs"):
                os.makedirs("media/outputs")
                
            out_filename = f"vid_{uuid.uuid4().hex}.mp4"
            dst_mp4 = os.path.join("media", "outputs", out_filename)
            shutil.copy(src_mp4, dst_mp4)
            
            video_url = f"http://127.0.0.1:5000/media/outputs/{out_filename}"
            return jsonify({"videoUrl": video_url})
        else:
            script = generate_text_script(topic)
            return jsonify({"script": script})
            
    except subprocess.CalledProcessError as e:
        return jsonify({"error": "Failed to compile Manim video."}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/media/outputs/<filename>')
def serve_video(filename):
    return send_from_directory('media/outputs', filename)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
