# Day 20 - EDA Using Univariate Analysis
# Topic: Categorical and Numerical Data Analysis

# Install libraries:
# pip install pandas matplotlib seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# --------------------------------------------------
# 1. LOAD THE DATASET
# --------------------------------------------------

# Keep titanic.csv in the same folder as this Python file.

df = pd.read_csv("titanic.csv")

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)


# --------------------------------------------------
# 2. UNDERSTAND THE DATA
# --------------------------------------------------

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())


# --------------------------------------------------
# 3. CATEGORICAL DATA ANALYSIS
# --------------------------------------------------

# Categorical columns in the Titanic dataset

categorical_columns = [
    "Survived",
    "Pclass",
    "Sex",
    "Embarked"
]


# --------------------------------------------------
# 4. VALUE COUNTS
# --------------------------------------------------

# Value counts show how many times each category appears.

print("\nSurvival Count:")
print(df["Survived"].value_counts())

print("\nPassenger Class Count:")
print(df["Pclass"].value_counts())

print("\nGender Count:")
print(df["Sex"].value_counts())

print("\nEmbarked Count:")
print(df["Embarked"].value_counts())


# --------------------------------------------------
# 5. COUNT PLOT
# --------------------------------------------------

# Count Plot for Survival

sns.countplot(data=df, x="Survived")

plt.title("Passenger Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")
plt.show()


# Count Plot for Passenger Class

sns.countplot(data=df, x="Pclass")

plt.title("Passenger Class Count")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.show()


# Count Plot for Gender

sns.countplot(data=df, x="Sex")

plt.title("Gender Count")
plt.xlabel("Gender")
plt.ylabel("Number of Passengers")
plt.show()


# --------------------------------------------------
# 6. PIE CHART
# --------------------------------------------------

# Pie Chart for Survival

survival_counts = df["Survived"].value_counts()

survival_counts.plot(
    kind="pie",
    autopct="%1.1f%%",
    labels=["Did Not Survive", "Survived"]
)

plt.title("Passenger Survival Percentage")
plt.ylabel("")
plt.show()


# Pie Chart for Gender

gender_counts = df["Sex"].value_counts()

gender_counts.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Gender Percentage")
plt.ylabel("")
plt.show()


# --------------------------------------------------
# 7. NUMERICAL DATA ANALYSIS
# --------------------------------------------------

# Age and Fare are numerical columns.

numerical_columns = ["Age", "Fare"]

print("\nNumerical Data Summary:")
print(df[numerical_columns].describe())


# --------------------------------------------------
# 8. HISTOGRAM
# --------------------------------------------------

# Histogram for Age

sns.histplot(
    data=df,
    x="Age",
    bins=20
)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.show()


# Histogram for Fare

sns.histplot(
    data=df,
    x="Fare",
    bins=20
)

plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Number of Passengers")
plt.show()


# --------------------------------------------------
# 9. HISTOGRAM WITH KDE
# --------------------------------------------------

# Histogram and KDE curve together

sns.histplot(
    data=df,
    x="Age",
    bins=20,
    kde=True
)

plt.title("Age Distribution with KDE")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.show()


# --------------------------------------------------
# 10. KDE PLOT
# --------------------------------------------------

# KDE Plot for Age

sns.kdeplot(
    data=df,
    x="Age"
)

plt.title("Age KDE Plot")
plt.xlabel("Age")
plt.show()


# KDE Plot for Fare

sns.kdeplot(
    data=df,
    x="Fare"
)

plt.title("Fare KDE Plot")
plt.xlabel("Fare")
plt.show()


# --------------------------------------------------
# 11. BOX PLOT
# --------------------------------------------------

# Box Plot for Age

sns.boxplot(
    data=df,
    x="Age"
)

plt.title("Age Box Plot")
plt.xlabel("Age")
plt.show()


# Box Plot for Fare

sns.boxplot(
    data=df,
    x="Fare"
)

plt.title("Fare Box Plot")
plt.xlabel("Fare")
plt.show()


# --------------------------------------------------
# 12. FIVE NUMBER SUMMARY
# --------------------------------------------------

print("\nAge Five Number Summary:")

age_summary = df["Age"].describe()[
    ["min", "25%", "50%", "75%", "max"]
]

print(age_summary)


print("\nFare Five Number Summary:")

fare_summary = df["Fare"].describe()[
    ["min", "25%", "50%", "75%", "max"]
]

print(fare_summary)


# --------------------------------------------------
# 13. FIND IQR AND POTENTIAL OUTLIERS
# --------------------------------------------------

# IQR = Q3 - Q1

for column in numerical_columns:

    data = df[column].dropna()

    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - (1.5 * IQR)
    upper_limit = Q3 + (1.5 * IQR)

    outliers = data[
        (data < lower_limit) |
        (data > upper_limit)
    ]

    print(f"\nPotential Outliers in {column}:")

    print("Q1:", Q1)
    print("Q3:", Q3)
    print("IQR:", IQR)
    print("Lower Limit:", lower_limit)
    print("Upper Limit:", upper_limit)
    print("Number of Potential Outliers:", len(outliers))


# --------------------------------------------------
# 14. CHECK SKEWNESS
# --------------------------------------------------

print("\nAge Skewness:")
print(df["Age"].skew())

print("\nFare Skewness:")
print(df["Fare"].skew())


# Check skewness of both numerical columns

print("\nSkewness of Numerical Columns:")
print(df[numerical_columns].skew())


# --------------------------------------------------
# 15. FINAL SUMMARY
# --------------------------------------------------

print("\nUnivariate Analysis Completed!")

print("\nCategorical Columns:")
print(categorical_columns)

print("\nNumerical Columns:")
print(numerical_columns)

print("\nDay 20 Practice Completed!")

Important: Keep the titanic.csv file in the same folder as your Python file. If the required libraries are not installed, open your terminal and run:

pip install pandas matplotlib seaborn

One important thing to remember: Univariate Analysis studies one column at a time. For example, when studying Age, we focus only on the Age column—not its relationship with survival. That relationship will come under Multivariate Analysis.
