# EDA Using Univariate Analysis | Day 20

## 1. What is EDA?

EDA stands for **Exploratory Data Analysis**.

It is the process of exploring and understanding a dataset before building a Machine Learning model.

In EDA, we use:
- Data analysis
- Statistical calculations
- Graphs and charts
- Data visualization

The main purpose of EDA is to understand what information our dataset contains.

### Why is EDA important?

EDA helps us:
- Understand the data.
- Find patterns and trends.
- Identify missing values.
- Detect outliers.
- Understand the distribution of data.
- Find relationships between variables.
- Make better decisions before training a model.

There are two important types of analysis:

1. **Univariate Analysis:** Studying one variable at a time.
2. **Multivariate Analysis:** Studying two or more variables together.

In this lesson, we focus on Univariate Analysis.

---

## 2. What is Univariate Analysis?

The word Univariate has two parts:

- Uni = One
- Variate = Variable

Univariate Analysis means studying **one column or variable at a time**.

For example, in the Titanic dataset, we can study:
- Passenger age.
- Passenger gender.
- Passenger class.
- Passenger survival.

We study each column separately to understand its values and distribution.

### Types of Data

Before performing Univariate Analysis, we should understand two main types of data.

**1. Numerical Data**

Numerical data contains numbers.

Examples:
- Age
- Height
- Weight
- Price
- Fare

**2. Categorical Data**

Categorical data contains groups or categories.

Examples:
- Gender
- Country
- City
- Department
- Passenger class

Some columns contain numbers but represent categories.

For example:
- `Pclass`: 1, 2, 3
- `Survived`: 0, 1

These are numerical-looking values, but they represent categories.

We should understand what a column means before deciding how to analyze it.

---

## 3. Understanding the Titanic Dataset

The Titanic dataset contains information about passengers who travelled on the Titanic.

Each row represents one passenger.

Some important columns are:

| Column | Meaning |
|---|---|
| PassengerId | Unique passenger ID |
| Survived | 0 = Did not survive, 1 = Survived |
| Pclass | Passenger class: 1, 2, or 3 |
| Name | Passenger name |
| Sex | Passenger gender |
| Age | Passenger age |
| SibSp | Number of siblings or spouses aboard |
| Parch | Number of parents or children aboard |
| Fare | Ticket price |
| Embarked | Port where the passenger boarded |

Our goal is to understand these columns using Univariate Analysis.

---

# Part A: Categorical Data Analysis

## 4. What is Categorical Data Analysis?

Categorical data contains different groups or categories.

For example, the `Survived` column contains two categories:

- 0 = Did not survive
- 1 = Survived

When analyzing categorical data, we mainly want to know:

- How many times does each category appear?
- Which category appears most often?
- Which category appears least often?
- What percentage belongs to each category?

Two useful visualizations are:

1. Count Plot
2. Pie Chart

---

## 5. Count Plot

A Count Plot shows how many times each category appears in a column.

For example, we can use it to find how many passengers survived and how many did not survive.

### Using Value Counts

Before creating a graph, we can count the values using Pandas.

```python
df["Survived"].value_counts()
```

Example output:

```text
0    549
1    342
```

This means:
- 549 passengers did not survive.
- 342 passengers survived.

### Creating a Count Plot

We can use Seaborn to create a Count Plot.

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(data=df, x="Survived")

