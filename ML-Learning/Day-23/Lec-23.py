# Day 23 – Feature Engineering (Python Practice)

# --------------------------------------------------
# 1. IMPORT LIBRARIES
# --------------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer


# --------------------------------------------------
# 2. LOAD DATASET
# --------------------------------------------------

# Load the Titanic dataset from Seaborn.
# An internet connection may be needed the first time.

df = sns.load_dataset("titanic")

print("First five rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nDataset information:")
df.info()


# --------------------------------------------------
# 3. MISSING VALUE CHECK
# --------------------------------------------------

print("\nMissing values:")
print(df.isnull().sum())

# Create a copy so the original dataset stays unchanged.
data = df.copy()

# Fill missing Age values using the median.
data["age"] = data["age"].fillna(data["age"].median())

# Fill missing Embarked values using the mode.
data["embarked"] = data["embarked"].fillna(
    data["embarked"].mode()[0]
)

print("\nMissing values after basic imputation:")
print(data[["age", "embarked"]].isnull().sum())


# --------------------------------------------------
# 4. HANDLING CATEGORICAL VALUES
# --------------------------------------------------

# One-Hot Encoding converts categories into numerical columns.

encoded_sex = pd.get_dummies(
    data["sex"],
    prefix="sex",
    dtype=int
)

print("\nOne-Hot Encoded Sex:")
print(encoded_sex.head())

# Add the encoded columns to the dataset.
data = pd.concat([data, encoded_sex], axis=1)


# --------------------------------------------------
# 5. BINNING
# --------------------------------------------------

# Convert Age into different groups.

age_bins = [0, 12, 19, 45, 100]

age_labels = [
    "Child",
    "Teenager",
    "Adult",
    "Senior"
]

data["Age_Group"] = pd.cut(
    data["age"],
    bins=age_bins,
    labels=age_labels,
    include_lowest=True
)

print("\nAge Groups:")
print(data[["age", "Age_Group"]].head(10))


# --------------------------------------------------
# 6. OUTLIER DETECTION USING IQR
# --------------------------------------------------

# We will check potential outliers in the Fare column.

Q1 = data["fare"].quantile(0.25)
Q3 = data["fare"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - (1.5 * IQR)
upper_limit = Q3 + (1.5 * IQR)

outliers = data[
    (data["fare"] < lower_limit) |
    (data["fare"] > upper_limit)
]

print("\nIQR Results:")
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)
print("Potential Outliers:", len(outliers))

# Visualize potential outliers.
sns.boxplot(x=data["fare"])
plt.title("Fare Outlier Detection")
plt.show()

# Important:
# We are detecting outliers, not automatically deleting them.
# Investigate outliers before deciding what to do.


# --------------------------------------------------
# 7. FEATURE SCALING
# --------------------------------------------------

# Select numerical columns for scaling.

numeric_features = data[
    ["age", "fare", "sibsp", "parch"]
]

# Standardization
standard_scaler = StandardScaler()

standard_scaled = standard_scaler.fit_transform(
    numeric_features
)

standard_scaled_df = pd.DataFrame(
    standard_scaled,
    columns=numeric_features.columns
)

print("\nStandard Scaled Data:")
print(standard_scaled_df.head())

# Min-Max Normalization
minmax_scaler = MinMaxScaler()

normalized_data = minmax_scaler.fit_transform(
    numeric_features
)

normalized_df = pd.DataFrame(
    normalized_data,
    columns=numeric_features.columns
)

print("\nMin-Max Normalized Data:")
print(normalized_df.head())


# --------------------------------------------------
# 8. FEATURE CONSTRUCTION
# --------------------------------------------------

# Create a new feature using existing columns.

# SibSp = siblings/spouses aboard
# Parch = parents/children aboard
# Add 1 for the passenger.

data["Family_Size"] = (
    data["sibsp"] + data["parch"] + 1
)

print("\nFamily Size:")
print(data[["sibsp", "parch", "Family_Size"]].head())

