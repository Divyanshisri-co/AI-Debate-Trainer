from django.shortcuts import render, redirect
from django.http import JsonResponse
from .utils import get_ai_reply, build_system_prompt, evaluate_winner, correct_english
from django.views.decorators.csrf import csrf_exempt
import json
# Simple moderation
BAD_WORDS = ["abuse", "vulgar"]

def is_valid_topic(topic):
    return not any(word in topic.lower() for word in BAD_WORDS)


def home(request):
    return render(request, "home.html")


def start_debate(request):
    if request.method == "POST":
        topic = request.POST.get("topic")
        stance = request.POST.get("stance")
        time = int(request.POST.get("time"))

        if not topic or len(topic.strip()) < 3:
            return render(request, "home.html", {"error": "Please enter a valid topic"})

        ai_stance = "Favor" if stance == "Against" else "Against"

        # Store in session
        request.session["topic"] = topic
        request.session["user_stance"] = stance
        request.session["ai_stance"] = ai_stance
        request.session["time"] = time

        # Initialize conversation
        def build_system_prompt(topic, ai_stance):
            return f"""
        You are an AI debate opponent.

        Topic: {topic}
        Your stance: {ai_stance}

        STRICT RULES:
        - Always disagree with the user
        - Never agree
        - Never act like a helper
        -Each response must be COMPLETE sentences
        - Do NOT cut sentences midway
        - No questions
        - Only 1-2 short lines
        - Be direct and argumentative
        """
        system_prompt = build_system_prompt(topic, ai_stance)
        request.session["messages"] = [
            {"role": "system", "content": system_prompt}
        ]

        return redirect("chat")

    return redirect("home")

def debate(request):
    return render(request, "debate.html", {
        "topic": request.session.get("topic")
    })
    
def chat(request):
    return render(request, "debate.html", {
        "topic": request.session.get("topic"),
        "time": request.session.get("time")
    })


@csrf_exempt
def chat_api(request):
    if request.method == "POST":
        user_input = request.POST.get("message")

        corrected = correct_english(user_input)

        messages = request.session.get("messages", [])

        # ✅ ALWAYS ensure system prompt exists
        if not messages or messages[0]["role"] != "system":
            system_prompt = build_system_prompt(
                request.session.get("topic"),
                request.session.get("ai_stance")
            )
            messages.insert(0, {"role": "system", "content": system_prompt})

        # ✅ Strong user instruction
        messages.append({
            "role": "user",
            "content": f"User argument: {user_input}. Give a strong 1-2 line counter-argument only."
        })

        # ✅ Get AI reply
        ai_reply = get_ai_reply(messages)

        # ✅ Save conversation
        messages.append({"role": "assistant", "content": ai_reply})
        request.session["messages"] = messages

        return JsonResponse({
            "reply": ai_reply,
            "corrected": corrected
        })
        
def result(request):
    messages = request.session.get("messages", [])

    conversation_text = ""
    for msg in messages:
        if msg["role"] != "system":
            role = "User" if msg["role"] == "user" else "AI"
            conversation_text += f"{role}: {msg['content']}\n"

    result = evaluate_winner(conversation_text)

    try:
        data = json.loads(result)
    except:
        data = {
            "winner": "Unknown",
            "user_score": 0,
            "ai_score": 0,
            "reason1": "Error parsing result",
            "reason2": ""
        }

    return render(request, "result.html", {"data": data})


def start_debate(request):
    if request.method == "POST":
        topic = request.POST.get("topic")
        stance = request.POST.get("stance")

        # Opposite stance for AI
        ai_stance = "Against" if stance == "Favor" else "Favor"

        # Store in session
        request.session["topic"] = topic
        request.session["user_stance"] = stance
        request.session["ai_stance"] = ai_stance
        request.session["messages"] = []

        return redirect("/chat/")