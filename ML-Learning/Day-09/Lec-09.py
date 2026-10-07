# ==========================================
# Day 09: MLDLC Pipeline Skeleton (Python)
# ==========================================

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

print("==========================================")
print(" MLDLC: SIMULATED END-TO-END PIPELINE")
print("==========================================")

# Step 1 & 2: Problem Framing & Data Loading
# Simulating raw dataset
df = pd.DataFrame({
    'Study_Hours': [2, 5, 3, 8, 1, 7],
    'Attendance': [50, 90, 60, 95, 40, 85],
    'Passed': [0, 1, 0, 1, 0, 1]
})
print("-> Step 1 & 2: Problem framed and data loaded.")

# Step 3 & 5: Data Preprocessing & Feature Selection
X = df[['Study_Hours', 'Attendance']] # Selected features
y = df['Passed']

# Step 6: Model Training & Evaluation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
print("-> Step 6: Model trained successfully.")

# Step 7: Model Deployment Prep (Saving model to a binary file)
model_filename = 'ml_model.pkl'
with open(model_filename, 'wb') as file:
    pickle.dump(model, file)

print(f"-> Step 7: Model saved as '{model_filename}' for API deployment!")
