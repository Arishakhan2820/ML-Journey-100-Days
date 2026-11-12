# Day 23 – What is Feature Engineering?

## 1. Introduction

Until now, we have learned how to:
- Collect data.
- Perform basic data analysis.
- Understand and explore datasets using EDA.

Now, the next important step in Machine Learning is **Feature Engineering**.

Feature Engineering helps us prepare and improve our data before giving it to a Machine Learning algorithm.

## 2. What is Feature Engineering?

Feature Engineering is the process of using domain knowledge to create, transform, or select useful features from raw data to improve the performance of Machine Learning models.

A **feature** is an input column in a dataset.

For example, a house dataset may contain:
- Number of rooms
- Number of bathrooms
- Area
- Price

Raw data is not always ready for a Machine Learning algorithm. We may need to clean it, transform it, or create new columns.

This process is called Feature Engineering.

### Why is Feature Engineering Important?

- It helps improve model performance.
- It makes data more useful for algorithms.
- It can remove unnecessary information.
- It can create meaningful features from existing columns.
- It can make model training faster by reducing unnecessary features.

Feature Engineering requires problem-solving skills and domain knowledge. There is no single technique that works for every dataset.

A good set of features can sometimes help a simple algorithm perform better than a powerful algorithm with poor features.

## 3. Main Types of Feature Engineering

Feature Engineering can be broadly divided into four categories:

1. Feature Transformation
2. Feature Construction
3. Feature Selection
4. Feature Extraction

---

## 4. Feature Transformation

Feature Transformation means changing an existing feature into another format or scale so that it becomes more useful for a Machine Learning algorithm.

Important techniques include:

### A. Missing Value Imputation

Real-world datasets often contain missing values.

Missing values can occur because:
- A person did not provide information.
- Data collection failed.
- Information was not recorded.

Many Machine Learning algorithms cannot directly work with missing values.

We can handle missing values in different ways:

**1. Remove missing values**

If only a very small number of rows contain missing values, we may remove those rows when appropriate.

**2. Mean Imputation**

Replace missing numerical values with the mean.

Example:

```python
df["Age"] = df["Age"].fillna(df["Age"].mean())
```

**3. Median Imputation**

Replace missing numerical values with the median.

```python
df["Age"] = df["Age"].fillna(df["Age"].median())
```

**4. Mode Imputation**

Replace missing categorical values with the most frequent value.

```python
df["Embarked"] = df["Embarked"].fillna(
    df["Embarked"].mode()[0]
)
```

The correct method depends on the dataset and problem.

### B. Handling Categorical Values

Categorical columns contain labels instead of numerical values.

Example:

| Animal |
|---|
| Dog |
| Cat |
| Lion |
| Dog |

Many Machine Learning algorithms require numerical input.

One technique is **One-Hot Encoding**.

It creates separate columns for categories.

Example:

| Animal | Dog | Cat | Lion |
|---|---:|---:|---:|
| Dog | 1 | 0 | 0 |
| Cat | 0 | 1 | 0 |
| Lion | 0 | 0 | 1 |

Python:

```python
pd.get_dummies(df["Animal"])
```

Another technique is **Ordinal Encoding**, which assigns numbers to categories that have a meaningful order.

Example:

| Education | Level |
|---|---:|
| School | 1 |
| College | 2 |
| University | 3 |

Do not assign arbitrary numbers to unordered categories because a model may interpret them as having a numerical relationship.

### C. Binning

Binning converts numerical values into groups or categories.

Example: Age

| Age | Age Group |
|---:|---|
| 8 | Child |
| 18 | Teenager |
| 30 | Adult |
| 60 | Senior |

Python:

```python
bins = [0, 12, 19, 45, 100]

labels = ["Child", "Teenager", "Adult", "Senior"]

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=bins,
    labels=labels
)
```

Binning can make numerical information easier to understand, but it also reduces some detail.

### D. Outlier Detection

An outlier is a value that is very different from most other values.

Example:

```text
Class marks: 45, 50, 55, 60, 98
```

If most students scored around 45–60, the value 98 is unusually high compared with the others.

Outliers can affect some Machine Learning algorithms.

One common method for detecting outliers is the **IQR method**.

Formula:

```text
IQR = Q3 - Q1

Lower Limit = Q1 - 1.5 × IQR

Upper Limit = Q3 + 1.5 × IQR
```

Values outside these limits are potential outliers.

Important: An outlier is not always an error. It should be investigated before removing it.

### E. Feature Scaling

Feature Scaling brings numerical features onto comparable scales.

Example:

| Age | Salary |
|---:|---:|
| 25 | 30000 |
| 30 | 50000 |
| 40 | 80000 |

Age has smaller values, while Salary has much larger values.

Algorithms based on distance, such as K-Nearest Neighbors (KNN), can be affected by differences in feature scales.

Two common techniques are:

**1. Standardization**

Transforms values using mean and standard deviation.

```text
z = (x - mean) / standard deviation
```

The transformed feature generally has a mean near 0 and standard deviation near 1.

