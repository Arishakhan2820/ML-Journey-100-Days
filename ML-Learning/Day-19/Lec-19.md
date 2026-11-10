# Understanding Your Data | Day 19

## 1. Introduction

When we receive a new dataset for a Machine Learning project, we should not immediately start training a model.

First, we need to understand the data.

We should ask some basic questions:

1. How big is the dataset?
2. What does the data look like?
3. What are the data types of each column?
4. Are there missing values?
5. What is the mathematical summary of numerical columns?
6. Are there duplicate rows?
7. Is there any correlation between columns?

In this lesson, we use the famous **Titanic dataset** to understand these questions.

---

## 2. Importing the Dataset

First, we import Pandas and load our dataset.

```python
import pandas as pd

df = pd.read_csv("titanic.csv")
```

Here:
- `pandas` is a Python library used for data analysis.
- `read_csv()` reads a CSV file.
- `df` is the DataFrame containing our dataset.

A DataFrame is a table containing rows and columns.

---

## 3. How Big Is the Dataset?

**Question:** How many rows and columns are present in our dataset?

We can use the `shape` attribute.

```python
df.shape
```

Example output:

```text
(891, 12)
```

It means:
- 891 rows
- 12 columns

**Remember:** `shape` returns the number of rows first and columns second.

This is useful because we should know the size of our dataset before starting analysis.

---

## 4. What Does the Dataset Look Like?

We can use the `head()` function to see the first five rows.

```python
df.head()
```

We can also see more rows:

```python
df.head(10)
```

To see the last five rows:

```python
df.tail()
```

### Why should we check the data?

Looking at the data helps us understand:
- What information is stored in the dataset.
- What each column contains.
- Whether values look correct.
- Whether there are unusual values.

### Random Sampling

Sometimes the first few rows do not represent the entire dataset.

For example, the first rows might contain passengers from one particular group.

To get a better overall idea, use `sample()`.

```python
df.sample(5)
```

This displays five randomly selected rows.

You can also use:

```python
df.sample(10, random_state=42)
```

`random_state=42` makes the random selection reproducible, so you can get the same sample again.

**Important:** Random sampling helps us avoid making assumptions based only on the first or last rows.

---

## 5. What Are the Data Types of Each Column?

**Question:** What type of data is stored in each column?

We can use the `info()` method.

```python
df.info()
```

It provides information such as:

- Column names.
- Number of non-null values.
- Data types.
- Memory usage.

### Common Pandas Data Types

| Data type | Meaning | Example |
|---|---|---|
| `int64` | Integer numbers | 25, 100 |
| `float64` | Decimal numbers | 25.5, 10.75 |
| `object` | Usually text or mixed values | "Male", "Female" |
| `bool` | True or False | True |
| `datetime64` | Date and time | 2026-11-10 |

### Why are data types important?

Sometimes a column contains numerical information but is stored using an inefficient data type.

For example:

```python
df["Age"].dtype
```

If a column contains whole numbers but is stored as `float64`, we may be able to convert it to an integer type after handling missing values.

Example:

```python
df["SomeColumn"] = df["SomeColumn"].astype("int32")
```

Only convert a column when its values are compatible with the new type.

### Memory Optimization

Large datasets can consume a lot of memory.

We can inspect memory usage with:

```python
df.info(memory_usage="deep")
```

Choosing suitable data types can reduce memory usage and sometimes improve processing performance.

For example, smaller integer types can be useful when the values fit within their supported ranges.

---

## 6. Are There Missing Values?

Missing values are values that are not available in the dataset.

Pandas usually represents missing values with `NaN` or `None`.

We can check missing values using:

```python
df.isnull()
```

This returns `True` for missing values and `False` for available values.

However, for a large dataset, checking every cell is not convenient.

### Count Missing Values in Each Column

```python
df.isnull().sum()
```

Example output:

```text
PassengerId      0
Survived         0
Pclass           0
Name             0
Age            177
Cabin          687
Embarked         2
```

This tells us how many missing values exist in each column.

### What Should We Do With Missing Values?

There are different ways to handle missing values.

**Option 1: Remove rows**

```python
df.dropna()
```

This removes rows containing missing values.

**Option 2: Fill missing values**

For numerical columns, we can use the mean or median.

```python
df["Age"] = df["Age"].fillna(df["Age"].median())
```

For categorical columns, we can use the mode.

```python
df["Embarked"] = df["Embarked"].fillna(
    df["Embarked"].mode()[0]
)
```

**Important:** Do not automatically delete or fill every missing value. First understand why the values are missing and how much data is affected.

---

## 7. How Does the Data Look Mathematically?

We can use the `describe()` method to get a statistical summary of numerical columns.

```python
df.describe()
```

It provides:

| Statistic | Meaning |
|---|---|
| `count` | Number of non-missing values |
| `mean` | Average value |
| `std` | Standard deviation |
| `min` | Minimum value |
| `25%` | First quartile |
| `50%` | Median |
| `75%` | Third quartile |
| `max` | Maximum value |

