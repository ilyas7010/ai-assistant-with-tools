# 🤖 AI Assistant with Tools

## 📌 Overview

For my first AI project, I created a simple AI assistant built with **Python, LangChain, and OpenAI**.
The assistant can chat with users and perform simple tasks using custom tools such as a **calculator** and **greeting function**.
This project demonstrates how AI assistants can combine natural conversation with tool execution.

---

## ⚙️ Features

✅ Chat with an AI assistant  
✅ Perform basic arithmetic calculations  
✅ Greet users by name  
✅ Demonstrates simple AI tool usage with LangChain  

---

## 🧠 How It Works

The assistant runs in the terminal and processes user input.

Workflow:

User input → detect command → run tool or AI → return response

Example 1:

You: greet jack

Assistant: Hi Jack, I hope you are well

&

Example 2:

You: 99 + 100 -32  

Assistant: 99 + 100 - 32 = 167.

You: add 300 and 900

Assistant: 300 plus 900 equals 1200.


***If the input is not a tool command, the message is sent to the AI model for a normal response.***

---

## 🛠️ Tech Stack

- 🐍 Python
- 🧠 LangChain
- 🤖 OpenAI API
- 🔐 python-dotenv

---

## 📦 Installation

Install required packages:

pip install langchain-openai python-dotenv


---

## ▶️ Run the Project

Run the assistant:
python main.py

---

## 🔑 Environment Variable

Create a `.env` file and add your OpenAI API key:

OPENAI_API_KEY=your_api_key_here


---

## 🎯 Purpose

This project helped me learn:

- AI integration with Python
- LangChain tool creation
- OpenAI API usage
- Building simple AI assistants

---

## 🚀 Future Improvements

Possible improvements:

- Add more AI tools
- Connect external APIs
- Add a web interface using Streamlit
- Improve command detection
