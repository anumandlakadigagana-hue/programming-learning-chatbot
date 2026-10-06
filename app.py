import streamlit as st
import ollama

# ============================================================
# PROGRAMMING LEARNING CHATBOT USING LLM
# ============================================================

# ------------------------------------------------------------
# PAGE CONFIGURATION
# ------------------------------------------------------------

st.set_page_config(
    page_title="Programming Learning Chatbot",
    page_icon="💻",
    layout="wide"
)

# ------------------------------------------------------------
# CUSTOM CSS
# ------------------------------------------------------------

st.markdown("""
<style>

.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 25px;
}

</style>
""", unsafe_allow_html=True)


# ------------------------------------------------------------
# TITLE
# ------------------------------------------------------------

st.markdown(
    '<div class="title">💻 Programming Learning Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Learn programming concepts using a Local LLM'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("⚙️ Chatbot Settings")

    # --------------------------------------------------------
    # PROGRAMMING LANGUAGE
    # --------------------------------------------------------

    language = st.selectbox(
        "Select Programming Language",
        [
            "Java",
            "Python",
            "C",
            "C++",
            "SQL",
            "JavaScript",
            "HTML",
            "CSS"
        ]
    )

    # --------------------------------------------------------
    # EXPLANATION STYLE
    # --------------------------------------------------------

    explanation_style = st.selectbox(
        "Select Explanation Style",
        [
            "Very Simple",
            "Simple",
            "Detailed"
        ]
    )

    st.divider()

    # --------------------------------------------------------
    # TOPICS
    # --------------------------------------------------------

    st.subheader("📚 Available Topics")

    if language == "Java":

        st.write("☕ Java")
        st.write("• Variables")
        st.write("• Data Types")
        st.write("• Operators")
        st.write("• Loops")
        st.write("• Arrays")
        st.write("• Methods")
        st.write("• Classes")
        st.write("• Objects")
        st.write("• Inheritance")
        st.write("• Polymorphism")
        st.write("• Encapsulation")
        st.write("• Abstraction")
        st.write("• Interfaces")
        st.write("• Exception Handling")
        st.write("• Multithreading")

    elif language == "Python":

        st.write("🐍 Python")
        st.write("• Variables")
        st.write("• Data Types")
        st.write("• Lists")
        st.write("• Tuples")
        st.write("• Dictionaries")
        st.write("• Sets")
        st.write("• Conditions")
        st.write("• Loops")
        st.write("• Functions")
        st.write("• Classes")
        st.write("• Exceptions")
        st.write("• File Handling")

    elif language == "C":

        st.write("🔵 C")
        st.write("• Variables")
        st.write("• Data Types")
        st.write("• Operators")
        st.write("• Conditions")
        st.write("• Loops")
        st.write("• Arrays")
        st.write("• Functions")
        st.write("• Pointers")
        st.write("• Structures")
        st.write("• Files")

    elif language == "C++":

        st.write("🔷 C++")
        st.write("• Variables")
        st.write("• Data Types")
        st.write("• Conditions")
        st.write("• Loops")
        st.write("• Arrays")
        st.write("• Functions")
        st.write("• Classes")
        st.write("• Objects")
        st.write("• Inheritance")
        st.write("• Polymorphism")
        st.write("• STL")

    elif language == "SQL":

        st.write("🗄️ SQL")
        st.write("• SELECT")
        st.write("• INSERT")
        st.write("• UPDATE")
        st.write("• DELETE")
        st.write("• WHERE")
        st.write("• ORDER BY")
        st.write("• GROUP BY")
        st.write("• HAVING")
        st.write("• JOIN")
        st.write("• Subqueries")
        st.write("• Primary Key")
        st.write("• Foreign Key")
        st.write("• Aggregate Functions")

    elif language == "JavaScript":

        st.write("🟨 JavaScript")
        st.write("• Variables")
        st.write("• Data Types")
        st.write("• Functions")
        st.write("• Arrays")
        st.write("• Objects")
        st.write("• Loops")
        st.write("• DOM")
        st.write("• Events")
        st.write("• Promises")

    elif language == "HTML":

        st.write("🌐 HTML")
        st.write("• Elements")
        st.write("• Tags")
        st.write("• Attributes")
        st.write("• Forms")
        st.write("• Tables")
        st.write("• Lists")
        st.write("• Links")
        st.write("• Images")

    elif language == "CSS":

        st.write("🎨 CSS")
        st.write("• Selectors")
        st.write("• Colors")
        st.write("• Fonts")
        st.write("• Box Model")
        st.write("• Flexbox")
        st.write("• Grid")
        st.write("• Positioning")

    st.divider()

    # --------------------------------------------------------
    # NEW CHAT
    # --------------------------------------------------------

    if st.button(
        "🆕 New Chat",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()


# ============================================================
# EXPLANATION STYLE
# ============================================================

def get_style_instruction():

    # --------------------------------------------------------
    # VERY SIMPLE
    # --------------------------------------------------------

    if explanation_style == "Very Simple":

        return """
The user selected VERY SIMPLE.

Give a very short and easy answer.

Use:

1. Short definition.
2. One small example if necessary.

Rules:

- Use very easy words.
- Keep the answer short.
- Do not give long theory.
- Do not give many examples.
- Do not give advantages and disadvantages.
- Do not give unnecessary information.

The answer should normally be around 2 to 6 short paragraphs
or a few short bullet points.
"""


    # --------------------------------------------------------
    # SIMPLE
    # --------------------------------------------------------

    elif explanation_style == "Simple":

        return """
The user selected SIMPLE.

Give a clear medium-length answer.

Use:

1. Definition
2. Simple explanation
3. One example
4. Small code example when required
5. Output when code is provided
6. A few important points

Rules:

- Use simple words.
- Explain the main idea clearly.
- Give only one or two examples.
- Do not give a very long explanation.
- Do not give unnecessary theory.
- Do not give a long line-by-line explanation.

The answer must be noticeably shorter than a Detailed answer.
"""


    # --------------------------------------------------------
    # DETAILED
    # --------------------------------------------------------

    else:

        return """
The user selected DETAILED.

Give a complete and detailed educational answer.

Do not give only a short definition.

Use suitable sections such as:

1. Definition
2. Introduction
3. Why it is used
4. How it works
5. Important concepts
6. Syntax
7. Simple example
8. Detailed example
9. Complete program or query
10. Explanation
11. Expected output
12. Output explanation
13. Advantages
14. Disadvantages or limitations
15. Common mistakes
16. Important points
17. Summary

For programming questions:

- Give complete code when appropriate.
- Explain the important lines.
- Show expected output.
- Explain why the output occurs.
- Explain the programming logic.

The answer should be substantially longer than a Simple answer.
"""


# ============================================================
# LANGUAGE RESTRICTION
# ============================================================

def get_language_rule():

    return f"""
STRICT LANGUAGE RULE:

The user selected:

{language}

You MUST answer ONLY questions related to {language}.

Do NOT answer questions about other programming languages.

Examples:

If the selected language is SQL:

Allowed:
- What is a primary key?
- Explain JOIN.
- What is GROUP BY?
- Write a SELECT query.
- Explain WHERE clause.

Not allowed:
- What is inheritance in Java?
- What is a Python list?
- What is a pointer in C?

If the user asks a question belonging to another language,
do NOT answer that question.

Instead respond:

"⚠️ This question is not related to {language}.
Please select the correct programming language from the
sidebar and ask your question again."

IMPORTANT:

Do not convert another language's question into {language}.

For example, if SQL is selected and the user asks:

"What is inheritance in Java?"

Do NOT explain inheritance.

Tell the user to select Java.

The selected language is a STRICT subject filter.
"""


# ============================================================
# SYSTEM PROMPT
# ============================================================

def create_system_prompt():

    style_instruction = get_style_instruction()

    language_rule = get_language_rule()

    system_prompt = f"""
You are a Programming Learning Chatbot.

Your purpose is to teach students programming.

============================================================
SELECTED PROGRAMMING LANGUAGE
============================================================

{language}

============================================================
STRICT LANGUAGE RESTRICTION
============================================================

{language_rule}

============================================================
CURRENT EXPLANATION STYLE
============================================================

{explanation_style}

{style_instruction}

============================================================
IMPORTANT STYLE RULE
============================================================

The explanation style can change between questions.

Always follow the CURRENT selected style.

If the user changes:

Detailed → Simple

then give a Simple answer.

If the user changes:

Simple → Detailed

then give a Detailed answer.

Do not copy the length of previous answers.

The current selection always has priority.

============================================================
PROGRAMMING RULES
============================================================

1. Give correct information.

2. Answer ONLY the selected programming language.

3. Use beginner-friendly language.

4. If the user asks for code, provide correct code.

5. Use proper indentation.

6. Show expected output when appropriate.

7. Explain the output.

8. If the user gives an error, explain:
   - What the error means
   - Why it occurred
   - How to fix it
   - Corrected code

9. If the user asks for a comparison, use a table when useful.

10. If the user asks for a definition, follow the selected
    explanation style.

11. Do not claim that code was executed if it was not executed.

12. Do not use an API key.

13. You are running through a local Ollama LLM.

14. Do not unnecessarily repeat information.

============================================================
FINAL INSTRUCTION
============================================================

Selected Language:
{language}

Current Style:
{explanation_style}

Follow BOTH settings exactly.
"""


    return system_prompt


# ============================================================
# ASK OLLAMA
# ============================================================

def ask_ollama(question):

    system_prompt = create_system_prompt()

    # --------------------------------------------------------
    # SYSTEM MESSAGE
    # --------------------------------------------------------

    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    # --------------------------------------------------------
    # PREVIOUS CONVERSATION
    # --------------------------------------------------------

    for message in st.session_state.messages:

        messages.append(
            {
                "role": message["role"],
                "content": message["content"]
            }
        )

    # --------------------------------------------------------
    # CURRENT QUESTION
    # --------------------------------------------------------

    current_question = f"""
CURRENT QUESTION:

{question}

============================================================

CURRENT SETTINGS:

Selected Programming Language:
{language}

Selected Explanation Style:
{explanation_style}

============================================================

IMPORTANT:

1. Check whether the question belongs to {language}.

2. If it does NOT belong to {language}, do NOT answer it.

3. Tell the user to select the correct programming language.

4. If it DOES belong to {language}, answer it using the
   {explanation_style} explanation style.

5. Do not let previous conversation change the current
   explanation style.

6. The current settings are more important than previous
   responses.
"""

    messages.append(
        {
            "role": "user",
            "content": current_question
        }
    )

    # --------------------------------------------------------
    # OLLAMA
    # --------------------------------------------------------

    try:

        response = ollama.chat(
            model="llama3.2:3b",
            messages=messages
        )

        answer = response["message"]["content"]

        return answer

    except Exception as e:

        return f"""
## ❌ Ollama Connection Error

The chatbot could not connect to Ollama.

Please make sure Ollama is running.

Installed model:

`llama3.2:3b`

Error:

`{str(e)}`
"""


# ============================================================
# DISPLAY PREVIOUS CHAT
# ============================================================

for message in st.session_state.messages:

    if message["role"] == "user":

        with st.chat_message("user"):

            st.markdown("### 👤 Question")

            st.write(message["content"])

    else:

        with st.chat_message("assistant"):

            st.markdown("### 🤖 Answer")

            st.markdown(message["content"])


# ============================================================
# QUESTION BOX
# ============================================================

st.subheader("💬 Ask Your Question")

st.caption(
    f"Selected language: {language} | "
    f"Explanation style: {explanation_style}"
)

user_question = st.chat_input(
    f"Ask a {language} question..."
)


# ============================================================
# PROCESS QUESTION
# ============================================================

if user_question:

    # --------------------------------------------------------
    # SAVE USER QUESTION
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    # --------------------------------------------------------
    # DISPLAY USER QUESTION
    # --------------------------------------------------------

    with st.chat_message("user"):

        st.markdown("### 👤 Question")

        st.write(user_question)

    # --------------------------------------------------------
    # GENERATE ANSWER
    # --------------------------------------------------------

    with st.chat_message("assistant"):

        st.markdown("### 🤖 Answer")

        with st.spinner("🤖 Thinking..."):

            answer = ask_ollama(user_question)

        st.markdown(answer)

    # --------------------------------------------------------
    # SAVE ANSWER
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )


# ============================================================
# EXAMPLE QUESTIONS
# ============================================================

st.divider()

st.subheader("💡 Example Questions")

if language == "Java":

    st.write("• What is inheritance in Java?")
    st.write("• What is method overloading?")
    st.write("• What is an interface?")
    st.write("• What is exception handling?")

elif language == "Python":

    st.write("• What is a list in Python?")
    st.write("• What is a function?")
    st.write("• What is a dictionary?")
    st.write("• Explain exception handling.")

elif language == "C":

    st.write("• What is a pointer?")
    st.write("• What is an array?")
    st.write("• What is a structure?")
    st.write("• Explain functions in C.")

elif language == "C++":

    st.write("• What is a class?")
    st.write("• What is inheritance?")
    st.write("• What is polymorphism?")
    st.write("• What is STL?")

elif language == "SQL":

    st.write("• What is a primary key?")
    st.write("• Explain SQL JOIN.")
    st.write("• What is GROUP BY?")
    st.write("• Write a SELECT query.")

elif language == "JavaScript":

    st.write("• What is a variable?")
    st.write("• What is a function?")
    st.write("• What is an array?")
    st.write("• What is the DOM?")

elif language == "HTML":

    st.write("• What is an HTML element?")
    st.write("• What is a form?")
    st.write("• What are HTML attributes?")
    st.write("• How are tables created?")

elif language == "CSS":

    st.write("• What is a CSS selector?")
    st.write("• What is Flexbox?")
    st.write("• What is the box model?")
    st.write("• What is CSS Grid?")


# ============================================================
# PROJECT INFORMATION
# ============================================================

st.divider()

st.subheader("📌 Project Information")

st.write(
    "**Programming Learning Chatbot Using LLM**"
)

st.write("**Technologies:** Python, Streamlit, Ollama, Llama 3.2 3B")

st.write(
    "**Features:** Language selection, explanation control, "
    "question answering, code examples, output explanation, "
    "error explanation and chat history."
)

st.write(
    "**API Key:** Not required"
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div style="text-align:center;">
        <b>💻 Programming Learning Chatbot</b><br>
        Streamlit + Ollama + Llama 3.2 3B<br>
        🔒 Local LLM • No API Key Required
    </div>
    """,
    unsafe_allow_html=True
)