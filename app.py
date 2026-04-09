import streamlit as st
from openai import OpenAI

# -------------------- CONFIG --------------------
client = OpenAI(api_key="YOUR_API_KEY")

st.set_page_config(page_title="Yaseen AI Career System")

st.title("🧠 Yaseen AI Career System")
st.write("AI-powered portfolio | Data Scientist")

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
        "🔥 HR Killer Answers"
    ]
)

# -------------------- 1. AI INTERVIEW CHAT --------------------
if option == "💬 AI Interview Chat":
    query = st.text_input("Ask anything about Yaseen")

    if query:
        prompt = f"""
        You are a senior recruiter interviewing a Data Scientist.

        Answer questions about Yaseen Arsalaan Mohammed using ONLY the resume below.

        Your answers must be:
        - Professional
        - Confident
        - Clear
        - Interview-ready

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
        You are an expert interview coach.

        Generate a PERFECT answer for this interview question based on Yaseen's resume.

        The answer must:
        - Sound natural (human, not robotic)
        - Be confident
        - Be concise but impactful
        - Impress HR

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
