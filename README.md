# 🧠 AI Debate Trainer

An AI-powered web application that allows users to engage in real-time debates with an intelligent AI opponent, receive instant feedback, and improve their argumentation and communication skills.

---

## 📌 Project Overview

AI Debate Trainer is a **full-stack Django-based application** that simulates a structured debate between a user and an AI system. The platform leverages **Large Language Models (LLMs)** and **prompt engineering** to generate intelligent counterarguments, correct user input, and evaluate performance.

This project demonstrates the integration of:

* Web development (Django)
* AI/LLM APIs
* NLP-based evaluation
* Real-time interactive UI

---

## 🚀 Core Features

### 🎯 1. Custom Debate Setup

* User can:

  * Enter any topic (dynamic input)
  * Choose stance: **Favor / Against**
  * Select time duration:

    * 3 min
    * 5 min
    * 10 min

👉 AI automatically takes the **opposite stance**

---

### 💬 2. Real-Time AI Debate

* Chat-based interface
* User vs AI argument exchange
* AI responses:

  * Context-aware (uses conversation history)
  * Short (1–2 lines)
  * Logical and opposing arguments

---

### ✍️ 3. English Correction System

* Each user input is analyzed
* Grammar corrections shown instantly
* Helps improve:

  * Sentence structure
  * Clarity
  * Fluency

---

### ⏱️ 4. Timer-Based Debate System

* Countdown timer displayed
* Debate ends automatically when time is up
* Prevents unlimited conversation

---

### 📊 5. AI-Based Scoring System

After debate ends:

System evaluates:

* Relevance to topic
* Logical reasoning
* Clarity of arguments
* Language quality

---

### 🏆 6. Result Dashboard

Displays:

* Winner (highlighted)
* User score
* AI score
* Key feedback (2 reasons)

---

## 🧠 AI & NLP Implementation

### 🔹 LLM Integration

* Uses external AI API (via `utils.py`)
* Functions:

  * `get_ai_reply()` → generates argument
  * `correct_english()` → grammar correction
  * `evaluate_debate()` → scoring

---

### 🔹 Prompt Engineering

Custom prompts designed to:

* Force AI to take opposite stance
* Limit response length
* Avoid incomplete sentences
* Maintain debate structure

---

### 🔹 Context Handling

* Stores conversation in session
* Sends full history to AI
* Ensures coherent responses

---

## 🛠️ Tech Stack

### 🔹 Backend

* Python
* Django (MVC architecture)
* Session management

---

### 🔹 Frontend

* HTML5
* CSS3 (custom UI styling)
* JavaScript (AJAX for real-time chat)

---

### 🔹 AI / NLP

* LLM API (Groq / LLaMA / OpenAI-like)
* Prompt Engineering
* Text correction logic

---

### 🔹 Database

* SQLite (default Django database)

---

### 🔹 Deployment

* Render (Cloud deployment)
* Gunicorn (WSGI server)

---

## 📁 Project Structure

```id="proj123"
AI_DEBATE_SYS/
│
├── ai_debate_trainer/        # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── debate/                   # Core app
│   ├── views.py              # Handles logic & APIs
│   ├── urls.py
│   ├── utils.py              # AI + scoring logic
│   ├── models.py
│   ├── migrations/
│
├── templates/
│   ├── home.html
│   ├── debate.html
│   ├── result.html
│
├── static/
│   ├── css/
│   ├── js/
│
├── manage.py
├── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Divyanshisri-co/AI-Debate-Trainer.git
cd AI-Debate-Trainer
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Start Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## 🔑 Environment Variables

Create `.env` file:

```env
API_KEY=your_api_key_here
```

---

## 🔄 Application Workflow

1. User inputs topic + stance + time
2. Django stores session data
3. Debate begins (chat interface)
4. User sends message → AI responds
5. English correction shown
6. Timer ends
7. AI evaluates debate
8. Result page displays winner + feedback

---

## 🎯 Skills Demonstrated

### 💻 Development

* Full-stack web development (Django)
* REST-like API handling (AJAX)

### 🤖 AI / NLP

* LLM integration
* Prompt engineering
* Text correction
* Context-aware response generation

### 🧠 Core Concepts

* Session management
* Real-time interaction
* UI/UX design
* System design thinking

---

## 🚀 Deployment (Render)

* Build Command:

```
pip install -r requirements.txt
```

* Start Command:

```
gunicorn ai_debate_trainer.wsgi
```

---

## 📌 Future Improvements

* User authentication system
* Debate history tracking
* Advanced scoring (ML-based)
* Voice-based debate (speech-to-text)
* Multi-language support

---

## 👩‍💻 Author

**Divyanshi**

---

## ⭐ Support

If you like this project:

* Star ⭐ the repo
* Share it
* Use it for learning

---

