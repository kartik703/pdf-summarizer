---
title: AI PDF Summarizer
emoji: 📄
colorFrom: indigo
colorTo: gray
sdk: streamlit
sdk_version: "1.28.0"
app_file: app.py
pinned: false
---

# 📄 AI PDF Summarizer with T5 & KeyBERT

[![GitHub Repo](https://img.shields.io/badge/GitHub-View%20Source-blue?logo=github)](https://github.com/kartik703/pdf-summarizer)

An intelligent, interactive web app that allows you to:

- 📄 Upload any PDF
- 🔍 Extract the text using `pdfplumber`
- 🧠 Summarize it using the T5 transformer model
- 🔑 Extract key concepts using KeyBERT
- 📅 Download the summary as a `.txt` file

Built with **Streamlit**, **Hugging Face Transformers**, and **KeyBERT**.  
Deployed on **Hugging Face Spaces**.

---

## 🚀 Live Demo

👉 [Launch on Hugging Face Spaces](https://huggingface.co/spaces/kartikG2000/pdf-summarizer)

---

## 🧠 Tech Stack

- `streamlit` – Interactive web app interface
- `transformers` – T5 model for abstractive summarization
- `pdfplumber` – Extract text from PDFs
- `keybert` – BERT-based keyword extraction
- `torch` – Model backend
- `sentencepiece` – Required tokenizer for T5
- `scikit-learn` & `nltk` – Support for keyword filtering

---

## 📦 How to Run Locally

```bash
# Clone the repo
git clone https://huggingface.co/spaces/kartikG2000/pdf-summarizer
cd pdf-summarizer

# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # For Mac/Linux
# venv\Scripts\activate    # For Windows

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

---

## 🖼️ App Preview

![App Screenshot](Screenshot.png)


---

## 🙌 Created By

**Kartik Goswami**  
📍 Data Science & AI Enthusiast  
🌐 [LinkedIn](https://www.linkedin.com/in/kartikgoswami2000) | [GitHub](https://github.com/kartik703)

---

## ⭐️ Show Some Love

If you found this project helpful, please consider:

- Giving it a ⭐ on [GitHub](https://github.com/kartik703/pdf-summarizer)
- Sharing it on LinkedIn to inspire others 🚀

