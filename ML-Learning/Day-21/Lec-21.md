# Day 21: EDA Using Bivariate and Multivariate Analysis

## 1. What is Bivariate Analysis?

Bivariate Analysis means analyzing **two variables (columns) together** to understand their relationship.

For example:
- Does the total bill increase when the tip increases?
- Is there a relationship between passenger age and survival?
- Does passenger class affect survival?

It helps us discover patterns and relationships between two columns.

## 2. What is Multivariate Analysis?

Multivariate Analysis means analyzing **more than two variables together**.

For example, we can study:
- Total bill
- Tip amount
- Customer gender
- Whether the customer is a smoker
- Number of people in the group

We can display all this information in one visualization using different visual properties such as color, size, and shape.

## 3. Types of Bivariate Analysis

When selecting a plot, first check the data types of your two columns.

There are three main combinations:

1. Numerical vs Numerical
2. Numerical vs Categorical
3. Categorical vs Categorical

---

## 4. Scatter Plot (Numerical vs Numerical)

A Scatter Plot is used when both columns contain numerical values.

**Example:** Total bill and tip from the Tips dataset.

```python
sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.show()
```

- X-axis represents the total bill.
- Y-axis represents the tip.
- Each dot represents one customer or restaurant bill.

### What can we learn?

If the dots generally move upward from left to right, it suggests a positive relationship.

For example, customers who have higher bills often leave higher tips.

### Multivariate Analysis Using Scatter Plot

We can add more information using additional parameters:

| Parameter | Purpose |
|---|---|
| `hue` | Shows categories using different colors |
| `style` | Shows categories using different marker shapes |
| `size` | Represents values using different marker sizes |

Example:

```python
sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="sex",
    style="smoker",
    size="size"
)
```

This plot can show:
- Total bill
- Tip amount
- Customer gender
- Smoking status
- Number of people in the group

One graph can display information about multiple variables.

---

## 5. Bar Plot (Numerical vs Categorical)

A Bar Plot is useful when one column is categorical and the other is numerical.

It helps us compare a numerical value across different categories.

**Example:** Find the average age of passengers in each Titanic passenger class.

```python
sns.barplot(
    data=titanic,
    x="pclass",
    y="age"
)
plt.show()
```

- X-axis represents passenger class.
- Y-axis represents average passenger age.
- Each bar represents a category.

By default, Seaborn's bar plot displays the mean of the numerical values for each category.

### Multivariate Analysis Using Bar Plot

We can add another categorical variable using `hue`.

```python
sns.barplot(
    data=titanic,
    x="pclass",
    y="age",
    hue="sex"
)
```

This allows us to compare average passenger ages across classes and genders.

**Remember:** A bar plot normally displays an aggregate such as the mean. It does not display every individual observation.

---

## 6. Box Plot (Numerical vs Categorical)

A Box Plot compares the distribution of a numerical column across different categories.

It displays:
- Median
- First quartile (Q1)
- Third quartile (Q3)
- Interquartile range (IQR)
- Potential outliers

**Example:** Compare passenger ages by gender.

```python
sns.boxplot(
    data=titanic,
    x="sex",
    y="age"
)
plt.show()
```

We can also add another categorical variable using `hue`.

```python
sns.boxplot(
    data=titanic,
    x="sex",
    y="age",
    hue="survived"
)
```

This helps us compare age distributions across genders and survival groups.

### Why use a Box Plot?

A bar plot mainly compares an aggregate such as the mean.

A box plot gives more information about the distribution, spread, median, and potential outliers.

---

## 7. Dist Plot (Numerical vs Categorical)

A distribution plot helps us compare the distribution of a numerical variable across different categories.

**Example:** Compare the age distributions of passengers who survived and those who did not survive.

First, separate the two groups:

```python
not_survived = titanic[titanic["survived"] == 0]
survived = titanic[titanic["survived"] == 1]
```

Then plot their distributions:

```python
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

plt.legend()
plt.show()
```

### What is KDE?

KDE stands for **Kernel Density Estimation**.

It creates a smooth curve to represent the distribution of numerical data.

- X-axis represents the numerical variable.
- Y-axis represents estimated probability density.
- A higher curve indicates a greater concentration of observations around that value.

KDE does not show the exact probability of an individual value.

### Why use KDE?

It helps us compare how numerical values are distributed across different groups.

For example, we can investigate how age distributions differ between passengers who survived and those who did not.

---

## 8. Heatmap (Categorical vs Categorical)

A Heatmap is useful for visualizing relationships between two categorical variables.

First, we can create a cross-tabulation using Pandas.

**Example:** Compare passenger class and survival.

```python
result = pd.crosstab(
    titanic["pclass"],
    titanic["survived"]
)

print(result)
```

This produces a table showing the number of passengers in each combination of class and survival status.

Now visualize it:

```python
sns.heatmap(result, annot=True, fmt="d")
plt.show()
```

### Important Parameters

| Parameter | Purpose |
|---|---|
| `annot=True` | Displays values inside the cells |
| `fmt="d"` | Displays integer values |
| `cmap` | Changes the color palette |

### Why use a Heatmap?

Colors make it easier to identify high and low values.

However, raw counts can be misleading when categories have different numbers of observations.

For example, one passenger class may have more passengers than another.

