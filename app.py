import os
import fitz  # PyMuPDF
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from summarize import extractive_summary

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get('text')
    length = data.get('length', 'medium')
    summary = extractive_summary(text, length)
    return jsonify({'summary': summary})

@app.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    if 'pdf' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['pdf']
    length = request.form.get('length', 'medium')

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type. Only PDF files are allowed.'}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    text = ""
    try:
        with fitz.open(filepath) as doc:
            for page in doc:
                text += page.get_text()

        if not text:
            return jsonify({'error': 'No text found in PDF'}), 400

        summary = extractive_summary(text, length)
        return jsonify({'summary': summary})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
