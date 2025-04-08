from keybert import KeyBERT
from nltk.corpus import stopwords
import nltk

# Ensure stopwords are downloaded
nltk.download("stopwords", quiet=True)

# Load the KeyBERT model once
kw_model = KeyBERT()

def extract_keywords(text, num_keywords=5):
    stop_words = stopwords.words("english")
    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        stop_words=stop_words,
        use_maxsum=True,
        top_n=num_keywords
    )
    return [kw for kw, _ in keywords]