### Example: Age Column

```python
df["Age"].describe()
```

Suppose the output shows:

```text
count    714
mean      29.7
std       14.5
min        0.4
25%       20.1
50%       28.0
75%       38.0
max       80.0
```

This helps us understand the distribution of passenger ages.

### Understanding Quartiles

- **25%:** 25% of the available values are at or below this value.
- **50%:** The median. Half of the values are at or below it.
- **75%:** 75% of the values are at or below this value.

### Why Is `describe()` Useful?

It helps us identify:
- Unusually high or low values.
- Possible outliers.
- Differences in numerical values.
- The general distribution of data.

For categorical columns, use:

```python
df.describe(include="object")
```

This provides information such as the number of unique values and the most frequent value.

---

## 8. Are There Duplicate Rows?

Duplicate rows are repeated records in a dataset.

We can check them using:

```python
df.duplicated()
```

To count duplicate rows:

```python
df.duplicated().sum()
```

To display duplicate rows:

```python
df[df.duplicated()]
```

### Removing Duplicates

```python
df.drop_duplicates(inplace=True)
```

**Important:** Duplicate records do not always mean bad data. Sometimes two records can have the same values but represent two different real-world events.

Before removing duplicates, understand the dataset and decide whether those records are actually repeated.

---

## 9. Is There Any Correlation Between Columns?

Correlation tells us how two numerical variables move in relation to each other.

For example:
- When one variable increases, does another variable also increase?
- When one variable increases, does another variable decrease?
- Is there little or no linear relationship?

We can calculate correlation using:

```python
df.corr(numeric_only=True)
```

This calculates correlations between numerical columns.

### Understanding Correlation Values

Correlation values range from `-1` to `+1`.

| Correlation | Meaning |
|---|---|
| `+1` | Perfect positive correlation |
| Close to `+1` | Strong positive correlation |
| `0` | No linear correlation |
| Close to `-1` | Strong negative correlation |
| `-1` | Perfect negative correlation |

### Positive Correlation

When one variable increases, the other variable tends to increase.

Example:

If study hours increase, exam scores may also increase.

### Negative Correlation

When one variable increases, the other variable tends to decrease.

Example:

In the Titanic dataset, passenger class (`Pclass`) and survival can show a negative correlation when class is represented numerically.

Remember: In Titanic, `Pclass = 1` means first class, while `Pclass = 3` means third class.

### No or Weak Correlation

A correlation close to zero means there is little or no linear relationship between the two variables.

### Checking Correlation With the Target Column

In the Titanic dataset, `Survived` is the target column.

```python
df.corr(numeric_only=True)["Survived"].sort_values(
    ascending=False
)
```

This helps us explore how numerical columns are related to survival.

For example:
- `Pclass` may have a negative relationship with survival.
- `Fare` may have a positive relationship with survival.
- `PassengerId` may have almost no useful relationship with survival.

### Important Points About Correlation

1. Correlation does not prove causation.
2. Correlation mainly describes linear relationships when using the default Pearson method.
3. A correlation close to zero does not mean that no relationship of any kind exists.
4. Correlation between numerical columns does not automatically explain categorical relationships.
5. A feature with a weak correlation can still be useful to a Machine Learning model.

---

## 10. Quick Revision: First Questions to Ask About a Dataset

| Question | Pandas command |
|---|---|
| How many rows and columns? | `df.shape` |
| What does the data look like? | `df.head()` |
| What are random rows? | `df.sample(5)` |
| What are the data types? | `df.info()` |
| How much memory is used? | `df.info(memory_usage="deep")` |
| How many missing values? | `df.isnull().sum()` |
| What is the statistical summary? | `df.describe()` |
| How many duplicate rows? | `df.duplicated().sum()` |
| What is the correlation? | `df.corr(numeric_only=True)` |

---

## 11. Practice Tasks

Use the Titanic dataset and try these tasks yourself:

1. Load the Titanic CSV file using Pandas.
2. Find the total number of rows and columns.
3. Display the first 10 rows.
4. Display 5 random rows.
5. Check all column names and data types.
6. Find the number of missing values in each column.
7. Display the statistical summary of numerical columns.
8. Find the number of duplicate rows.
9. Calculate the correlation matrix.
10. Find the correlation of numerical columns with `Survived`.

---

## 12. Useful Documentation

- Pandas documentation: https://pandas.pydata.org/docs/
- `DataFrame.shape`: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html
- `DataFrame.info()`: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html
- `DataFrame.describe()`: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
- `DataFrame.isnull()`: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isnull.html
- `DataFrame.duplicated()`: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html
- `DataFrame.corr()`: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html

---

## Conclusion

Before applying Machine Learning algorithms, we should understand our dataset.

The first step is to inspect its size, structure, data types, missing values, statistical summary, duplicate rows, and correlations.

These basic checks help us understand the quality of our data and prepare it for further Exploratory Data Analysis (EDA).

**Next Topic:** Exploratory Data Analysis (EDA) and Univariate Analysis.
