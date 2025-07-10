# 🧠 Resume–Job Description Matcher

An AI-inspired tool that evaluates how well a resume matches a job description. Built using Python, Flask, and classical Natural Language Processing (NLP) techniques like TF-IDF and cosine similarity.

> ✅ Built for placement prep, resume optimization, and real-world HR tech use cases.

---

## 🚀 Features

- 📄 Upload a resume (PDF format)
- 📋 Paste a job description
- 🧠 NLP-based text analysis (TF-IDF + cosine similarity)
- 📊 Match score (0–100%) showing how relevant the resume is to the JD
- 🧾 Shows overlapping keywords between resume and JD
- ⚙️ Ready for future upgrades: BERT, frontend UI, deployment

---

## 🛠 Tech Stack

| Layer         | Tools Used                    |
|---------------|-------------------------------|
| **Backend**   | Python, Flask                 |
| **NLP Engine**| Scikit-learn, TF-IDF, Cosine Similarity |
| **PDF Parsing**| pdfminer.six                 |
| **Testing**   | Postman (for file+text API testing) |
| **Versioning**| Git, GitHub                   |

---

## 🔍 How It Works

1. User uploads a resume in PDF format
2. Job description is pasted as text
3. Text is cleaned and vectorized using TF-IDF
4. Cosine similarity is calculated between vectors
5. Returns:
   - 🎯 Match score (as percentage)
   - 🧩 List of matched keywords

---

## 📷 API Demo (via Postman)

**Endpoint:**
POST /match



**Form-Data Parameters:**
- `resume`: File (PDF)
- `jd`: Text (job description)

**Example Response:**
```json
{
  "match_score": 82.45,
  "matched_keywords": ["python", "flask", "automation", "developer"]
}
```
## 📦 Folder Structure
resume-jd-matcher/
├── app.py # Flask backend
├── utils/
│ └── matcher.py # TF-IDF + similarity logic
├── requirements.txt # Dependencies
├── .gitignore
└── README.md # This file

🧠 Future Enhancements
🤖 Upgrade to BERT / Sentence Transformers for semantic AI

🌐 Add frontend upload form (React or plain HTML)

☁️ Deploy to Render / Hugging Face Spaces

📊 Add keyword analysis + optimization feedback

📁 Add exportable reports (PDF / email)

👨‍💻 Author
Asunu Jakha
📍 Dimapur, Nagaland
🔗 LinkedIn | 🌐 asunuofficial.com

💡 Why This Matters
This project simulates how modern Applicant Tracking Systems (ATS) work — giving you insight into what companies look for and how to tailor your resume to match real job descriptions.

⭐ If you found this project useful or insightful, feel free to star it on GitHub!