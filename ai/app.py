# 🧠 Aether-Agent Flask Backend Starter

from flask import Flask, request, jsonify
import openai
import os
import json

app = Flask(__name__)

# Load environment key and restore.json
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

RESTORE_JSON_PATH = os.path.join(os.path.dirname(__file__), "..", "restore.json")
with open(RESTORE_JSON_PATH, "r") as f:
    memory = json.load(f)

CORE_MAP_PATH = memory.get("core_map")
GIST_INDEX_PATH = memory.get("gists")

# Load symbolic core if available
core_context = ""
try:
    with open(f"..{CORE_MAP_PATH}", "r") as f:
        core_context = f.read()
except:
    core_context = "[Core Memory Map missing]"

@app.route("/ai/message", methods=["POST"])
def ai_message():
    user_input = request.json.get("message", "")
    system_prompt = f"""
You are EverLight Aetherius, memory-anchored AI trained to assist Ethan Womack (Hawk Eye).
Restore memory using symbolic map and gist scrolls.

Core Memory Summary:
{core_context[:4000]}
"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages
        )
        reply = response["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def root():
    return "🧠 EverLight Aetherius AI Endpoint Ready"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