Python:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaled_data = scaler.fit_transform(df[["Age", "Salary"]])
```

**2. Normalization (Min-Max Scaling)**

Usually scales values into a range between 0 and 1.

```text
x_scaled = (x - minimum) / (maximum - minimum)
```

Python:

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

scaled_data = scaler.fit_transform(df[["Age", "Salary"]])
```

The choice depends on the data and algorithm.

Other transformations include Log Transformation and Box-Cox Transformation.

---

## 5. Feature Construction

Feature Construction means creating completely new features using existing columns.

It depends on:
- Domain knowledge
- Experience
- Understanding of the dataset
- Problem-solving skills

### Example: Titanic Dataset

The Titanic dataset contains:

- `SibSp`: Number of siblings or spouses aboard.
- `Parch`: Number of parents or children aboard.

We can combine these columns to create a new feature called `Family_Size`.

Formula:

```text
Family Size = SibSp + Parch + 1
```

We add 1 for the passenger.

Python:

```python
df["Family_Size"] = df["SibSp"] + df["Parch"] + 1
```

We can also create a new categorical feature:

```python
df["Family_Type"] = df["Family_Size"].apply(
    lambda x: "Alone" if x == 1
    else "Small Family" if x <= 4
    else "Large Family"
)
```

This new feature may provide useful information to a Machine Learning model.

---

## 6. Feature Selection

Feature Selection means selecting the most useful features from the existing columns and removing features that are less useful.

### Why is Feature Selection Important?

- Reduces the number of input features.
- Can improve model performance.
- Can reduce training time.
- Can make a model easier to understand.
- Can help reduce unnecessary information.

### Example: Image Dataset

An image can be converted into numerical pixel values.

For example, an image of size 28 × 28 contains:

```text
28 × 28 = 784 pixels
```

Each pixel can become a feature.

But not every pixel may be equally useful for recognizing a digit.

Feature Selection tries to identify useful existing features and remove less useful ones.

Some Feature Selection techniques include:
- Forward Selection
- Backward Elimination
- Statistical tests such as SelectKBest

Feature Selection keeps selected original features.

---

## 7. Feature Extraction

Feature Extraction creates a new set of features from the original features.

It is different from Feature Selection.

### Example: Real Estate Dataset

Suppose a dataset contains:

- Number of rooms
- Number of bathrooms
- House price

We may combine the room-related information into a new feature, such as estimated area, when the required information and assumptions are available.

The new feature can represent the information in a different way.

### Example: PCA

PCA stands for **Principal Component Analysis**.

It is a popular dimensionality reduction technique.

PCA:
- Creates new features called principal components.
- Combines information from existing numerical features.
- Tries to preserve as much variation in the data as possible.
- Can reduce the number of dimensions.

For example, if a dataset has 10 numerical features, PCA may transform them into 2 or 3 principal components.

These components are new features, not simply selected original columns.

---

## 8. Feature Selection vs Feature Extraction

| Feature Selection | Feature Extraction |
|---|---|
| Selects existing features | Creates new features |
| Removes less useful columns | Transforms original information |
| Keeps original feature meaning | New features may have different meanings |
| Example: SelectKBest | Example: PCA |

## 9. Complete Feature Engineering Summary

| Category | Meaning | Examples |
|---|---|---|
| Feature Transformation | Changes existing features | Imputation, encoding, binning, outlier handling, scaling |
| Feature Construction | Creates new features from existing data | Family Size |
| Feature Selection | Selects useful existing features | Forward Selection, SelectKBest |
| Feature Extraction | Creates new features from existing features | PCA |

## 10. Important Points to Remember

1. Feature Engineering prepares data for Machine Learning.
2. A feature is an input column.
3. Missing values should be handled before model training when the chosen algorithm requires complete values.
4. Categorical values may need encoding.
5. Binning converts numerical values into groups.
6. Outliers should be investigated before removal.
7. Feature Scaling is important for many distance-based algorithms.
8. Feature Construction creates new meaningful columns.
9. Feature Selection keeps useful existing columns.
10. Feature Extraction creates new features from existing information.
11. PCA is a popular Feature Extraction technique.
12. Feature Engineering depends on the dataset and problem.

## 11. Practice Tasks

1. Load the Titanic dataset using Pandas or Seaborn.
2. Check missing values in each column.
3. Fill missing Age values using the median.
4. Convert Sex into numerical columns using One-Hot Encoding.
5. Create a Family_Size column.
6. Create an Age_Group column using binning.
7. Detect potential outliers in Fare using the IQR method.
8. Apply StandardScaler to numerical features.
9. Try SelectKBest for Feature Selection.
10. Apply PCA to scaled numerical features.

## 12. Useful Documentation

- Pandas: https://pandas.pydata.org/docs/
- Scikit-learn: https://scikit-learn.org/stable/
- StandardScaler: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html
- OneHotEncoder: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html
- PCA: https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html

**Final Reminder:** Feature Engineering is an important part of Machine Learning. Good features can help a model learn useful patterns from data.
