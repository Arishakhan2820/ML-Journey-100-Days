# Day 25: Feature Scaling – Normalization
# MinMaxScaler, Mean Normalization, MaxAbsScaler, RobustScaler

"""
LEARNING GOALS
--------------
1. Understand why feature scaling is important.
2. Apply MinMaxScaler.
3. Apply Mean Normalization manually.
4. Apply MaxAbsScaler.
5. Apply RobustScaler.
6. Compare original and scaled data.
7. Learn how to avoid data leakage.

DATASET
-------
This script uses the Wine dataset provided by Scikit-learn.
It does not require a separate CSV file.

INSTALLATION
------------
Run this command in your terminal:

pip install pandas numpy matplotlib scikit-learn
"""

# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import (
    MinMaxScaler,
    MaxAbsScaler,
    RobustScaler,
    StandardScaler
)


# ============================================================
# 2. LOAD THE WINE DATASET
# ============================================================

wine = load_wine()

# Convert the dataset into a Pandas DataFrame
df = pd.DataFrame(
    wine.data,
    columns=wine.feature_names
)

# Add the target column
df["target"] = wine.target

print("\nFirst five rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())


# ============================================================
# 3. SELECT NUMERICAL FEATURES
# ============================================================

# We will use two numerical features for demonstration.
# Target is not included in feature scaling.

X = df[["alcohol", "malic_acid"]]

print("\nOriginal feature data:")
print(X.head())

print("\nOriginal feature statistics:")
print(X.describe())


# ============================================================
# 4. VISUALIZE ORIGINAL DATA
# ============================================================

plt.figure(figsize=(8, 5))

plt.scatter(
    X["alcohol"],
    X["malic_acid"],
    alpha=0.7
)

plt.xlabel("Alcohol")
plt.ylabel("Malic Acid")
plt.title("Original Wine Dataset Features")
plt.grid(True)

plt.show()


# ============================================================
# 5. MINMAX SCALING
# ============================================================

print("\n========== MINMAX SCALING ==========")

minmax_scaler = MinMaxScaler()

# Fit and transform the selected data for this demonstration
X_minmax = minmax_scaler.fit_transform(X)

# Convert the result back into a DataFrame
X_minmax = pd.DataFrame(
    X_minmax,
    columns=X.columns
)

print("\nMinMax scaled data:")
print(X_minmax.head())

print("\nMinimum values after MinMax Scaling:")
print(X_minmax.min())

print("\nMaximum values after MinMax Scaling:")
print(X_minmax.max())

# Both features should have minimum 0 and maximum 1.


# ============================================================
# 6. MEAN NORMALIZATION
# ============================================================

print("\n========== MEAN NORMALIZATION ==========")

# Formula:
# (Original Value - Mean) / (Maximum - Minimum)

X_mean = (X - X.mean()) / (X.max() - X.min())

print("\nMean normalized data:")
print(X_mean.head())

print("\nMean after Mean Normalization:")
print(X_mean.mean())

# The mean of each transformed feature should be approximately 0.


# ============================================================
# 7. MAXABS SCALING
# ============================================================

print("\n========== MAXABS SCALING ==========")

maxabs_scaler = MaxAbsScaler()

X_maxabs = maxabs_scaler.fit_transform(X)

X_maxabs = pd.DataFrame(
    X_maxabs,
    columns=X.columns
)

print("\nMaxAbs scaled data:")
print(X_maxabs.head())

print("\nMaximum absolute values after scaling:")
print(X_maxabs.abs().max())


# ============================================================
# 8. ROBUST SCALING
# ============================================================

print("\n========== ROBUST SCALING ==========")

robust_scaler = RobustScaler()

X_robust = robust_scaler.fit_transform(X)

X_robust = pd.DataFrame(
    X_robust,
    columns=X.columns
)

print("\nRobust scaled data:")
print(X_robust.head())

print("\nMedian after Robust Scaling:")
print(X_robust.median())

# RobustScaler uses the median and IQR.
# It does not remove outliers.


# ============================================================
# 9. STANDARDIZATION FOR COMPARISON
# ============================================================

print("\n========== STANDARDIZATION ==========")

standard_scaler = StandardScaler()

X_standard = standard_scaler.fit_transform(X)

X_standard = pd.DataFrame(
    X_standard,
    columns=X.columns
)

print("\nStandardized data:")
print(X_standard.head())

print("\nMean after Standardization:")
print(X_standard.mean())

print("\nStandard deviation after Standardization:")
print(X_standard.std())


# ============================================================
# 10. COMPARE ALL SCALING TECHNIQUES
# ============================================================

print("\n========== SCALING COMPARISON ==========")

print("\nOriginal Data:")
print(X.head())

print("\nMinMax Scaling:")
print(X_minmax.head())

print("\nMean Normalization:")
print(X_mean.head())

print("\nMaxAbs Scaling:")
print(X_maxabs.head())

print("\nRobust Scaling:")
print(X_robust.head())

print("\nStandardization:")
print(X_standard.head())


# ============================================================
# 11. VISUALIZE SCALING RESULTS
# ============================================================

# Compare the Alcohol feature before and after scaling.

scaling_results = {
    "Original": X["alcohol"],
    "MinMax": X_minmax["alcohol"],
    "Mean Normalization": X_mean["alcohol"],
    "MaxAbs": X_maxabs["alcohol"],
    "Robust": X_robust["alcohol"],
    "Standardization": X_standard["alcohol"]
}

plt.figure(figsize=(12, 6))

for label, values in scaling_results.items():
    plt.hist(
        values,
        bins=20,
        alpha=0.35,
        label=label
    )

plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Comparison of Feature Scaling Techniques")
plt.legend()
plt.grid(True)

plt.show()


# ============================================================
# 12. COMPARE SCATTER PLOTS
# ============================================================

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Original data
axes[0].scatter(
    X["alcohol"],
    X["malic_acid"],
    alpha=0.7
)

axes[0].set_title("Before Scaling")
axes[0].set_xlabel("Alcohol")
axes[0].set_ylabel("Malic Acid")
axes[0].grid(True)

# MinMax scaled data
axes[1].scatter(
    X_minmax["alcohol"],
    X_minmax["malic_acid"],
    alpha=0.7
)

axes[1].set_title("After MinMax Scaling")
axes[1].set_xlabel("Alcohol")
axes[1].set_ylabel("Malic Acid")
axes[1].grid(True)

plt.tight_layout()
plt.show()


# ============================================================
# 13. UNDERSTANDING OUTLIERS
# ============================================================

print("\n========== OUTLIER EXPERIMENT ==========")

# Create a small sample dataset containing an extreme value.

sample = pd.DataFrame({
    "Salary": [20000, 25000, 30000, 35000, 40000, 500000]
})

print("\nOriginal sample:")
print(sample)

# Apply MinMax Scaling
sample_minmax = MinMaxScaler().fit_transform(sample)

# Apply Robust Scaling
sample_robust = RobustScaler().fit_transform(sample)

print("\nMinMax scaled sample:")
print(pd.DataFrame(sample_minmax, columns=["Salary"]))

print("\nRobust scaled sample:")
print(pd.DataFrame(sample_robust, columns=["Salary"]))

# Notice how the extreme value affects MinMax Scaling.
# Robust Scaling uses median and IQR, so it is less affected.


# ============================================================
# 14. CORRECT TRAIN-TEST SCALING WORKFLOW
# ============================================================

print("\n========== TRAIN-TEST WORKFLOW ==========")

# Select all numerical input features.
# The target column is kept separate.

X_all = df.drop(columns=["target"])
y = df["target"]

# First split the dataset.
X_train, X_test, y_train, y_test = train_test_split(
    X_all,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create the scaler.
scaler = MinMaxScaler()

# Fit only on training data.
X_train_scaled = scaler.fit_transform(X_train)

# Transform test data using the same fitted scaler.
X_test_scaled = scaler.transform(X_test)

# Convert results back into DataFrames.
X_train_scaled = pd.DataFrame(
    X_train_scaled,
    columns=X_train.columns,
    index=X_train.index
)

X_test_scaled = pd.DataFrame(
    X_test_scaled,
    columns=X_test.columns,
    index=X_test.index
)

print("\nTraining data shape:")
print(X_train_scaled.shape)

print("\nTesting data shape:")
print(X_test_scaled.shape)

print("\nScaled training data:")
print(X_train_scaled.head())

print("\nScaled testing data:")
print(X_test_scaled.head())

print("\nTraining minimum values:")
print(X_train_scaled.min())

print("\nTraining maximum values:")
print(X_train_scaled.max())

# Important:
# Some test values can be below 0 or above 1 if they fall
# outside the training data's minimum and maximum values.
# This is normal because the scaler was fitted only on training data.


# ============================================================
# 15. FINAL REVISION
# ============================================================

print("\n========== FINAL REVISION ==========")

print("""
1. MinMaxScaler:
   Uses minimum and maximum values.
   Default output range is 0 to 1.

2. Mean Normalization:
   Subtracts mean and divides by feature range.
   Centers the feature around zero.

3. MaxAbsScaler:
   Divides by maximum absolute value.
   Preserves zero values and is useful for sparse data.

4. RobustScaler:
   Uses median and IQR.
   Less affected by outliers.

5. StandardScaler:
   Uses mean and standard deviation.
   Produces mean approximately 0 and standard deviation 1.

IMPORTANT:
Always split your dataset before fitting a scaler.
Fit on training data and transform both training and test data.
""")

print("Day 25 practice completed!")


# ============================================================
# 16. PRACTICE TASKS
# ============================================================

"""
Try these tasks yourself:

1. Apply MinMaxScaler to a dataset of your choice.
2. Perform Mean Normalization manually.
3. Apply MaxAbsScaler to data containing zero values.
4. Apply RobustScaler to data containing an extreme outlier.
5. Compare the results of all four techniques.
6. Try StandardScaler and compare its output.
7. Use a different numerical dataset.
8. Split the dataset before scaling.
9. Check whether scaling improves a KNN model.
10. Compare model performance before and after scaling.

Remember:
Different datasets and algorithms may need different scaling methods.
Experiment and compare results.
"""
