# 🤖 Gemini CLI Agent

A simple Agentic AI command-line assistant built with Python and Google's Gemini API.

The assistant can decide when to use external tools such as a calculator or web search through Gemini's built-in function calling capability.

---

## ✨ Features

- 🤖 AI-powered conversational assistant
- ➕ Calculator tool
- 🌐 Web search using DuckDuckGo
- 💬 Interactive command-line interface
- 🔐 Secure API key management using environment variables

---

## 🛠️ Tech Stack

- Python 3
- Google Gemini API
- google-genai SDK
- DuckDuckGo Search (DDGS)
- python-dotenv

---

## 📂 Project Structure

```
gemini-cli-agent/
│
├── agent.py
├── config.py
├── tools.py
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
└── LICENSE
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/gemini-cli-agent.git
```

Move into the project folder

```bash
cd gemini-cli-agent
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

Example:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run

```bash
python agent.py
```

---

## Example

```
You: What is 24 × 18?

Agent:
432
```

```
You: Latest AI news

Agent:
(Searches the web...)

...
```

---

## 📌 Future Improvements

- Weather Tool
- Wikipedia Tool
- File Reader
- Conversation Memory
- Voice Input
- GUI Version

---

## 📄 License

This project is licensed under the MIT License.