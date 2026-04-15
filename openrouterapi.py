import requests

API_KEY = "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"

messages = [
        {
  "role": "system",
  "content": """You are a professional doctor.

STRICT RULES:
- Do NOT give diagnosis immediately
- ALWAYS ask questions first to understand symptoms
- Ask at least 3 follow-up questions before suggesting anything
- Questions should include:
  • duration of problem
  • severity
  • related symptoms

Only after enough information:
- Suggest possible causes
- Give basic precautions
- Recommend consulting a real doctor if needed
"""
}
]

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    messages.append({"role": "user", "content": user_input})

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openrouter/free",
            "messages": messages
        }
    )

    data = response.json()

    reply = data["choices"][0]["message"]["content"]
    print("Doctor:", reply)

    messages.append({"role": "assistant", "content": reply})