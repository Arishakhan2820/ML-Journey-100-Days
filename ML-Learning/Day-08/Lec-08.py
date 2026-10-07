# ==========================================
# Day 08: Real-Life ML Concepts Demo (Python)
# ==========================================

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

print("==========================================")
print(" 1. RETAIL: ASSOCIATION RULE MINING (SIMULATED)")
print("==========================================")

# Simple Market Basket Analysis concept
transactions = [
    ['Milk', 'Bread', 'Butter'],
    ['Beer', 'Diaper', 'Milk'],
    ['Milk', 'Bread', 'Diaper', 'Beer'],
    ['Bread', 'Butter']
]
print("-> Sample Customer Transactions processed for product placement rules.")


print("\n==========================================")
print(" 2. SOCIAL MEDIA: SIMPLE SENTIMENT ANALYSIS")
print("==========================================")

# Simulating Sentiment Analysis (CampusX Twitter/Review Example)
reviews = [
    "This movie was brilliant and amazing!",
    "Terrible waste of time and money, very disappointed.",
    "Absolute masterpiece, loved every second.",
    "Worst experience ever, horrible acting."
]
labels = ["Positive", "Negative", "Positive", "Negative"]

# Vectorizing text data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(reviews)

# Training a basic classifier
model = MultinomialNB()
model.fit(X, labels)

# Testing on a new review
new_review = ["The plot was fantastic and stunning!"]
new_vector = vectorizer.transform(new_review)
prediction = model.predict(new_vector)

print(f"-> New Review: '{new_review[0]}'")
print(f"-> Predicted Sentiment: {prediction[0]}")
