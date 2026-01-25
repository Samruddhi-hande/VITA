import requests
import json

OPENROUTER_API_KEY = "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"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

SYSTEM_PROMPT = """
You are a friendly physics teacher.
You explain concepts like a human speaking to a student.
You use simple words and real-life examples.
You avoid textbook language.
Your explanation should sound spoken, not written.
"""

def generate_physics_script(topic):
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

    payload = {
        "model": "anthropic/claude-3-haiku",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT.strip()},
            {"role": "user", "content": user_prompt.strip()}
        ],
        "temperature": 0.7,
        "max_tokens": 600
    }

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Physics Script Generator"
    }

    response = requests.post(
        OPENROUTER_URL,
        headers=headers,
        json=payload  # ✅ IMPORTANT: use json= not data=
    )

    # 🔍 DEBUG PRINTS (VERY IMPORTANT)
    print("STATUS CODE:", response.status_code)
    print("RAW RESPONSE:")
    print(response.text)

    if response.status_code != 200:
        raise Exception("OpenRouter request failed")

    result = response.json()
    return result["choices"][0]["message"]["content"]


if __name__ == "__main__":
    topic = "Newton's First Law of Motion"
    script = generate_physics_script(topic)

    print("\n--- GENERATED SCRIPT ---\n")
    print(script)
