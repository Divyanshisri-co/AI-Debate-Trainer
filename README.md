# AI-Debate-Trainer
AI Debate Trainer is an interactive web application where users can debate with an AI system on any topic. The system evaluates the debate and provides scores for logic, clarity, and confidence, and declares a winner.

Features

User selects debate topic

Select debate time (5 / 10 / 15 minutes)

Choose debate stance (Favor / Against)

Real-time AI counterarguments

Debate timer

AI judge evaluates performance

Result dashboard with:

Logic score

Clarity score

Confidence score

Winner announcement

Reasons for the decision

Tech Stack

Backend:

Python

Django

AI:

Groq API

LLaMA 3.1 Model

Frontend:

HTML

CSS

Bootstrap

JavaScript

How It Works

User enters debate topic and selects time.

User chooses whether they are in favor or against the topic.

AI takes the opposite side automatically.

Debate continues until the timer ends.

AI judge analyzes the arguments and declares the winner.

Installation

pip install -r requirements.txt

Add your Groq API key inside:

debate/ai_service.py

Run the server

python manage.py runserver

Open in browser

http://127.0.0.1:8000



Author: Divyanshisri-co
