# ==========================================================
# Day 13: End-to-End Machine Learning Pipeline Practice Script
# ==========================================================

import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

print("=" * 60)
print(" 1. CREATING MOCK DATASET (STUDENT PLACEMENT)")
print("=" * 60)

# Simulating a dataset with CGPA, IQ, and Placement status (0 or 1)
np.random.seed(42)
n_samples = 150

cgpa = np.random.uniform(5.0, 9.5, n_samples)
iq = np.random.uniform(80, 140, n_samples)
# Simple logic for placement rule based on features + some noise
placement = ((cgpa * 10 + iq * 0.2) > 105).astype(int)

df = pd.DataFrame({
    'Unnecessary_Col': ['ID_' + str(i) for i in range(n_samples)], # Irrelevant feature
    'CGPA': cgpa,
    'IQ': iq,
    'Placed': placement
})

print(f"-> Original Dataset Shape: {df.shape}")
print(df.head(3))


print("\n" + "=" * 60)
print(" 2. DATA PREPROCESSING (DROPPING UNNECESSARY FEATURES)")
print("=" * 60)

# Drop the irrelevant column
df_cleaned = df.drop(columns=['Unnecessary_Col'])
print("-> Irrelevant column 'Unnecessary_Col' dropped successfully!")


print("\n" + "=" * 60)
print(" 3. EXTRACTING FEATURES (X) AND TARGET (y)")
print("=" * 60)

X = df_cleaned[['CGPA', 'IQ']]  # Input features
y = df_cleaned['Placed']        # Target output label

print(f"-> Features Shape (X): {X.shape}")
print(f"-> Target Shape (y)  : {y.shape}")


print("\n" + "=" * 60)
print(" 4. TRAIN-TEST SPLIT")
print("=" * 60)

# Splitting data: 90% for training, 10% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

print(f"-> Training Set Rows : {X_train.shape[0]}")
print(f"-> Testing Set Rows  : {X_test.shape[0]}")


print("\n" + "=" * 60)
print(" 5. FEATURE SCALING (STANDARDIZATION)")
print("=" * 60)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("-> Features scaled successfully using StandardScaler (-1 to 1 range approx).")


print("\n" + "=" * 60)
print(" 6. MODEL TRAINING (LOGISTIC REGRESSION)")
print("=" * 60)

model = LogisticRegression()
model.fit(X_train_scaled, y_train)

print("-> Logistic Regression model trained successfully on training data!")


print("\n" + "=" * 60)
print(" 7. MODEL EVALUATION")
print("=" * 60)

y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

print(f"-> Model Predictions on Test Set : {y_pred}")
print(f"-> Actual Test Labels            : {y_test.values}")
print(f"-> Model Accuracy Score          : {accuracy * 100:.2f}%")


print("\n" + "=" * 60)
print(" 8. EXPORTING MODEL & SCALER USING PICKLE")
print("=" * 60)

# Saving both the trained model and the scaler for production use
with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('scaler.pkl', 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)

print("-> Success! 'model.pkl' and 'scaler.pkl' files saved locally for deployment.")
print("=" * 60)
