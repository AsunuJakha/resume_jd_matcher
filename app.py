from flask import Flask, request, jsonify
from utils.matcher import compute_match_score

app = Flask(__name__)

@app.route('/match', methods=['POST'])
def match_resume():
    resume_file = request.files.get('resume')
    job_description = request.form.get('jd')

    if not resume_file and not job_description:
        return jsonify({'error': 'Missing both resume and job description'}), 400
    elif not resume_file:
        return jsonify({'error': 'Missing resume file'}), 400
    elif not job_description:
        return jsonify({'error': 'Missing job description'}), 400

    try:
        score, matched_keywords = compute_match_score(resume_file, job_description)
        return jsonify({'match_score': score, 'matched_keywords': matched_keywords})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
