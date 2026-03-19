from groq import Groq
import os
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("API key not found")
client = Groq(api_key=api_key)


def build_system_prompt(topic, stance):
    return f"""
You are an expert debater.

Topic: {topic}
Your stance: {stance}

Rules:
- Give strong logical arguments
- Keep responses short (2-3 lines)
- Be persuasive and confident
- Counter opponent points
"""


def get_ai_reply(messages):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",   # LLaMA model
            messages=messages,
            temperature=0.7,
            max_tokens=80   # 🔥 keeps replies short
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("AI Error:", e)
        return f"Error: {str(e)}"  


def evaluate_winner(conversation):
    try:
        prompt = f"""
You are an evaluator.

Analyze the debate below and return ONLY valid JSON.

Debate:
{conversation}

STRICT RULES:
- Do NOT write anything except JSON
- Do NOT add explanation
- Do NOT add extra text

FORMAT:
{{
    "winner": "User or AI",
    "user_score": 0-10,
    "ai_score": 0-10,
    "reason1": "short reason",
    "reason2": "short reason"
}}
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        result = response.choices[0].message.content.strip()

        print("🔥 RAW AI RESULT:", result)  # DEBUG

        return result

    except Exception as e:
        print("🔥 ERROR:", e)
        return None

def correct_english(text):
    try:
        prompt = f"""
Correct the grammar of this sentence:

{text}

Return only corrected sentence.
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("Correction error:", e)
        return text
