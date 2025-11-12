from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match(resume_text, job_description):
    texts = [resume_text, job_description]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf = vectorizer.fit_transform(texts)
    similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])
    return round(similarity[0][0] * 100, 2)
