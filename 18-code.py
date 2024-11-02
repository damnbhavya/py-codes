# Import necessary libraries
import nltk
import spacy
from nltk.sentiment import SentimentIntensityAnalyzer
from pynlpl.formats import folia

# Download NLTK resources
nltk.download('punkt')
nltk.download('vader_lexicon')

# Sample sentence
sentence = "Natural Language Processing is awesome!"

# NLTK Tokenization
tokens = nltk.word_tokenize(sentence)
print("NLTK Tokenization:")
print(tokens)

# SpaCy Part-of-Speech Tagging
nlp = spacy.load('en_core_web_sm')
doc = nlp(sentence)
print("\nSpaCy Part-of-Speech Tagging:")
for token in doc:
    print(f"{token.text}: {token.pos_}")

# NLTK VADER Sentiment Analysis
sia = SentimentIntensityAnalyzer()
sentiment_score_vader = sia.polarity_scores(sentence)
print("\nNLTK VADER Sentiment Analysis Score:")
print(sentiment_score_vader)

# PyNLPl Example: Basic File Parsing (Example Feature)
# Note: PyNLPl is more commonly used for processing linguistic data formats.
# Here, we show how to read a FoLiA XML file for demonstration purposes.
# (Replace 'example.folia.xml' with a real file path if available)
try:
    doc_folia = folia.Document(file='example.folia.xml')
    print("\nPyNLPl Example: Parsed FoLiA Document")
    print(f"Title: {doc_folia.metadata['title'] if 'title' in doc_folia.metadata else 'N/A'}")
except FileNotFoundError:
    print("\nPyNLPl Example: No FoLiA document found for demonstration. Please provide a valid file.")

# Placeholder for any custom analysis or processing you want to add with PyNLPl.