plt.title("Passenger Survival Count")
plt.show()
```

The graph displays the number of passengers in each category.

### Where Can We Use Count Plots?

We can use Count Plots for:
- Gender distribution.
- Passenger class distribution.
- Survival count.
- Embarkation port distribution.

Example:

```python
sns.countplot(data=df, x="Pclass")
plt.show()
```

This shows how many passengers travelled in each class.

---

## 6. Pie Chart

A Pie Chart shows the percentage or proportion of each category.

For example, we can use it to understand what percentage of passengers survived.

```python
df["Survived"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Passenger Survival Percentage")
plt.ylabel("")
plt.show()
```

### Understanding `autopct`

`autopct="%1.1f%%"` displays percentages on the pie chart.

For example:
- 61.6% did not survive.
- 38.4% survived.

### Count Plot vs Pie Chart

| Count Plot | Pie Chart |
|---|---|
| Shows category counts | Shows category percentages |
| Uses bars | Uses a circle |
| Easy to compare counts | Easy to understand proportions |

**Remember:** Both charts help us understand categorical data, but they show information in different ways.

---

# Part B: Numerical Data Analysis

## 7. What is Numerical Data Analysis?

Numerical data contains numbers that can have many different values.

Examples from the Titanic dataset:
- Age
- Fare

For numerical data, we want to understand:
- Minimum value.
- Maximum value.
- Average value.
- Data distribution.
- Outliers.
- Whether the data is symmetric or skewed.

Three important graphs are:

1. Histogram
2. KDE Plot
3. Box Plot

---

## 8. Histogram

A Histogram shows the distribution of numerical data.

It groups numerical values into intervals called **bins**.

For example, we can divide passenger ages into groups:

- 0–10 years
- 10–20 years
- 20–30 years
- 30–40 years
- 40–50 years

The histogram shows how many passengers belong to each age group.

### Python Code

```python
sns.histplot(data=df, x="Age", bins=10)

plt.title("Age Distribution")
plt.show()
```

### What Does a Histogram Tell Us?

It helps us understand:
- Which values appear most often.
- Which values appear less often.
- Whether most values are small or large.
- How the data is distributed.

### What Are Bins?

Bins are the intervals used to group numerical values.

For example:

```python
sns.histplot(data=df, x="Age", bins=20)
```

Changing the number of bins changes the appearance of the histogram.

- More bins create smaller intervals.
- Fewer bins create larger intervals.

Choose a suitable number of bins so the distribution is easy to understand.

---

## 9. KDE Plot

KDE stands for **Kernel Density Estimation**.

A KDE Plot shows a smooth curve representing the distribution of numerical data.

It is useful for understanding where values are concentrated.

### Python Code

```python
sns.kdeplot(data=df, x="Age")

plt.title("Age Distribution - KDE Plot")
plt.show()
```

### Understanding KDE

Imagine that we want to understand the age distribution of Titanic passengers.

The KDE curve helps us see:
- Where most ages are concentrated.
- Where fewer ages are found.
- The overall shape of the distribution.

### Histogram vs KDE Plot

| Histogram | KDE Plot |
|---|---|
| Uses bars | Uses a smooth curve |
| Groups values into bins | Estimates a smooth density |
| Shows frequency or count | Shows probability density |

**Important:** KDE shows probability density, not the probability of one exact value. The total area under the curve is 1.

We can also display a KDE curve over a histogram:

```python
sns.histplot(
    data=df,
    x="Age",
    bins=20,
    kde=True
)

plt.title("Age Distribution")
plt.show()
```

---

## 10. Box Plot

A Box Plot is used to understand the spread of numerical data and identify potential outliers.

It is based on the **Five Number Summary**.

The five values are:

1. Minimum
2. First Quartile (Q1)
3. Median (Q2)
4. Third Quartile (Q3)
5. Maximum

### Understanding the Five Number Summary

**Minimum:** The smallest value within the lower whisker.

**Q1 (25th Percentile):** 25% of the data values are at or below this value.

**Median (50th Percentile):** The middle value of the data.

**Q3 (75th Percentile):** 75% of the data values are at or below this value.

**Maximum:** The largest value within the upper whisker.

### What is IQR?

IQR stands for **Interquartile Range**.

It measures the spread of the middle 50% of the data.

Formula:

```text
IQR = Q3 - Q1
```

### How Does a Box Plot Identify Outliers?

A common rule uses these limits:

```text
Lower Limit = Q1 - 1.5 × IQR

Upper Limit = Q3 + 1.5 × IQR
```

Values below the lower limit or above the upper limit are considered potential outliers.

### Python Code

```python
sns.boxplot(data=df, x="Age")

plt.title("Age Box Plot")
plt.show()
```

### Why Are Box Plots Useful?

They help us:
- Understand the spread of data.
- See the median.
- Compare the range of values.
- Identify potential outliers.

**Important:** A point outside the whiskers is a potential outlier, not automatically an incorrect value. Always investigate before removing it.

---

## 11. Understanding Skewness

Skewness tells us whether a numerical distribution is symmetric or tilted towards one side.

There are three common types.

### 1. Symmetrical Distribution

In a symmetrical distribution, both sides of the graph look approximately balanced.

The values are distributed around the center.

```text
Skewness ≈ 0
```

### 2. Positive Skew (Right Skew)

In positive skew:
- Most values are concentrated on the left.
- A long tail extends towards the right.
- A few values are much larger than most other values.

Example: Income or salary data can sometimes have positive skew.

```text
Skewness > 0
```

### 3. Negative Skew (Left Skew)

In negative skew:
- Most values are concentrated on the right.
- A long tail extends towards the left.
- A few values are much smaller than most other values.

```text
Skewness < 0
```

### Checking Skewness in Pandas

```python
df["Age"].skew()
```

We can also check Fare:

```python
df["Fare"].skew()
```

A positive result indicates right skew, while a negative result indicates left skew.

A result close to zero suggests a more symmetrical distribution, but it does not guarantee a perfectly normal distribution.

---

## 12. Important Python Libraries

We use three main libraries in this lesson.

| Library | Purpose |
|---|---|
| Pandas | Reading and analyzing data |
| Matplotlib | Creating graphs |
| Seaborn | Creating statistical visualizations |

Install them using:

```bash
pip install pandas matplotlib seaborn
```

Import them:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

---

## 13. Quick Revision

| Topic | Purpose | Python Command |
|---|---|---|
| EDA | Understand the dataset | Analysis process |
| Univariate Analysis | Study one variable | Analyze one column |
| Value Counts | Count categories | `df["Sex"].value_counts()` |
| Count Plot | Display category counts | `sns.countplot()` |
| Pie Chart | Display category percentages | `plot(kind="pie")` |
| Histogram | Understand numerical distribution | `sns.histplot()` |
| KDE Plot | Display smooth data distribution | `sns.kdeplot()` |
| Box Plot | Understand spread and potential outliers | `sns.boxplot()` |
| Skewness | Check distribution shape | `df["Age"].skew()` |

---

## 14. Practice Tasks

Use the Titanic dataset and complete these tasks:

### Categorical Data

1. Find the number of male and female passengers.
2. Find how many passengers survived.
3. Create a Count Plot for `Survived`.
4. Create a Count Plot for `Pclass`.
5. Create a Pie Chart for `Sex`.
6. Create a Pie Chart for `Survived`.

### Numerical Data

7. Create a Histogram for `Age`.
8. Create a Histogram for `Fare`.
9. Create a KDE Plot for `Age`.
10. Create a Box Plot for `Age`.
11. Create a Box Plot for `Fare`.
12. Calculate the skewness of `Age` and `Fare`.

### Thinking Questions

13. Which passenger class has the most passengers?
14. Which survival category has more passengers?
15. What does the Age histogram tell you?
16. Does the Fare column contain potential outliers?
17. Is the Fare distribution positively or negatively skewed?

---

## 15. Useful Documentation

- Pandas: https://pandas.pydata.org/docs/
- Matplotlib: https://matplotlib.org/stable/
- Seaborn: https://seaborn.pydata.org/
- Seaborn Count Plot: https://seaborn.pydata.org/generated/seaborn.countplot.html
- Seaborn Histogram: https://seaborn.pydata.org/generated/seaborn.histplot.html
- Seaborn KDE Plot: https://seaborn.pydata.org/generated/seaborn.kdeplot.html
- Seaborn Box Plot: https://seaborn.pydata.org/generated/seaborn.boxplot.html

---

## Conclusion

EDA helps us understand our data before applying Machine Learning algorithms.

Univariate Analysis focuses on one variable at a time.

For categorical data, we commonly use:
- Count Plot
- Pie Chart

For numerical data, we commonly use:
- Histogram
- KDE Plot
- Box Plot

These graphs help us understand categories, distributions, data spread, skewness, and potential outliers.

**Next Topic:** Multivariate Analysis.
