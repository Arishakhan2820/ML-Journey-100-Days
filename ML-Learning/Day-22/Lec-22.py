# Day_22_Pandas_Profiling.py

# Day 22: Pandas Profiling

# Modern library name: ydata-profiling

# Install required libraries:
# pip install pandas seaborn ydata-profiling


# --------------------------------------------------
# 1. IMPORT LIBRARIES
# --------------------------------------------------

import pandas as pd
import seaborn as sns

from ydata_profiling import ProfileReport


# --------------------------------------------------
# 2. LOAD DATASET
# --------------------------------------------------

# Load the Titanic dataset from Seaborn.

df = sns.load_dataset("titanic")

# If you want to use your own CSV dataset,
# replace the line above with:
#
# df = pd.read_csv("titanic.csv")


# --------------------------------------------------
# 3. BASIC DATASET INFORMATION
# --------------------------------------------------

print("\nFIRST FIVE ROWS:")
print(df.head())

print("\nLAST FIVE ROWS:")
print(df.tail())

print("\nDATASET SHAPE:")
print(df.shape)

print("\nCOLUMN NAMES:")
print(df.columns)

print("\nDATA TYPES:")
print(df.dtypes)

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())


# --------------------------------------------------
# 4. CREATE PROFILE REPORT
# --------------------------------------------------

# ProfileReport automatically analyzes the dataset.

profile = ProfileReport(
    df,
    title="Titanic Dataset Profiling Report",
    explorative=True
)


# --------------------------------------------------
# 5. EXPORT REPORT TO HTML
# --------------------------------------------------

# Save the report in the current project folder.

profile.to_file("titanic_report.html")

print("\nProfiling report created successfully!")

print("Open titanic_report.html in your browser.")


# --------------------------------------------------
# 6. OPTIONAL: DISPLAY REPORT IN JUPYTER NOTEBOOK
# --------------------------------------------------

# If you are running this code inside Jupyter Notebook,
# you can display the report directly.

# profile.to_notebook_iframe()


# --------------------------------------------------
# 7. EXPLORE DATASET INFORMATION
# --------------------------------------------------

# These commands help us understand the dataset manually.

print("\nNUMERICAL COLUMN SUMMARY:")
print(df.describe())

print("\nALL COLUMN SUMMARY:")
print(df.describe(include="all"))

print("\nNUMBER OF UNIQUE VALUES:")
print(df.nunique())


# --------------------------------------------------
# 8. CHECK MISSING VALUE PERCENTAGE
# --------------------------------------------------

missing_percentage = (
    df.isnull().mean() * 100
)

print("\nMISSING VALUE PERCENTAGE:")
print(missing_percentage.round(2))


# --------------------------------------------------
# 9. CHECK CORRELATION
# --------------------------------------------------

# Select numerical columns only.

numeric_df = df.select_dtypes(include="number")

correlation = numeric_df.corr()

print("\nCORRELATION MATRIX:")
print(correlation)


# --------------------------------------------------
# 10. PRACTICE TASKS
# --------------------------------------------------

# Try these tasks yourself:

# 1. Load another dataset.
# 2. Generate its profiling report.
# 3. Save the report with a different HTML filename.
# 4. Identify columns with missing values.
# 5. Find columns with high numbers of unique values.
# 6. Explore numerical and categorical variables.
# 7. Check the correlation section.
# 8. Write down five observations from your report.

print("\nDay 22 practice completed!")

Important setup note: Is script mein modern library ydata-profiling use hui hai. Purane tutorials mein pandas-profiling ka naam aur import mil sakta hai. Dono ko mix na karein.

Install karne ke baad Python file run karein. Aapke project folder mein titanic_report.html generate hogi. Usay browser mein open karke complete report explore kar sakti hain.
