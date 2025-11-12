import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.text_analyzer import calculate_match

st.set_page_config(page_title="AI Resume Tailor", page_icon="🤖", layout="centered")

st.title("🤖 AI Resume Tailor")
st.write("Match your resume with a job description and get instant insights!")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description here:")

if uploaded_file and job_description:
    with st.spinner("Analyzing..."):
        resume_text = extract_text_from_pdf(uploaded_file)
        match_score = calculate_match(resume_text, job_description)
    
    st.success(f"🎯 Match Score: {match_score}%")

    if match_score < 60:
        st.warning("Your resume and job description seem less aligned. Try adding relevant keywords!")
    else:
        st.info("Great! Your resume aligns well with this job posting.")

st.markdown("---")
st.caption("Built by Dehan Nimna & Sandaruvi Dias")
