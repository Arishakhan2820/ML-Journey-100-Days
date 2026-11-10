# Day 19 - Understanding Your Data
# Topic: Basic questions to ask when you receive a dataset

# Install required library:
# pip install pandas

import pandas as pd


# --------------------------------------------------
# 1. LOAD THE DATASET
# --------------------------------------------------

# Keep titanic.csv in the same folder as this Python file.
df = pd.read_csv("titanic.csv")

print("\nOriginal Dataset:")
print(df.head())


# --------------------------------------------------
# 2. HOW BIG IS THE DATASET?
# --------------------------------------------------

print("\n1. Dataset Shape:")
print(df.shape)

print("Total Rows:", df.shape[0])
print("Total Columns:", df.shape[1])


# --------------------------------------------------
# 3. WHAT DOES THE DATA LOOK LIKE?
# --------------------------------------------------

print("\n2. First 5 Rows:")
print(df.head())

print("\nFirst 10 Rows:")
print(df.head(10))

print("\nLast 5 Rows:")
print(df.tail())

print("\n5 Random Rows:")
print(df.sample(5, random_state=42))


# --------------------------------------------------
# 4. WHAT ARE THE DATA TYPES?
# --------------------------------------------------

print("\n3. Dataset Information:")
df.info()

print("\nColumn Data Types:")
print(df.dtypes)

print("\nColumn Names:")
print(df.columns.tolist())


# --------------------------------------------------
# 5. HOW MUCH MEMORY DOES THE DATASET USE?
# --------------------------------------------------

print("\n4. Memory Usage:")
df.info(memory_usage="deep")

print("\nMemory Used by Each Column:")
print(df.memory_usage(deep=True))


# --------------------------------------------------
# 6. ARE THERE MISSING VALUES?
# --------------------------------------------------

print("\n5. Missing Values in Each Column:")
print(df.isnull().sum())

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

print("\nColumns Containing Missing Values:")
missing_columns = df.isnull().sum()

print(missing_columns[missing_columns > 0])


# Missing value percentage in each column
print("\nMissing Value Percentage:")
missing_percentage = (df.isnull().mean() * 100).round(2)

print(missing_percentage)


# --------------------------------------------------
# 7. STATISTICAL SUMMARY
# --------------------------------------------------

print("\n6. Numerical Columns Summary:")
print(df.describe())

print("\nCategorical Columns Summary:")
print(df.describe(include="object"))


# Summary of a single column
if "Age" in df.columns:
    print("\nAge Column Summary:")
    print(df["Age"].describe())


# --------------------------------------------------
# 8. ARE THERE DUPLICATE ROWS?
# --------------------------------------------------

print("\n7. Duplicate Rows Count:")
print(df.duplicated().sum())

print("\nDuplicate Rows:")
print(df[df.duplicated()])


# To remove duplicates, uncomment the following lines:
# df = df.drop_duplicates()
# print("Shape after removing duplicates:", df.shape)


# --------------------------------------------------
# 9. CORRELATION BETWEEN NUMERICAL COLUMNS
# --------------------------------------------------

print("\n8. Correlation Matrix:")

correlation = df.corr(numeric_only=True)

print(correlation)


# --------------------------------------------------
# 10. CORRELATION WITH TARGET COLUMN
# --------------------------------------------------

if "Survived" in df.columns:

    print("\n9. Correlation With Survived:")

    survival_correlation = correlation["Survived"].sort_values(
        ascending=False
    )

    print(survival_correlation)

else:
    print("\nSurvived column was not found.")


# --------------------------------------------------
# 11. OPTIONAL: MEMORY OPTIMIZATION EXAMPLE
# --------------------------------------------------

# Always check the values before changing a data type.
# Example: convert Age from float to a smaller integer type
# only if you have handled missing values and decimal precision
# is not important.

# Example:
#
# df["Age"] = df["Age"].fillna(df["Age"].median())
# df["Age"] = df["Age"].astype("int32")


# --------------------------------------------------
# 12. FINAL DATASET SUMMARY
# --------------------------------------------------

print("\n10. Final Dataset Summary:")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Duplicate Rows:", df.duplicated().sum())
print("Total Missing Values:", df.isnull().sum().sum())

print("\nDay 19 Practice Completed!")

Important: Keep the titanic.csv file in the same folder as your Python file. If Pandas is not installed, open your terminal and type:
# </> Bash 
pip install pandas
