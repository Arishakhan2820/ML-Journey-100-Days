# Day 24 – Feature Scaling: Standardization
# Python Practice File

# ==================================================
# 1. IMPORT LIBRARIES
# ==================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# ==================================================
# 2. LOAD DATASET
# ==================================================

# Download Social_Network_Ads.csv.
# Keep it in the same folder as this Python file.

df = pd.read_csv("Social_Network_Ads.csv")

# Make column names lowercase.
df.columns = df.columns.str.strip().str.lower()

print("First Five Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())


# ==================================================
# 3. SELECT INPUT AND TARGET FEATURES
# ==================================================

# Input features:
# Age and EstimatedSalary

# Target feature:
# Purchased

X = df[["age", "estimatedsalary"]]

y = df["purchased"]

print("\nInput Features:")
print(X.head())

print("\nTarget Feature:")
print(y.head())


# ==================================================
# 4. UNDERSTAND ORIGINAL DATA
# ==================================================

print("\nOriginal Data Description:")
print(X.describe())

print("\nOriginal Mean:")
print(X.mean())

print("\nOriginal Standard Deviation:")
print(X.std())


# Notice:
# Age has smaller values.
# EstimatedSalary has much larger values.
# Their different scales can affect some ML algorithms.


# ==================================================
# 5. VISUALIZE ORIGINAL DATA
# ==================================================

plt.figure(figsize=(8, 5))

plt.scatter(
    X["age"],
    X["estimatedsalary"],
    alpha=0.6
)

plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.title("Before Standardization")

plt.show()


# ==================================================
# 6. TRAIN-TEST SPLIT
# ==================================================

# First split the dataset.
# Fit the scaler only on training data.

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Data Shape:")
print(X_train.shape)

print("\nTesting Data Shape:")
print(X_test.shape)


# ==================================================
# 7. CREATE STANDARD SCALER
# ==================================================

scaler = StandardScaler()


# ==================================================
# 8. FIT AND TRANSFORM TRAINING DATA
# ==================================================

# fit_transform():
# 1. Learns the mean and standard deviation.
# 2. Transforms the training data.

X_train_scaled = scaler.fit_transform(X_train)

print("\nScaled Training Data:")
print(X_train_scaled[:5])


# ==================================================
# 9. TRANSFORM TESTING DATA
# ==================================================

# Use the same fitted scaler.
# Do not fit again on testing data.

X_test_scaled = scaler.transform(X_test)

print("\nScaled Testing Data:")
print(X_test_scaled[:5])


# ==================================================
# 10. CONVERT NUMPY ARRAY TO DATAFRAME
# ==================================================

X_train_scaled_df = pd.DataFrame(
    X_train_scaled,
    columns=X_train.columns,
    index=X_train.index
)

X_test_scaled_df = pd.DataFrame(
    X_test_scaled,
    columns=X_test.columns,
    index=X_test.index
)

print("\nScaled Training DataFrame:")
print(X_train_scaled_df.head())


# ==================================================
# 11. CHECK MEAN AND STANDARD DEVIATION
# ==================================================

print("\nMean After Standardization:")
print(X_train_scaled_df.mean())

print("\nStandard Deviation After Standardization:")
print(X_train_scaled_df.std())

# Expected:
# Mean should be approximately 0.
# Standard deviation should be approximately 1.
#
# Note:
# StandardScaler uses population standard deviation.
# Pandas std() uses sample standard deviation by default.
# Therefore, the result may be slightly different from 1.


# ==================================================
# 12. VISUALIZE DATA AFTER STANDARDIZATION
# ==================================================

plt.figure(figsize=(8, 5))

plt.scatter(
    X_train_scaled_df["age"],
    X_train_scaled_df["estimatedsalary"],
    alpha=0.6
)

plt.xlabel("Standardized Age")
plt.ylabel("Standardized Salary")
plt.title("After Standardization")

plt.show()


# ==================================================
# 13. COMPARE DISTRIBUTIONS BEFORE AND AFTER
# ==================================================

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Original Age
sns.histplot(
    X_train["age"],
    kde=True,
    ax=axes[0, 0]
)

axes[0, 0].set_title("Original Age")

# Standardized Age
sns.histplot(
    X_train_scaled_df["age"],
    kde=True,
    ax=axes[0, 1]
)

axes[0, 1].set_title("Standardized Age")

# Original Salary
sns.histplot(
    X_train["estimatedsalary"],
    kde=True,
    ax=axes[1, 0]
)

axes[1, 0].set_title("Original Salary")

# Standardized Salary
sns.histplot(
    X_train_scaled_df["estimatedsalary"],
    kde=True,
    ax=axes[1, 1]
)

axes[1, 1].set_title("Standardized Salary")

plt.tight_layout()
plt.show()

# Standardization changes the center and scale.
# It generally preserves the distribution shape.


# ==================================================
# 14. KNN WITHOUT STANDARDIZATION
# ==================================================

knn_original = KNeighborsClassifier(n_neighbors=5)

knn_original.fit(X_train, y_train)

y_pred_original = knn_original.predict(X_test)

accuracy_original = accuracy_score(
    y_test,
    y_pred_original
)

print("\nKNN Accuracy Without Scaling:")
print(accuracy_original)


# ==================================================
# 15. KNN WITH STANDARDIZATION
# ==================================================

knn_scaled = KNeighborsClassifier(n_neighbors=5)

knn_scaled.fit(X_train_scaled, y_train)

y_pred_scaled = knn_scaled.predict(X_test_scaled)

accuracy_scaled = accuracy_score(
    y_test,
    y_pred_scaled
)

print("\nKNN Accuracy With Scaling:")
print(accuracy_scaled)


# ==================================================
# 16. COMPARE KNN ACCURACY
# ==================================================

print("\nKNN Accuracy Comparison")

print(
    "Without Scaling:",
    round(accuracy_original * 100, 2),
    "%"
)

print(
    "With Standardization:",
    round(accuracy_scaled * 100, 2),
    "%"
)

# Scaling may improve KNN performance.
# Results depend on the dataset and split.


# ==================================================
# 17. LOGISTIC REGRESSION WITHOUT SCALING
# ==================================================

logistic_original = LogisticRegression(max_iter=1000)

logistic_original.fit(X_train, y_train)

logistic_pred_original = logistic_original.predict(X_test)

logistic_accuracy_original = accuracy_score(
    y_test,
    logistic_pred_original
)

print("\nLogistic Regression Without Scaling:")
print(logistic_accuracy_original)


# ==================================================
# 18. LOGISTIC REGRESSION WITH SCALING
# ==================================================

logistic_scaled = LogisticRegression(max_iter=1000)

logistic_scaled.fit(X_train_scaled, y_train)

logistic_pred_scaled = logistic_scaled.predict(X_test_scaled)

logistic_accuracy_scaled = accuracy_score(
    y_test,
    logistic_pred_scaled
)

print("\nLogistic Regression With Scaling:")
print(logistic_accuracy_scaled)


# ==================================================
# 19. COMPARE LOGISTIC REGRESSION ACCURACY
# ==================================================

print("\nLogistic Regression Comparison")

print(
    "Without Scaling:",
    round(logistic_accuracy_original * 100, 2),
    "%"
)

print(
    "With Standardization:",
    round(logistic_accuracy_scaled * 100, 2),
    "%"
)


# ==================================================
# 20. UNDERSTANDING OUTLIERS
# ==================================================

# Create a small salary dataset.

salary_data = pd.DataFrame({
    "salary": [20000, 25000, 30000, 35000, 40000]
})

# Add an extreme value.

salary_data_outlier = pd.DataFrame({
    "salary": [20000, 25000, 30000, 35000, 40000, 500000]
})

print("\nSalary Data Without Outlier:")
print(salary_data)

print("\nSalary Data With Outlier:")
print(salary_data_outlier)


# ==================================================
# 21. APPLY STANDARD SCALER TO OUTLIER DATA
# ==================================================

scaler1 = StandardScaler()

normal_scaled = scaler1.fit_transform(salary_data)

scaler2 = StandardScaler()

outlier_scaled = scaler2.fit_transform(salary_data_outlier)

print("\nStandardized Data Without Outlier:")
print(normal_scaled.flatten())

print("\nStandardized Data With Outlier:")
print(outlier_scaled.flatten())

# StandardScaler uses mean and standard deviation.
# Extreme values can affect both statistics.
# StandardScaler does not remove outliers.


# ==================================================
# 22. APPLY ROBUST SCALER
# ==================================================

# RobustScaler uses median and interquartile range.
# It is less sensitive to extreme values.

robust_scaler = RobustScaler()

robust_scaled = robust_scaler.fit_transform(
    salary_data_outlier
)

print("\nData After Robust Scaling:")
print(robust_scaled.flatten())


# ==================================================
# 23. FINAL SUMMARY
# ==================================================

print("\nFeature Scaling Practice Completed!")

print("\nTopics Covered:")

print("1. Feature Scaling")
print("2. Standardization")
print("3. Z-score Formula")
print("4. StandardScaler")
print("5. Mean Centering")
print("6. Standard Deviation")
print("7. fit() and transform()")
print("8. fit_transform()")
print("9. Train-Test Split")
print("10. Data Leakage Prevention")
print("11. Distribution Visualization")
print("12. KNN Comparison")
print("13. Logistic Regression Comparison")
print("14. Outlier Impact")
print("15. RobustScaler")


# ==================================================
# INSTALL REQUIRED LIBRARIES
# ==================================================

# Run this command in your terminal:
#
# pip install pandas numpy matplotlib seaborn scikit-learn


# ==================================================
# DATASET REQUIREMENT
# ==================================================

# Download:
# Social_Network_Ads.csv
#
# Keep the CSV file in the same folder as this script.
#
# Required columns:
# Age
# EstimatedSalary
# Purchased
#
# User ID and Gender are not used in this example.

File name: Day_24_Feature_Scaling_Standardization.py

Dataset: Social_Network_Ads.csv — Python file ke same folder mein rakhna.
