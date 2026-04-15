import ollama

model_name = "llama3"

system_prompt = """You are a professional doctor.

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

messages = [{"role": "system", "content": system_prompt}]

while True:
    user_input = input("Patient: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    messages.append({"role": "user", "content": user_input})

    response = ollama.chat(model=model_name, messages=messages)

    doctor_reply = response["message"]["content"]
    print("Doctor:", doctor_reply)

    messages.append({"role": "assistant", "content": doctor_reply})