import nltk
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

# Prepare sample data
sentences = [
    'I love Python programming.',
    'I dislike writing code.',
    'Machine learning is fascinating.',
    'Natural language processing is challenging.'
]
labels = ['positive', 'negative', 'positive', 'negative']

# Tokenization and preprocessing
nltk.download('punkt')
corpus = [nltk.word_tokenize(sentence) for sentence in sentences]

# Convert corpus to feature vectors
vectorizer = CountVectorizer()
X = vectorizer.fit_transform([' '.join(sentence) for sentence in corpus])

# Apply TF-IDF transformation
transformer = TfidfTransformer()
X = transformer.fit_transform(X)

# Train a Linear SVM classifier on the entire dataset
classifier = LinearSVC()
classifier.fit(X, labels)

# Make predictions on the entire dataset
y_pred = classifier.predict(X)

# Calculate accuracy on the entire dataset
accuracy = accuracy_score(labels, y_pred)
print('Accuracy on entire dataset:', accuracy)

# Print predictions and actual labels to check model output
print('Predictions:', y_pred)
print('Actual Labels:', labels)

# Perform cross-validation to get a more robust measure of accuracy
scores = cross_val_score(classifier, X, labels, cv=2)
print('Cross-Validation Scores:', scores)
print('Mean Cross-Validation Accuracy:', scores.mean())
