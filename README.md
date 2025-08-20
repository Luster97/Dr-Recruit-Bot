# Dr-Recruit-Bot
A simple Telegram bot that uses NLP (via SpaCy) to assist users in analyzing job descriptions and resumes. It identifies key keywords, responsibilities, and strong action verbs to help you tailor your application materials more effectively.

## ✅ Features

- Extracts key terms from job descriptions
- Highlights strong action verbs from resume text
- Lightweight NLP using SpaCy
- Works inside Telegram

## 🔗 GitHub Repository

🔗 **Repo URL**: [https://github.com/Luster97/Chatbot](https://github.com/Luster97/Chatbot)

## 🚀 How to Set Up Locally

1. **Clone the repository**

```bash
git clone https://github.com/Luster97/Chatbot.git
cd Chatbot
2.	Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
3.	Install required dependencies
pip install -r requirements.txt
4.	Download the SpaCy English model
python -m spacy download en_core_web_sm
5.	Create a .env file in the root directory and paste your Telegram bot token
TELEGRAM_TOKEN=your_bot_token_here
6.	Run the bot
python bot.py
🧪 How to Test
•	Start the bot using /start
•	Paste a job description → the bot will extract key terms
•	Paste a resume snippet → the bot will highlight action verbs
•	Use /help to get a quick command overview
⚠️ Limitations
•	Supports English only
•	Doesn’t yet compare job descriptions against resumes (just analyzes each individually)
•	Only accepts plain text — no file uploads
•	Can misinterpret complex or highly formatted input
💡 Future Features
•	Resume-vs-job-description keyword matching
•	File support (PDFs, DOCX)
•	Integration with advanced language models for personalized suggestions
•	Multilingual support

---

## 🚀 Final Steps to Push Your Code

If you're doing this for the first time, here's a quick guide:

1. Open a terminal in your project folder and run:

```bash
git init
git remote add origin https://github.com/Luster97/Chatbot.git
git add .
git commit -m "Initial commit with working chatbot"
git push -u origin master  # or 'main' if that's your default
2.	Confirm that your files (especially bot.py, handlers/nlp_handlers.py, README.md, etc.) are showing up on GitHub.
