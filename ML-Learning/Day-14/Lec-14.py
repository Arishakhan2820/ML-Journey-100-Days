# ==========================================================
# Day 14: Framing & Planning Simulation Script (Python)
# ==========================================================

"""
This script simulates a simplified end-to-end framing workflow 
for a Churn Prediction problem (inspired by the Netflix case study).
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

print("==========================================")
print(" 1. SIMULATING USER CHURN DATASET (FRAMING STAGE)")
print("==========================================")

# Simulating user behavior features
np.random.seed(42)
n_users = 200

watch_hours = np.random.uniform(5, 50, n_users)       # Hours spent watching per month
failed_searches = np.random.randint(0, 10, n_users)     # Unfulfilled searches
abandoned_shows = np.random.randint(0, 5, n_users)      # Shows started and left

# Churn logic: Low watch hours + high failed searches -> likely to churn (1)
churn_probability = (25 - watch_hours * 0.4 + failed_searches * 1.5) > 10
churned = churn_probability.astype(int)

df = pd.DataFrame({
    'Watch_Hours': watch_hours,
    'Failed_Searches': failed_searches,
    'Abandoned_Shows': abandoned_shows,
    'Churned': churned
})

print(f"-> Dataset Generated Successfully! Total Users: {df.shape[0]}")
print(df.head(3))


print("\n==========================================")
print(" 2. PREPARING FEATURES (X) AND TARGET (y)")
print("==========================================")

X = df[['Watch_Hours', 'Failed_Searches', 'Abandoned_Shows']]
y = df['Churned']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"-> Training Samples: {X_train.shape[0]} | Testing Samples: {X_test.shape[0]}")


print("\n==========================================")
print(" 3. MODEL TRAINING & CHURN PREDICTION")
print("==========================================")

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"-> Churn Prediction Model Accuracy: {accuracy * 100:.2f}%")
print("==========================================")
