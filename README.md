> 🔀 This is the `bert-upgrade` branch — upgraded to AI-based semantic similarity using Sentence-BERT.


# 🧠 Resume–Job Description Matcher (BERT Version)

An AI-powered tool that evaluates how well a resume matches a job description — using state-of-the-art **BERT embeddings** for deep semantic comparison.

Built with `Flask`, `sentence-transformers`, and classical NLP to simulate how real-world ATS systems analyze job relevance.

> ✅ This is the `bert-upgrade` branch. It uses Sentence-BERT (`all-MiniLM-L6-v2`) for context-aware matching, with stopword filtering for accurate keyword overlap.
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

| Layer                 | Tools Used                                |
| --------------------- | ----------------------------------------- |
| **Backend**           | Python, Flask                             |
| **NLP Engine**        | Sentence-BERT (MiniLM), Cosine Similarity |
| **PDF Parsing**       | pdfminer.six                              |
| **Keyword Filtering** | nltk (stopwords)                          |
| **Testing**           | Postman                                   |
| **Versioning**        | Git, GitHub (`bert-upgrade` branch)       |

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
```
resume-jd-matcher/
├── app.py # Flask backend
├── utils/
│ └── matcher.py # TF-IDF + similarity logic
├── requirements.txt # Dependencies
├── .gitignore
└── README.md # This file
```

## 🧠 Future Enhancements

- 🎯 **Score Explanation**  
  Show why a resume got a high/low score — using heatmaps or keyword relevance.

- 🏷️ **Match Labeling**  
  Add match labels like `Low`, `Moderate`, `Strong`, `Excellent` based on score range.

- 🧠 **Chunk-Level Semantic Matching**  
  Break resume and JD into sections (skills, experience, bullet points) and compare in pairs for better accuracy.

- 🌐 **Frontend Upload Interface**  
  Build a web UI to let users upload resumes and view scores in real time (React, HTML, or Streamlit).

- 📤 **PDF Report Export**  
  Generate downloadable match reports with scores, keywords, and improvement tips.

- ☁️ **Deployment**  
  Host the app on Render, Hugging Face Spaces, or Streamlit Cloud for public use.

- 📈 **Keyword Frequency Heatmaps**  
  Highlight high-impact keywords in resume vs. JD.

- 🔍 **Skill Gap Insights**  
  Recommend what’s missing in the resume to match a specific JD better (based on semantic distance).

- 🗃️ **Multiple JD Comparison**  
  Let users upload one resume and match it to several job descriptions.

- 🧪 **BERT Model Selector**  
  Add option to switch between BERT models like `MiniLM`, `MPNet`, `RoBERTa` for experimentation.

## 👨‍💻 Author
Asunu Jakha
📍 Dimapur, Nagaland
🔗 LinkedIn | (https://www.linkedin.com/in/asunu-jakha-3995a3258?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)

## 💡 Why This Matters
This project simulates how modern Applicant Tracking Systems (ATS) work — giving you insight into what companies look for and how to tailor your resume to match real job descriptions.

⭐ If you found this project useful or insightful, feel free to star it on GitHub!