# Day 22: Pandas Profiling

## 1. What is Pandas Profiling?

Pandas Profiling is a tool that automatically generates a detailed report about a dataset.

In normal EDA, we manually check:
- Number of rows and columns
- Data types
- Missing values
- Duplicate rows
- Statistical information
- Data distributions
- Correlations between columns

Pandas Profiling performs many of these checks automatically and displays the results in an interactive HTML report.

It saves time and helps us understand a dataset before starting Machine Learning.

**Important:** The modern name of this library is `ydata-profiling`. Older tutorials may use the name `pandas-profiling`.

## 2. Install the Library

Open your terminal and run:

```bash
pip install ydata-profiling
```

We also need Pandas:

```bash
pip install pandas
```

If you are using Jupyter Notebook, you can run installation commands in a notebook cell by adding `!` before the command.

## 3. Import the Required Libraries

```python
import pandas as pd
from ydata_profiling import ProfileReport
```

- `pandas` is used to work with datasets.
- `ProfileReport` creates an automatic profiling report.

## 4. Load Your Dataset

For this lesson, we will use the Titanic dataset.

```python
import seaborn as sns

df = sns.load_dataset("titanic")
```

You can also load your own CSV file:

```python
df = pd.read_csv("titanic.csv")
```

## 5. Generate a Profiling Report

Create a report using `ProfileReport`.

```python
profile = ProfileReport(df)

profile.to_file("titanic_report.html")
```

Here is what happens:

1. `ProfileReport(df)` analyzes the dataset.
2. It creates a profiling report.
3. `to_file()` saves the report as an HTML file.

After running the code, a file named `titanic_report.html` will be created in your project folder.

Open this file in your browser to explore the report.

## 6. Main Sections of the Report

The profiling report contains several important sections.

### A. Overview

The Overview section provides general information about the dataset.

It includes:

- Number of variables (columns)
- Number of observations (rows)
- Missing cells
- Missing cell percentage
- Duplicate rows
- Duplicate row percentage
- Total memory size
- Average record size
- Variable types

It may also display warnings about possible data-quality problems.

For example:
- A column may contain many missing values.
- A column may contain too many unique values.
- A variable may have a high percentage of zeros.

These warnings help us identify columns that need further investigation.

### B. Variables

The Variables section provides information about every individual column.

For example, in the Titanic dataset:

- `survived`
- `pclass`
- `sex`
- `age`
- `fare`
- `embarked`

For categorical variables, the report can display:

- Number of unique values
- Most frequent values
- Frequency of each category
- Missing values
- Sample values

For numerical variables, it can display:

- Minimum value
- Maximum value
- Mean
- Median
- Standard deviation
- Percentiles
- Histogram
- Distribution information
- Potential outliers

You can open a variable to explore more detailed information.

### C. Interactions

The Interactions section helps us explore relationships between two variables.

For example:

- Age and Fare
- Fare and Passenger Class
- Age and Passenger Class

It can display plots that help us understand how two variables interact.

This is useful for Bivariate Analysis.

### D. Correlations

The Correlations section shows the correlation between numerical variables.

Correlation helps us understand how two numerical variables move in relation to each other.

For example:
- A positive correlation means two variables tend to increase together.
- A negative correlation means one variable tends to decrease when the other increases.
- A correlation near zero indicates little or no linear relationship.

Pearson correlation ranges from -1 to +1.

**Important:** Correlation does not prove causation. A strong correlation does not mean one variable causes the other.

The report may provide different correlation methods, such as Pearson and Spearman, depending on the configuration.

### E. Missing Values

The Missing Values section shows how many values are missing in each column.

It can include:
- Missing values count
- Missing values percentage
- Missing values matrix
- Missing values charts

For example, if the Age column contains many missing values, we may need to investigate how to handle them.

Possible approaches include:
- Removing rows
- Filling missing values with the mean
- Filling missing values with the median
- Using the most frequent value for categorical columns

The correct approach depends on the dataset and the problem.

### F. Sample

The Sample section displays sample rows from the dataset.

It can show:
- First rows
- Last rows

This gives us a quick look at the actual data.

## 7. Important Advantages

Pandas Profiling is useful because:

1. It automates many basic EDA tasks.
2. It saves time.
3. It provides detailed information about every column.
4. It helps identify missing values and duplicates.
5. It provides statistical summaries and visualizations.
6. It helps discover possible data-quality problems.
7. It creates an HTML report that can be opened and shared.

## 8. Important Limitations

Although Pandas Profiling is powerful, it does not replace manual EDA.

Remember:

- It does not automatically clean your dataset.
- It does not decide how missing values should be handled.
- It does not guarantee that every warning is a real problem.
- It does not understand the complete business meaning of your data.
- Large datasets may take more time and memory to analyze.

Always read the report and investigate important findings yourself.

## 9. Quick Revision

| Section | What It Shows |
|---|---|
| Overview | General dataset information |
| Variables | Details about individual columns |
| Interactions | Relationships between two variables |
| Correlations | Correlation between variables |
| Missing Values | Missing data information |
| Sample | First and last rows of the dataset |

## 10. Practice Tasks

1. Install `ydata-profiling`.
2. Load the Titanic dataset.
3. Generate a profiling report.
4. Save the report as an HTML file.
5. Open the report in your browser.
6. Check the number of rows and columns.
7. Identify columns with missing values.
8. Find categorical and numerical variables.
9. Explore the Age and Fare distributions.
10. Check the correlation section.
11. Write down at least five observations about the dataset.
12. Repeat the same process with another dataset.

## 11. Documentation

- YData Profiling Documentation: https://docs.profiling.ydata.ai/
- Pandas Documentation: https://pandas.pydata.org/docs/
- Seaborn Documentation: https://seaborn.pydata.org/

## Final Summary

Pandas Profiling is an automated EDA tool that generates a detailed HTML report from a dataset.

Instead of manually checking every column, we can use `ProfileReport()` to get information about:

- Dataset overview
- Variables
- Interactions
- Correlations
- Missing values
- Sample rows

**Remember:** Use automated profiling to understand your dataset faster, but always investigate the results yourself before building a Machine Learning model.
