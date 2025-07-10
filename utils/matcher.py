from sentence_transformers import SentenceTransformer, util
from pdfminer.high_level import extract_text
from nltk.corpus import stopwords
import nltk
import re

# Download stopwords (only needed the first time)
nltk.download('stopwords')

# Load BERT model once
model = SentenceTransformer('all-MiniLM-L6-v2')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower()

def extract_resume_text(pdf_file):
    # Read text from uploaded PDF file
    text = extract_text(pdf_file.stream)
    return clean_text(text)

def compute_match_score(resume_file, job_description):
    # Extract and clean text
    resume_text = extract_resume_text(resume_file)
    job_description = clean_text(job_description)

    # Generate sentence embeddings using BERT
    embeddings = model.encode([resume_text, job_description], convert_to_tensor=True)

    # Compute cosine similarity between the resume and JD
    similarity_score = util.pytorch_cos_sim(embeddings[0], embeddings[1]).item()
    match_score = round(similarity_score * 100, 2)

    # Extract meaningful overlapping keywords (exclude stopwords)
    resume_words = set(word for word in resume_text.split() if word not in stop_words)
    jd_words = set(word for word in job_description.split() if word not in stop_words)
    matched_keywords = sorted(list(resume_words.intersection(jd_words)))

    return match_score, matched_keywords
