from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Predefined skills list (you can expand)
PREDEFINED_SKILLS = [
    "python", "java", "c#", "javascript", "react", "node",
    "sql", "excel", "aws", "docker", "linux", "git",
    "html", "css", "communication", "project management",
    "team leadership", "agile", "problem solving", "creativity"
]

def calculate_match(resume_text, job_description):
    """Return CV vs Job Description similarity percentage"""
    texts = [resume_text, job_description]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf = vectorizer.fit_transform(texts)
    similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])
    return round(similarity[0][0] * 100, 2)

def extract_skills_from_text(text):
    """Detect skills from predefined list"""
    text_lower = text.lower()
    detected = [skill.title() for skill in PREDEFINED_SKILLS if skill in text_lower]
    return detected

def generate_feedback(resume_text, job_description):
    """Generate detailed, premium-quality suggestions"""
    resume_words = set(resume_text.lower().split()) - stop_words
    job_words = set(job_description.lower().split()) - stop_words
    missing_keywords = sorted(list(job_words - resume_words))[:20]

    skills_found = extract_skills_from_text(resume_text)

    feedback = []

    # Skills
    if missing_keywords:
        feedback.append("✅ Add or emphasize these keywords/skills to match the job description:\n- " + "\n- ".join([kw.title() for kw in missing_keywords]))
    
    # Experience
    if "experience" not in resume_text.lower() or len(resume_text.split()) < 200:
        feedback.append("💼 Expand your Work Experience section with clear roles, responsibilities, and measurable achievements (e.g., improved X by 20%).")

    # Education
    if "education" not in resume_text.lower() and "degree" not in resume_text.lower():
        feedback.append("🎓 Include your Education details: degree, institution, and graduation year.")

    # Projects / Impact
    feedback.append("🚀 Highlight impactful projects, contributions, or measurable outcomes to demonstrate your value to employers.")

    # Additional readability / clarity suggestions
    feedback.append("✍️ Ensure your CV uses concise bullet points and action verbs for clarity and impact.")

    return feedback, skills_found
