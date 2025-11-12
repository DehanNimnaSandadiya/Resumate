import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.docx_reader import extract_text_from_docx
from utils.text_analyzer import calculate_match, generate_feedback
from utils.pdf_writer import generate_feedback_pdf

st.set_page_config(page_title="xAI Resume Tailor", page_icon="🤖", layout="centered")
st.title("🤖 xAI Resume Tailor - Premium CV Feedback")
st.write("Upload your CV and paste the Job Description to receive a **detailed, actionable CV audit**.")

uploaded_file = st.file_uploader("Upload your Resume (PDF/DOCX/TXT)", type=["pdf","docx","txt"])
job_description = st.text_area("Paste Job Description here:")

if uploaded_file and job_description:
    file_type = uploaded_file.name.split('.')[-1].lower()

    # Extract resume text
    if file_type == "pdf":
        resume_text = extract_text_from_pdf(uploaded_file)
    elif file_type == "docx":
        resume_text = extract_text_from_docx(uploaded_file)
    elif file_type == "txt":
        resume_text = str(uploaded_file.read(), "utf-8")
    else:
        st.error("Unsupported file type")
        st.stop()

    # Match percentage
    match_score = calculate_match(resume_text, job_description)
    st.metric("CV Match Score", f"{match_score}%")

    # Generate advanced feedback
    feedback_list, skills_found = generate_feedback(resume_text, job_description)

    # Generate premium PDF report
    output_file = generate_feedback_pdf(match_score, skills_found, feedback_list)

    st.success("✅ Premium CV Feedback Report generated!")
    st.download_button("📥 Download Feedback Report", data=open(output_file, "rb"), file_name="Tailored_CV_Report.pdf")