# Create a categorical family type.

def get_family_type(size):

    if size == 1:
        return "Alone"

    elif size <= 4:
        return "Small Family"

    else:
        return "Large Family"


data["Family_Type"] = data["Family_Size"].apply(
    get_family_type
)

print("\nFamily Types:")
print(data[["Family_Size", "Family_Type"]].head(10))


# --------------------------------------------------
# 9. FEATURE SELECTION USING SelectKBest
# --------------------------------------------------

# SelectKBest chooses useful existing features.
# We use a small set of numerical features for this example.

feature_columns = [
    "age",
    "fare",
    "sibsp",
    "parch",
    "pclass"
]

X = data[feature_columns]
y = data["survived"]

# Split data before fitting feature selection.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Impute missing values using training data only.
imputer = SimpleImputer(strategy="median")

X_train_imputed = imputer.fit_transform(X_train)
X_test_imputed = imputer.transform(X_test)

# Select the 3 best features.
selector = SelectKBest(
    score_func=f_classif,
    k=3
)

X_train_selected = selector.fit_transform(
    X_train_imputed,
    y_train
)

X_test_selected = selector.transform(
    X_test_imputed
)

selected_features = [
    feature_columns[i]
    for i in selector.get_support(indices=True)
]

print("\nSelected Features:")
print(selected_features)

print("\nSelected Training Data Shape:")
print(X_train_selected.shape)


# --------------------------------------------------
# 10. FEATURE EXTRACTION USING PCA
# --------------------------------------------------

# PCA creates new features called principal components.
# We apply PCA to the imputed and scaled numerical data.

pca_scaler = StandardScaler()

X_train_scaled = pca_scaler.fit_transform(
    X_train_imputed
)

X_test_scaled = pca_scaler.transform(
    X_test_imputed
)

# Reduce 5 original features to 2 new components.
pca = PCA(n_components=2)

X_train_pca = pca.fit_transform(
    X_train_scaled
)

X_test_pca = pca.transform(
    X_test_scaled
)

print("\nPCA Training Data:")
print(X_train_pca[:5])

print("\nOriginal Number of Features:")
print(X_train.shape[1])

print("New Number of PCA Features:")
print(X_train_pca.shape[1])

print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)

print(
    "Total Explained Variance:",
    pca.explained_variance_ratio_.sum()
)


# --------------------------------------------------
# 11. FINAL SUMMARY
# --------------------------------------------------

print("\nFeature Engineering Practice Completed!")

print("Original Dataset Shape:", df.shape)
print("Dataset After Feature Construction:", data.shape)

print("\nNew Features Created:")
print([
    "Age_Group",
    "Family_Size",
    "Family_Type"
])

print("\nTopics Practiced:")
print("1. Missing Value Imputation")
print("2. One-Hot Encoding")
print("3. Binning")
print("4. Outlier Detection")
print("5. Feature Scaling")
print("6. Feature Construction")
print("7. Feature Selection")
print("8. Feature Extraction using PCA")


# --------------------------------------------------
# IMPORTANT LEARNING NOTES
# --------------------------------------------------

# 1. Feature Transformation changes existing features.
# 2. Feature Construction creates new features.
# 3. Feature Selection chooses useful existing features.
# 4. Feature Extraction creates new features from old ones.
# 5. Do not remove outliers without understanding them.
# 6. Fit scalers, imputers, and selectors on training data only.
# 7. PCA should be applied to appropriately scaled numerical data.

# --------------------------------------------------
# INSTALL REQUIRED LIBRARIES
# --------------------------------------------------

# Run this command in your terminal:
#
# pip install pandas seaborn matplotlib scikit-learn
#
# Note:
# Seaborn may need internet access to download its Titanic dataset
# the first time you run this program.

Code run karne ke liye: Terminal mein pip install pandas seaborn matplotlib scikit-learn run karein. Is example mein Titanic dataset Seaborn se load hota hai, is liye first run par internet required ho sakta hai.
