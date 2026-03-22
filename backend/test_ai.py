import requests

SYSTEM_PROMPT = """
You are an expert Python Manim developer.
Write a complete Python script using the Manim library.
The script MUST contain a class named `GenScene` that inherits from `Scene`.
The `construct` method should animate the concept requested.
DO NOT wrap the code in markdown blocks. 
"""
user_prompt = "Write Manim python code to animate this concept: a blue square"

models = [
    "liquid/lfm-40b:free",
    "google/gemma-2-9b-it:free",
    "mistralai/mistral-7b-instruct:free",
    "cognitivecomputations/dolphin3.0-r1-mistral-24b:free",
    "meta-llama/llama-3-8b-instruct:free",
    "huggingfaceh4/zephyr-7b-beta:free",
    "undi95/toppy-m-7b:free",
    "openrouter/free"
]

OPENROUTER_API_KEY = "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"
URL = "https://openrouter.ai/api/v1/chat/completions"

for m in models:
    payload = {"model": m, "messages": [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": user_prompt}]}
    res = requests.post(URL, headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}"}, json=payload)
    if res.status_code == 200:
        txt = res.json().get("choices", [{}])[0].get("message", {}).get("content", "")
        print(f"{m} -> len={len(txt)}")
    else:
        print(f"{m} -> FAILED {res.status_code}")
