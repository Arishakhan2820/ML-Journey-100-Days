# Day_21_EDA_Bivariate_Multivariate_Analysis.py

# Day 21: EDA Using Bivariate and Multivariate Analysis

# Required libraries:
# pip install pandas matplotlib seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# --------------------------------------------------
# 1. LOAD DATASETS
# --------------------------------------------------

# Seaborn provides some example datasets.
# The first time you load them, an internet connection
# may be required.

tips = sns.load_dataset("tips")
titanic = sns.load_dataset("titanic")
flights = sns.load_dataset("flights")
iris = sns.load_dataset("iris")

# Display the first five rows of each dataset.

print("\nTIPS DATASET")
print(tips.head())

print("\nTITANIC DATASET")
print(titanic.head())

print("\nFLIGHTS DATASET")
print(flights.head())

print("\nIRIS DATASET")
print(iris.head())


# --------------------------------------------------
# 2. SCATTER PLOT
# Numerical vs Numerical
# --------------------------------------------------

# Example: Total bill and tip.

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip"
)

plt.title("Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()


# --------------------------------------------------
# 3. MULTIVARIATE SCATTER PLOT
# Adding hue, style, and size
# --------------------------------------------------

plt.figure(figsize=(9, 6))

sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="sex",
    style="smoker",
    size="size",
    sizes=(30, 200)
)

plt.title("Tips: Multivariate Scatter Plot")
plt.show()


# --------------------------------------------------
# 4. BAR PLOT
# Numerical vs Categorical
# --------------------------------------------------

# Example: Average passenger age in each class.

plt.figure(figsize=(8, 5))

sns.barplot(
    data=titanic,
    x="pclass",
    y="age"
)

plt.title("Average Age by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Average Age")
plt.show()


# --------------------------------------------------
# 5. MULTIVARIATE BAR PLOT
# Adding gender using hue
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.barplot(
    data=titanic,
    x="pclass",
    y="age",
    hue="sex"
)

plt.title("Average Age by Class and Gender")
plt.show()


# --------------------------------------------------
# 6. BOX PLOT
# Numerical vs Categorical
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=titanic,
    x="sex",
    y="age"
)

plt.title("Age Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Age")
plt.show()


# --------------------------------------------------
# 7. MULTIVARIATE BOX PLOT
# Gender and Survival
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=titanic,
    x="sex",
    y="age",
    hue="survived"
)

plt.title("Age by Gender and Survival")
plt.show()


# --------------------------------------------------
# 8. KDE PLOT
# Numerical vs Categorical
# --------------------------------------------------

# Separate passengers into two groups.
# survived = 0 means did not survive.
# survived = 1 means survived.

not_survived = titanic[titanic["survived"] == 0]
survived = titanic[titanic["survived"] == 1]

plt.figure(figsize=(9, 5))

sns.kdeplot(
    data=not_survived,
    x="age",
    label="Not Survived"
)

sns.kdeplot(
    data=survived,
    x="age",
    label="Survived"
)

plt.title("Age Distribution by Survival")
plt.xlabel("Age")
plt.ylabel("Density")
plt.legend()
plt.show()


# --------------------------------------------------
# 9. HEATMAP
# Categorical vs Categorical
# --------------------------------------------------

# Cross-tabulation counts passengers by class and survival.

result = pd.crosstab(
    titanic["pclass"],
    titanic["survived"]
)

print("\nPassenger Class vs Survival:")
print(result)

plt.figure(figsize=(7, 5))

sns.heatmap(
    result,
    annot=True,
    fmt="d",
    cmap="Blues"
)

plt.title("Passenger Class vs Survival (Counts)")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Passenger Class")
plt.show()


# --------------------------------------------------
# 10. HEATMAP USING PERCENTAGES
# --------------------------------------------------

# normalize="index" calculates percentages within each row.
# Each passenger class will have percentages adding to 100.

survival_percentage = pd.crosstab(
    titanic["pclass"],
    titanic["survived"],
    normalize="index"
) * 100

print("\nSurvival Percentage by Passenger Class:")
print(survival_percentage.round(2))

plt.figure(figsize=(7, 5))

sns.heatmap(
    survival_percentage,
    annot=True,
    fmt=".1f",
    cmap="YlGnBu"
)

plt.title("Survival Percentage by Passenger Class")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Passenger Class")
plt.show()


# --------------------------------------------------
# 11. CLUSTERMAP
# --------------------------------------------------

# ClusterMap groups similar rows and columns.

sns.clustermap(
    result,
    annot=True,
    fmt="d",
    cmap="Blues"
)

plt.suptitle("Passenger Class and Survival ClusterMap")
plt.show()


# --------------------------------------------------
# 12. PAIR PLOT
# Multiple Numerical Variables
# --------------------------------------------------

# Iris contains four numerical measurements
# and one categorical column called species.

sns.pairplot(iris)

plt.suptitle("Iris Dataset Pair Plot", y=1.02)
plt.show()


# --------------------------------------------------
# 13. MULTIVARIATE PAIR PLOT
# Adding species using hue
# --------------------------------------------------

sns.pairplot(
    iris,
    hue="species"
)

plt.suptitle("Iris Pair Plot by Species", y=1.02)
plt.show()


# --------------------------------------------------
# 14. LINE PLOT
# Numerical vs Time
# --------------------------------------------------

# Calculate total passengers for each year.

yearly_data = (
    flights.groupby("year")["passengers"]
    .sum()
    .reset_index()
)

print("\nYearly Passenger Data:")
print(yearly_data.head())

plt.figure(figsize=(10, 5))

sns.lineplot(
    data=yearly_data,
    x="year",
    y="passengers",
    marker="o"
)

plt.title("Yearly Passenger Trend")
plt.xlabel("Year")
plt.ylabel("Total Passengers")
plt.show()


# --------------------------------------------------
# 15. PIVOT TABLE
# --------------------------------------------------

# Rows represent months.
# Columns represent years.
# Values represent passenger numbers.

pivot_data = flights.pivot_table(
    values="passengers",
    index="month",
    columns="year"
)

print("\nFlights Pivot Table:")
print(pivot_data)


# --------------------------------------------------
# 16. HEATMAP USING PIVOT TABLE
# --------------------------------------------------

plt.figure(figsize=(12, 7))

sns.heatmap(
    pivot_data,
    cmap="YlGnBu"
)

plt.title("Monthly Passengers Across Years")
plt.xlabel("Year")
plt.ylabel("Month")
plt.show()


# --------------------------------------------------
# 17. CLUSTERMAP USING PIVOT TABLE
# --------------------------------------------------

sns.clustermap(
    pivot_data,
    cmap="YlGnBu",
    figsize=(12, 9)
)

plt.suptitle("Flights Data ClusterMap", y=1.02)
plt.show()


# --------------------------------------------------
# 18. PRACTICE TASKS
# --------------------------------------------------

# Try these tasks yourself:

# 1. Create a scatter plot using total_bill and tip.
# 2. Add gender and smoker information using hue and style.
# 3. Create a bar plot showing average age by passenger class.
# 4. Create a box plot comparing age by gender.
# 5. Compare age distributions of survived and not-survived passengers.
# 6. Create a heatmap for gender and survival.
# 7. Calculate survival percentages for each passenger class.
# 8. Create a pair plot using the Iris dataset.
# 9. Create a line plot showing yearly passenger numbers.
# 10. Create a pivot table and visualize it using a heatmap.

print("\nDay 21 practice completed!")

Important: This practice script loads the example datasets directly from Seaborn, so an internet connection may be required the first time. Install the libraries in your terminal using:
pip install pandas matplotlib seaborn
