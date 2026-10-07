# ==========================================
# Day 07: Addressing Basic ML Challenges (Demo)
# ==========================================

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

print("==========================================")
print(" 1. HANDLING POOR DATA & MISSING VALUES")
print("==========================================")

# Simulating a messy dataset with missing values (Challenge #4)
data = {
    'IQ': [100, 120, np.nan, 110, 130],
    'CGPA': [3.0, 3.5, 2.8, np.nan, 3.9],
    'Placed': [0, 1, 0, 0, 1]
}
df = pd.DataFrame(data)
print("-> Original Messy Data:")
print(df)

# Cleaning: Fill missing values with the median (Data Cleaning step)
df['IQ'].fillna(df['IQ'].median(), inplace=True)
df['CGPA'].fillna(df['CGPA'].median(), inplace=True)
print("\n-> Cleaned Data (Missing values handled):")
print(df)


print("\n==========================================")
print(" 2. DROPPING IRRELEVANT FEATURES")
print("==========================================")

# Simulating an irrelevant feature like 'City' (Challenge #5)
df['City'] = ['Karachi', 'Lahore', 'Karachi', 'Islamabad', 'Lahore']

# Feature Selection: Drop 'City' because it adds no predictive value to placement
X = df[['IQ', 'CGPA']] # Keeping only relevant features
y = df['Placed']

print("-> Features selected for training (Irrelevant 'City' dropped):")
print(X.head())


print("\n==========================================")
print(" 3. TRAIN-TEST SPLIT TO CATCH OVERFITTING")
print("==========================================")

# Splitting data to test generalization on unseen data (Challenges #6 & #7)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f"-> Model trained successfully! Ready for software integration.")
