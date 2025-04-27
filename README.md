# 📝 Text Summarizer

A web application for **extractive text summarization** using **BERT embeddings**.  
Built with **Flask**, **HTML/CSS/JS**, and powered by **bert-extractive-summarizer** for accurate, context-aware sentence extraction.  
It also supports uploading **PDF files** and customizing the **length** of the summary (Short, Medium, Long)!

---

## 🚀 Features
- Summarize **raw text** or **uploaded PDF** files.
- Customize summary length:
  - **Short** (20% of original content)
  - **Medium** (40% of original content)
  - **Long** (60% of original content)
- Fast and accurate extraction using **BERT-based summarizer**.
- Simple and clean **responsive UI**.

---


## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/dipeshlohchab/text-summarizer.git
cd text-summarizer
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # Mac/Linux
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 4. Run the Flask App
```bash
python app.py
```

The app will be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

---

## ✨ How It Works

- The input text is processed using a **BERT-based summarizer**.
- Sentences are ranked contextually and extracted based on the selected **summary length**.
- For PDFs, the text is extracted automatically before summarization.

---

## 📦 Dependencies
- Flask
- bert-extractive-summarizer
- transformers
- spaCy
- scikit-learn
- nltk

---

## 🙏 Acknowledgements
- [bert-extractive-summarizer](https://github.com/dmmiller612/bert-extractive-summarizer)
- [HuggingFace Transformers](https://huggingface.co/transformers/)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