To compare survival percentages, calculate normalized values:

```python
survival_percentage = pd.crosstab(
    titanic["pclass"],
    titanic["survived"],
    normalize="index"
) * 100

sns.heatmap(
    survival_percentage,
    annot=True,
    fmt=".1f"
)
plt.show()
```

This shows the percentage of passengers who survived or did not survive within each class.

---

## 9. ClusterMap (Categorical vs Categorical)

A ClusterMap is similar to a Heatmap, but it also groups rows and columns with similar patterns.

It uses hierarchical clustering to organize similar groups close to each other.

Example:

```python
sns.clustermap(
    result,
    annot=True,
    fmt="d"
)
plt.show()
```

### Why use ClusterMap?

- It helps identify similar patterns.
- It groups rows and columns based on similarity.
- It can make relationships easier to explore in larger datasets.

**Important:** Clustering shows similarity in the data. It does not automatically prove that two groups have a meaningful real-world relationship.

---

## 10. Pair Plot (Multiple Numerical Variables)

A Pair Plot creates a collection of plots for numerical columns.

It automatically compares each numerical variable with the other numerical variables.

For example, the Iris dataset contains:
- Sepal length
- Sepal width
- Petal length
- Petal width

```python
sns.pairplot(iris)
plt.show()
```

### How does it work?

- Scatter plots show relationships between different numerical columns.
- Diagonal plots show the distribution of individual columns.
- Each combination of numerical columns gets its own plot.

### Multivariate Analysis Using Pair Plot

We can use `hue` to display different categories using different colors.

```python
sns.pairplot(
    iris,
    hue="species"
)
plt.show()
```

This helps us compare the numerical measurements of different Iris species.

**Note:** Pair plots can become crowded and slow when a dataset contains many numerical columns.

---

## 11. Line Plot (Numerical vs Numerical with Time)

A Line Plot is useful when the X-axis contains time-based values, such as:
- Years
- Months
- Dates
- Time intervals

It helps us understand how a numerical value changes over time.

**Example:** Analyze yearly passenger numbers using the Flights dataset.

First, group passengers by year:

```python
yearly_data = flights.groupby("year")["passengers"].sum().reset_index()
```

Then create the line plot:

```python
sns.lineplot(
    data=yearly_data,
    x="year",
    y="passengers"
)

plt.show()
```

### What can we learn?

A Line Plot helps us identify:
- Increasing trends
- Decreasing trends
- Changes over time
- Seasonal or repeated patterns (when enough time-based data is available)

### Pivot Table

A Pivot Table helps us reorganize data into rows and columns.

For the Flights dataset:

```python
pivot_data = flights.pivot_table(
    values="passengers",
    index="month",
    columns="year"
)
```

Here:
- `values` contains the numerical data.
- `index` contains the row labels.
- `columns` contains the column labels.

### Heatmap of the Pivot Table

```python
sns.heatmap(pivot_data)
plt.show()
```

This makes it easier to compare passenger numbers across different months and years.

### ClusterMap of the Pivot Table

```python
sns.clustermap(pivot_data)
plt.show()
```

This can group months and years that have similar passenger patterns.

---

## 12. Quick Revision

| Plot | Data Combination | Main Purpose |
|---|---|---|
| Scatter Plot | Numerical vs Numerical | Show relationships between two numerical variables |
| Bar Plot | Numerical vs Categorical | Compare an aggregate, usually the mean, across categories |
| Box Plot | Numerical vs Categorical | Compare distributions and identify potential outliers |
| KDE / Dist Plot | Numerical vs Categorical | Compare numerical distributions |
| Heatmap | Categorical vs Categorical | Display values using colors |
| ClusterMap | Matrix of values | Group similar rows and columns |
| Pair Plot | Multiple numerical columns | Compare many numerical variables |
| Line Plot | Numerical vs Time | Show changes and trends over time |

## 13. Important Libraries

Install the required libraries:

```bash
pip install pandas matplotlib seaborn
```

Import them:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

## 14. Practice Tasks

1. Create a Scatter Plot using `total_bill` and `tip` from the Tips dataset.
2. Add `sex`, `smoker`, and `size` to the Scatter Plot.
3. Create a Bar Plot showing average age by passenger class.
4. Compare passenger age distributions using a Box Plot.
5. Compare survival and age distributions using KDE.
6. Create a Heatmap for passenger class and survival.
7. Calculate survival percentages for each passenger class.
8. Create a ClusterMap using the cross-tabulation.
9. Create a Pair Plot using the Iris dataset.
10. Create a Line Plot showing yearly passenger numbers using the Flights dataset.
11. Create a Pivot Table and visualize it using a Heatmap.

## 15. Documentation

- Pandas: https://pandas.pydata.org/docs/
- Seaborn: https://seaborn.pydata.org/
- Matplotlib: https://matplotlib.org/stable/
- Pandas `crosstab`: https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html
- Pandas `pivot_table`: https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html

## Final Summary

- **Bivariate Analysis:** Study two variables together.
- **Multivariate Analysis:** Study more than two variables together.
- Select a visualization according to the data types and the question you want to answer.
- Use color, size, and shape to display additional information.
- EDA helps us discover patterns, compare groups, and understand our data before building a Machine Learning model.
