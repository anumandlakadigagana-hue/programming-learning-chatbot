# 💻 Programming Learning Chatbot Using LLM

## 📌 Project Overview

**Programming Learning Chatbot Using LLM** is an AI-based educational chatbot designed to help students learn programming concepts easily.

The chatbot uses a **Large Language Model (LLM)** through **Ollama** and provides answers according to the programming language selected by the user.

The application is developed using **Python and Streamlit** and runs the LLM locally without requiring an API key.

---

## 🎯 Objectives

* Help students learn programming concepts.
* Provide beginner-friendly programming explanations.
* Provide very simple, simple, or detailed explanations.
* Support multiple programming languages.
* Answer programming questions using a local LLM.
* Explain programming code and expected output.
* Explain programming errors and their solutions.

---

## 🚀 Features

* 🤖 AI-powered programming chatbot
* 💻 Multiple programming language support
* 📝 Very Simple explanation mode
* 📚 Simple explanation mode
* 📖 Detailed explanation mode
* 💬 Interactive chat interface
* 🔄 New Chat option
* 📌 Language-specific question answering
* 💡 Example questions for each language
* 🧑‍💻 Code examples and output explanations
* ❌ Error explanation and correction
* 🔒 Local LLM
* 🔑 No API key required

---

## 🛠️ Technologies Used

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Main programming language |
| Streamlit    | Web application interface |
| Ollama       | Local LLM platform        |
| Llama 3.2 3B | Language model            |
| HTML/CSS     | Interface styling         |

---

## 🌐 Supported Programming Languages

The chatbot supports:

* ☕ Java
* 🐍 Python
* 🔵 C
* 🔷 C++
* 🗄️ SQL
* 🟨 JavaScript
* 🌐 HTML
* 🎨 CSS

---

## 📂 Project Structure

```text
programming_learning_chatbot/
│
├── app.py
└── README.md
```

### `app.py`

Contains the complete Streamlit application, chatbot logic, language selection, explanation styles, Ollama connection, chat history, and user interface.

### `README.md`

Contains the documentation and instructions for the project.

---

## ⚙️ Requirements

Before running the project, install:

* Python
* Streamlit
* Ollama
* Llama 3.2 3B model

---

## 📥 Installation

### 1. Install Python

Install Python on your computer and make sure Python is available from the command line.

Check the installation:

```bash
python --version
```

### 2. Install Python Packages

Open Command Prompt or PowerShell and run:

```bash
pip install streamlit ollama
```

### 3. Install Ollama

Install Ollama and make sure it is running on your computer.

### 4. Download the LLM Model

The project uses:

```text
llama3.2:3b
```

Download the model using:

```bash
ollama pull llama3.2:3b
```

You can check the installed models using:

```bash
ollama list
```

---

## ▶️ How to Run the Project

Open the project folder in Command Prompt or PowerShell.

For example:

```bash
cd C:\programming_learning_chatbot
```

Run the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will open in your web browser.

Usually, Streamlit runs at:

```text
http://localhost:8501
```

---

## 🔄 How the Chatbot Works

The basic working process is:

```text
User
  ↓
Select Programming Language
  ↓
Select Explanation Style
  ↓
Enter Programming Question
  ↓
Streamlit Application
  ↓
Create Prompt
  ↓
Ollama
  ↓
Llama 3.2 3B
  ↓
Generate Answer
  ↓
Display Answer
```

---

## 🧠 Explanation Styles

The chatbot provides three explanation styles.

### 1. Very Simple

Provides a short and easy explanation.

It generally includes:

* Short definition
* Small example when necessary

It avoids unnecessary theory and lengthy explanations.

### 2. Simple

Provides a medium-length explanation.

It can include:

* Definition
* Simple explanation
* Example
* Small code example
* Output
* Important points

### 3. Detailed

Provides a complete educational explanation.

It can include:

* Definition
* Introduction
* Why it is used
* How it works
* Syntax
* Examples
* Complete code
* Explanation
* Expected output
* Advantages
* Limitations
* Common mistakes
* Important points
* Summary

---

## 🔒 Language Restriction

The selected programming language works as a **strict subject filter**.

For example, if the user selects **SQL**, the chatbot should answer SQL-related questions.

If the user selects SQL and asks:

```text
What is inheritance in Java?
```

the chatbot will not explain Java inheritance. Instead, it asks the user to select the correct programming language.

This helps keep the chatbot focused on the selected programming language.

---

## 💬 Example Questions

### Java

```text
What is inheritance in Java?
What is method overloading?
What is an interface?
What is exception handling?
```

### Python

```text
What is a list in Python?
What is a function?
What is a dictionary?
Explain exception handling.
```

### C

```text
What is a pointer?
What is an array?
What is a structure?
Explain functions in C.
```

### C++

```text
What is a class?
What is inheritance?
What is polymorphism?
What is STL?
```

### SQL

```text
What is a primary key?
Explain SQL JOIN.
What is GROUP BY?
Write a SELECT query.
```

### JavaScript

```text
What is a variable?
What is a function?
What is an array?
What is the DOM?
```

### HTML

```text
What is an HTML element?
What is a form?
What are HTML attributes?
How are tables created?
```

### CSS

```text
What is a CSS selector?
What is Flexbox?
What is the box model?
What is CSS Grid?
```

---

## 💾 Chat History

The application maintains the conversation using Streamlit session state.

Previous questions and answers are displayed in the chat interface.

The **New Chat** button clears the current conversation and starts a new chat.

---

## 🔐 API Key

This project does **not require an API key**.

The chatbot uses **Ollama locally** to communicate with the Llama 3.2 3B model.

---

## ✅ Advantages

* Easy for students to use.
* Beginner-friendly explanations.
* Supports multiple programming languages.
* Provides different explanation levels.
* Can explain code and output.
* Can explain programming errors.
* Runs locally.
* Does not require an API key.
* Provides an interactive web interface.

---

## ⚠️ Limitations

* Ollama must be installed and running.
* The required LLM model must be installed.
* Answer quality depends on the selected LLM.
* The chatbot may occasionally generate incorrect information.
* It requires sufficient system resources to run the local LLM.

---

## 🔮 Future Enhancements

The project can be extended with:

* Code execution
* Automatic code debugging
* Programming quizzes
* Practice problems
* User login
* Learning progress tracking
* More programming languages
* Voice-based interaction
* Code compilation
* Database integration

---

## 🏁 Conclusion

The **Programming Learning Chatbot Using LLM** is an AI-based educational application that helps students learn programming concepts through an interactive chatbot.

It combines **Python, Streamlit, Ollama, and Llama 3.2 3B** to provide programming explanations based on the user's selected language and explanation style.

The project demonstrates how a **local Large Language Model can be integrated into an educational application** to support programming learning.

---

## 👩‍💻 Project Information

**Project Name:** Programming Learning Chatbot Using LLM

**Technologies:** Python, Streamlit, Ollama, Llama 3.2 3B

**Domain:** Artificial Intelligence / Large Language Models / Education

**Application:** Programming Learning Assistant

**API Key:** Not Required
