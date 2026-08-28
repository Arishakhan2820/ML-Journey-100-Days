# ==========================================
# Day 06: Instance-Based vs Model-Based Learning
# ==========================================

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

print("==========================================")
print(" 1. INSTANCE-BASED LEARNING (KNN EXAMPLE)")
print("==========================================")

# 1. Instance-based models memorize the data instead of finding a formula.
# Let's define historical training features (IQ, CGPA) and labels (Placement: 0 or 1)
X_train = np.array([[7.0, 3.0], [8.5, 3.5], [6.0, 2.0], [9.0, 3.8]])
y_train = np.array([0, 1, 0, 1])

# Initialize KNN Classifier (Instance-based / Lazy learner)
knn_model = KNeighborsClassifier(n_neighbors=3)

# Training just means storing the data points in memory
knn_model.fit(X_train, y_train)
print("-> Instance-based model stored training data points successfully!")

# Predict for a new student query point
new_student = np.array([[8.0, 3.2]])
prediction = knn_model.predict(new_student)
print(f"-> Prediction for new student (Instance-Based): {'Placed' if prediction[0] == 1 else 'Not Placed'}\n")


print("==========================================")
print(" 2. MODEL-BASED LEARNING (LOGISTIC REGRESSION)")
print("==========================================")

# 2. Model-based algorithms learn a generalized mathematical rule/boundary.
# Initialize Logistic Regression (Model-based learner)
model_based = LogisticRegression()

# Training calculates the underlying parameters (coefficients and intercept)
model_based.fit(X_train, y_train)
print("-> Model-based algorithm learned the parameters and generalized the rule!")

# Once learned, the original data is no longer strictly required for predictions
predicted_result = model_based.predict(new_student)
print(f"-> Prediction for new student (Model-Based): {'Placed' if predicted_result[0] == 1 else 'Not Placed'}")
