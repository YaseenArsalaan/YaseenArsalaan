import streamlit as st
from openai import OpenAI
import os

# -------------------- CONFIG --------------------
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
st.set_page_config(page_title="Yaseen AI Career System")

st.title("🧠 Yaseen AI Career Intelligence System")
st.write("AI-powered portfolio | Data Scientist | LLM + RAG")

# -------------------- LOAD RESUME --------------------
with open("resume.txt", "r") as f:
    resume = f.read()

# -------------------- SIDEBAR --------------------
option = st.sidebar.selectbox(
    "Choose Feature",
    [
        "💬 AI Interview Chat",
        "📊 Resume Analyzer",
        "🎯 Job Match",
        "🔥 HR Killer Answers",
        "🚀 My Projects (Explained)",
        "💼 Why Hire Me?"
    ]
)

# -------------------- 1. AI INTERVIEW CHAT --------------------
if option == "💬 AI Interview Chat":
    query = st.text_input("Ask anything about Yaseen")

    if query:
        prompt = f"""
        You are Yaseen Arsalaan Mohammed himself, answering confidently in an interview.

        - Speak in first person ("I", "my experience")
        - Be specific with projects, metrics, and tools
        - Sound human, not robotic
        - Keep answers concise but impactful

        RESUME:
        {resume}

        QUESTION:
        {query}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        st.write("🤖 AI Response")
        st.write(response.choices[0].message.content)

# -------------------- 2. RESUME ANALYZER --------------------
elif option == "📊 Resume Analyzer":
    text = st.text_area("Paste any resume")

    if text:
        prompt = f"""
        You are an expert HR and ATS system.

        Analyze this resume and provide:

        1. Strengths
        2. Weaknesses
        3. Missing skills
        4. Improvements
        5. ATS Score (out of 100)
        6. Final verdict (Shortlist or Reject)

        RESUME:
        {text}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        st.write("📊 Analysis Result")
        st.write(response.choices[0].message.content)

# -------------------- 3. JOB MATCH --------------------
elif option == "🎯 Job Match":
    jd = st.text_area("Paste Job Description")

    if jd:
        prompt = f"""
        You are a hiring manager.

        Compare this resume with the job description.

        Provide:

        1. Match Percentage
        2. Matching Skills
        3. Missing Skills
        4. What Yaseen should learn
        5. Hiring Decision (Strong / Moderate / Weak)

        RESUME:
        {resume}

        JOB DESCRIPTION:
        {jd}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        st.write("📊 Job Match Report")
        st.write(response.choices[0].message.content)

# -------------------- 4. HR KILLER ANSWERS --------------------
elif option == "🔥 HR Killer Answers":
    question = st.selectbox(
        "Choose Interview Question",
        [
            "Tell me about yourself",
            "Why should we hire you?",
            "What are your strengths?",
            "What are your weaknesses?",
            "Explain your projects",
            "Where do you see yourself in 5 years?"
        ]
    )

    if question:
        prompt = f"""
        You are Yaseen.

        Generate a PERFECT answer.

        - Natural (human tone)
        - Confident
        - Concise but impactful
        - Based on real experience

        RESUME:
        {resume}

        QUESTION:
        {question}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        st.write("🔥 Best Answer")
        st.write(response.choices[0].message.content)

# -------------------- 5. PROJECT EXPLAINER --------------------
elif option == "🚀 My Projects (Explained)":
    project = st.selectbox(
        "Select Project",
        [
            "Fraud Detection System",
            "Credit Risk Prediction",
            "GenAI Support Bot",
            "Real-Time ML Pipeline",
            "NLP Compliance Engine"
        ]
    )

    prompt = f"""
    You are Yaseen explaining your project in an interview.

    Include:
    - Problem
    - Approach
    - Tools used
    - Results (metrics)
    - Business impact

    Speak in first person.

    RESUME:
    {resume}

    PROJECT:
    {project}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    st.write("🚀 Project Explanation")
    st.write(response.choices[0].message.content)

# -------------------- 6. WHY HIRE ME --------------------
elif option == "💼 Why Hire Me?":
    prompt = f"""
    You are Yaseen.

    Answer: "Why should we hire you?"

    Make it:
    - Confident
    - Data-driven
    - Focused on impact
    - Short and powerful

    RESUME:
    {resume}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    st.write("💼 Why Hire Me")
    st.write(response.choices[0].message.content)
