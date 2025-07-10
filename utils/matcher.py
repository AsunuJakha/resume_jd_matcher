import io
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pdfminer.high_level import extract_text

def clean_text(text):
    # Remove punctuation, numbers, and lowercase everything
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower()

def extract_resume_text(pdf_file):
    # Read the binary content from Flask's FileStorage object
    file_stream = pdf_file.stream  # Get the file-like object
    text = extract_text(file_stream)  # pdfminer can read from this
    return clean_text(text)


def compute_match_score(resume_file, job_description):
    # Extract text from resume PDF
    resume_text = extract_resume_text(resume_file)

    # Clean JD too
    job_description = clean_text(job_description)

    # Use TF-IDF to vectorize both
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_description])

    # Calculate cosine similarity
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    # Convert to percentage
    match_score = round(similarity * 100, 2)

    # Optional: Find matched keywords (overlap in top words)
    resume_keywords = set(resume_text.split())
    jd_keywords = set(job_description.split())
    matched_keywords = list(resume_keywords.intersection(jd_keywords))

    return match_score, matched_keywords
