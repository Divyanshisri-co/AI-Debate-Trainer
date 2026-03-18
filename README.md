# AI-Debate-Trainer

AI Debate Trainer is a web application where a user can debate with an AI system on a selected topic.
The user chooses the debate topic, duration, and stance (favor or against). The AI automatically takes the opposite side and generates counterarguments. When the debate time ends, the AI judge evaluates the arguments and declares the winner with scores.

---

## Features

* Enter custom debate topic
* Choose debate duration (5 / 10 / 15 minutes)
* Select debate stance (Favor or Against)
* AI automatically argues the opposite side
* Real-time debate interaction
* Countdown timer for debate duration
* AI judge evaluates debate after time ends
* Result dashboard showing:

  * Winner
  * Logic score
  * Clarity score
  * Confidence score
  * Two reasons for the decision

---

## Tech Stack

Backend

* Python
* Django

AI Model

* Groq API
* LLaMA 3.1 model

Frontend

* HTML
* CSS
* Bootstrap
* JavaScript

---

## Project Workflow

1. User enters debate topic.
2. User selects debate time.
3. User selects stance (Favor / Against).
4. Debate starts and AI responds with counterarguments.
5. Timer runs during the debate.
6. When time ends, debate stops automatically.
7. AI judge analyzes the conversation.
8. Result dashboard displays winner and evaluation scores.

---

## Installation

Clone the repository

git clone https://github.com/yourusername/ai-debate-trainer.git

cd ai-debate-trainer

Install dependencies

pip install -r requirements.txt

Add your Groq API key in:

debate/ai_service.py

Run the project

python manage.py runserver

Open in browser

http://127.0.0.1:8000

---

## Future Improvements

* Debate history storage using database
* Grammar correction for user arguments
* Speech-based debate (voice input)
* Real-time scoring during debate
* Multiple AI debate personalities

---

## Author

B.Tech Computer Science with Artificial Intelligence
