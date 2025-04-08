import streamlit as st
from pdf_utils import extract_text_from_pdf
from summarizer import summarize_text
from keywords import extract_keywords

st.set_page_config(page_title="AI PDF Summarizer", layout="centered")
st.title("📄 AI PDF Summarizer with T5 & Keyword Extraction")

# Upload PDF file
pdf_file = st.file_uploader("📤 Upload a PDF", type=["pdf"])

if pdf_file:
    # Extract text
    with st.spinner("🔍 Extracting text from PDF..."):
        extracted_text = extract_text_from_pdf(pdf_file)

    # Preview the extracted text
    st.subheader("📜 Extracted Text (Preview)")
    st.text(extracted_text[:1000] + "...\n\n[Preview truncated]")

    # Summarize the text
    st.subheader("🧠 Summary")
    with st.spinner("✍️ Generating summary using T5..."):
        summary = summarize_text(extracted_text)
    st.success(summary)

    # Extract keywords
    st.subheader("🔑 Keywords")
    with st.spinner("📌 Extracting top keywords..."):
        keywords = extract_keywords(extracted_text)
    st.write(", ".join(keywords))

    # Download button
    st.download_button(
        label="💾 Download Summary as .txt",
        data=summary,
        file_name="summary.txt",
        mime="text/plain"
    )
else:
    st.info("👆 Upload a PDF to get started.")
