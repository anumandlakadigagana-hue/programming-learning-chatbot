# 💻 Programming Learning Chatbot Using LLM

## 📌 Project Overview

**Programming Learning Chatbot Using LLM** is an AI-based chatbot that helps students learn programming concepts through simple and detailed explanations.

The chatbot allows the user to select a programming language and ask programming-related questions. It uses a **Large Language Model (LLM)** through **Ollama** to generate answers.

The application is developed using **Python** and **Streamlit** to provide a simple and interactive web interface.

---

## 🎯 Objectives

* To help students learn programming concepts easily.
* To provide simple explanations for programming questions.
* To provide detailed explanations when required.
* To support multiple programming languages.
* To generate answers using an LLM.
* To provide an interactive chatbot interface.

---

## 🚀 Features

* 🤖 AI-powered programming chatbot
* 💬 Ask programming questions in natural language
* 🐍 Python support
* ☕ Java support
* 🗄️ SQL support
* 📝 Simple explanation mode
* 📚 Detailed explanation mode
* 🌐 User-friendly Streamlit interface
* 🔒 Runs locally using Ollama

---

## 🛠️ Technologies Used

| Technology | Purpose                       |
| ---------- | ----------------------------- |
| Python     | Main programming language     |
| Streamlit  | Web interface                 |
| Ollama     | Runs the LLM locally          |
| LLM        | Generates programming answers |
| HTML/CSS   | User interface styling        |

---

## 📂 Project Structure

```text
programming_learning_chatbot/
│
├── app.py
├── requirements.txt
└── README.md
```

### `app.py`

Contains the main Python code for the Streamlit chatbot application.

### `requirements.txt`

Contains the Python libraries required to run the project.

### `README.md`

Contains the project documentation and setup instructions.

---

## ⚙️ Requirements

Before running the project, install:

* Python
* Ollama
* Required Python packages
* An Ollama LLM model

---

## 📥 Installation

### 1. Clone or create the project

Open Command Prompt or PowerShell and go to the project folder:

```bash
cd C:\programming_learning_chatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

```bash
venv\Scripts\activate
```

### 4. Install required packages

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install the main packages using:

```bash
pip install streamlit ollama
```

---

## 🤖 Ollama Setup

Install Ollama and make sure it is running on your computer.

Pull the required LLM model, for example:

```bash
ollama pull llama3.2:3b
```

Check whether the model is available:

```bash
ollama list
```

You should see the installed model in the list.

---

## ▶️ Running the Project

First activate the virtual environment:

```bash
venv\Scripts\activate
```

Then run the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

Usually, it will be available at:

```text
http://localhost:8501
```

---

## 💡 How the Chatbot Works

The working process of the project is:

```text
User
  ↓
Select Programming Language
  ↓
Enter Programming Question
  ↓
Select Explanation Type
  ↓
Streamlit Application
  ↓
Prompt sent to LLM through Ollama
  ↓
LLM generates answer
  ↓
Answer displayed to User
```

---

##
