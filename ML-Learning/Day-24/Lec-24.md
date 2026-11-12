# Day 24 – Feature Scaling: Standardization

## 1. What is Feature Scaling?

Feature Scaling is a data preprocessing technique used to bring independent features of a dataset into a similar scale.

A machine learning dataset usually contains:

- **Input Features (X):** The information used to make predictions.
- **Target Feature (y):** The output we want to predict.

### Example

Suppose we want to predict whether a customer will purchase a product.

| Age | Estimated Salary | Purchased |
|---:|---:|---:|
| 27 | 48,000 | 0 |
| 50 | 83,000 | 1 |
| 35 | 60,000 | 0 |
| 45 | 75,000 | 1 |

Here:

- Age is an input feature.
- Estimated Salary is an input feature.
- Purchased is the target feature.

Notice that Age contains relatively small values, while Estimated Salary contains much larger values.

Feature Scaling helps bring input features to a comparable scale.

**Important:** We normally apply feature scaling to input features (X), not the target column (y) in this classification example.

---

## 2. Why Do We Need Feature Scaling?

Some machine learning algorithms calculate distances between data points or use feature values during model optimization.

If one feature has much larger values than another, the larger-scale feature can dominate the calculation.

### Example: Age and Salary

Suppose we have two customers:

| Customer | Age | Salary |
|---|---:|---:|
| A | 27 | 48,000 |
| B | 50 | 83,000 |

Difference in Age:

\[
50-27=23
\]

Difference in Salary:

\[
83000-48000=35000
\]

The Euclidean Distance formula is:

\[
d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}
\]

Substituting the values:

\[
d=\sqrt{(50-27)^2+(83000-48000)^2}
\]

\[
d=\sqrt{23^2+35000^2}
\]

\[
d=\sqrt{529+1225000000}
\]

The squared salary difference is much larger than the squared age difference.

Therefore, salary dominates the distance calculation.

### Diagram: Distance Dominance

Imagine plotting Age on the X-axis and Salary on the Y-axis:

```text
        Salary
          |
  83000   |                         B
          |                        *
          |                       /
          |                      /
          |                     /
  48000   |          A         /
          |          *
          |
          |
          +-------------------------------- Age
                    27              50
```

The distance between these two points is influenced much more by the salary difference because salary has a much larger numerical scale.

**Why is this a problem?**

Algorithms such as KNN use distance calculations to find nearby data points.

If salary dominates the distance, the model may not give Age enough influence.

**Solution:** Apply Feature Scaling to bring both features to comparable scales.

---

## 3. Types of Feature Scaling

There are two commonly discussed types of Feature Scaling:

1. Standardization
2. Normalization

### A. Standardization

Standardization transforms data using its mean and standard deviation.

After standardization:

- Mean becomes approximately 0.
- Standard deviation becomes approximately 1.

### B. Normalization

Normalization transforms data into a specified range.

A common technique is Min-Max Scaling, which usually converts values into a range between 0 and 1.

**This lesson focuses on Standardization.**

---

## 4. What is Standardization?

Standardization is a Feature Scaling technique that transforms the values of a feature so that the transformed feature has:

- Mean approximately equal to 0.
- Standard deviation approximately equal to 1.

It is also commonly called **Z-score Normalization**.

### Standardization Formula

\[
z=\frac{x-\mu}{\sigma}
\]

Where:

- \(z\) = Standardized value
- \(x\) = Original value
- \(\mu\) = Mean of the feature
- \(\sigma\) = Standard deviation of the feature

### Understanding the Formula

The formula performs two operations:

1. Subtract the mean from every value.
2. Divide the result by the standard deviation.

In simple words:

- Subtracting the mean moves the center of the data to zero.
- Dividing by standard deviation adjusts the spread of the data.

### Example

Suppose the Age feature has:

- Mean = 32
- Standard Deviation = 10

One customer's Age is 50.

Applying the formula:

\[
z=\frac{50-32}{10}
\]

\[
z=\frac{18}{10}
\]

\[
z=1.8
\]

The standardized value of Age 50 is **1.8**.

This means that the original value is 1.8 standard deviations above the mean.

Another customer has Age 27:

\[
z=\frac{27-32}{10}
\]

\[
z=-0.5
\]

The standardized value is **-0.5**.

This means that the original value is half a standard deviation below the mean.

**Remember:** A negative standardized value does not mean the original value was negative. It means the value is below the mean.

---

## 5. Understanding Mean Centering

The first operation in Standardization is called **Mean Centering**.

Mean Centering means subtracting the mean from every value in a feature.

### Example

Suppose we have these Age values:

```text
Original Age:

10     20     30     40     50
 |------|------|------|------|
                ^
             Mean = 30
```

Subtract 30 from every value:

| Original Age | Age - Mean | New Value |
|---:|---:|---:|
| 10 | 10 - 30 | -20 |
| 20 | 20 - 30 | -10 |
| 30 | 30 - 30 | 0 |
| 40 | 40 - 30 | 10 |
| 50 | 50 - 30 | 20 |

After Mean Centering:

```text
       Negative Values       Positive Values

      -20    -10      0      10      20
       |------|-------|-------|-------|
                       ^
                    Mean = 0
```

The mean of the transformed values becomes zero.

### What Does Mean Centering Do?

- Moves the center of the data to zero.
- Keeps the relative distances between values unchanged.
- Does not change the overall shape of the distribution.

**Important:** Mean Centering alone does not make the standard deviation equal to 1. We need the second operation for that.

---

## 6. Understanding Standard Deviation Scaling

The second operation is dividing the mean-centered values by their standard deviation.

Standard deviation measures how spread out the values are around their mean.

### Understanding Standard Deviation Visually

Consider two features:

```text
Feature A: Small Spread

             *
           * * *
             *
             |
-------------0----------------


Feature B: Large Spread

       *       *       *
           *       *
             *
             |
-------------0----------------
```

Feature A has values concentrated close to its mean.

Feature B has values spread over a larger range.

Their standard deviations are different.

### What Happens During Standardization?

Suppose:

- Mean of Age = 32
- Standard Deviation of Age = 6
- Mean of Salary = 50,000
- Standard Deviation of Salary = 20,000

After standardization, both features are centered around zero and have a standard deviation of approximately one.

```text
BEFORE STANDARDIZATION

Age                         Salary

   *                           *
  ***                          *
 *****                         *
  ***                          *
   *                           *
----------------       -------------------
Small numerical scale      Large numerical scale


AFTER STANDARDIZATION

Age                         Salary

        *                           *
      *****                       *****
    *********                   *********
      *****                       *****
        *                           *
----------------       -------------------
Mean = 0                  Mean = 0
SD = 1                    SD = 1
```

The diagram shows the concept, not exact data distributions.

### Two Main Operations of Standardization

1. Mean Centering: Move the mean to zero.
2. Standard Deviation Scaling: Adjust the spread so that standard deviation becomes one.

---

## 7. Geometric Intuition of Standardization

Geometric intuition means understanding how the data points look on a graph before and after a transformation.

Suppose we have 500 customers and two features:

- Age
- Estimated Salary

### Before Standardization

Age and Salary have different scales.

```text
               Salary
                 |
                 |       *  *   *
                 |    *  * * * *
                 |  * * * * * *
                 |    * * * *
                 |      * *
                 |
                 |
                 +---------------------- Age
```

The salary axis has a much larger numerical range.

The data may look stretched differently along the two axes.

### Step 1: Mean Centering

First, subtract the mean of each feature.

Both feature means become zero.

```text
             Salary
               |
       * * *   |
     * * * *   |
   * * * * *   |
-------------0---------------- Age
   * * * * *
     * * *
       *
```

The center of the data moves to the origin (0, 0).

### Step 2: Standard Deviation Scaling

Next, divide each mean-centered feature by its standard deviation.

```text
             Standardized Salary
                    |
                * * *
              * * * * *
             * * * * * *
              * * * * *
                * * *
                    |
--------------------0---------------- Standardized Age
```

The spread of each feature is adjusted to a comparable scale.

**Important:** Standardization does not make every data point identical. It changes the center and scale of each feature while generally preserving its distribution shape.

---

## 8. Does Standardization Change the Distribution?

No. Standardization generally changes the location and scale of a distribution, not its overall shape.

For example:

- A right-skewed distribution remains right-skewed.
- A left-skewed distribution remains left-skewed.
- A normally distributed feature remains normally distributed after standardization.

### Diagram: Before and After

```text
BEFORE STANDARDIZATION

Frequency
   |
   |             *
   |           * * *
   |         * * * * *
   |       * * * * * * *
   |________________________ Value


AFTER STANDARDIZATION

Frequency
   |
   |             *
   |           * * *
   |         * * * * *
   |       * * * * * * *
   |________________________ Z-score
```

The distribution shape is shown as similar, but the horizontal scale and center change.

---

## 9. Applying Standardization Using Scikit-Learn

Python provides a class called `StandardScaler` in Scikit-Learn.

### Import

```python
from sklearn.preprocessing import StandardScaler
```

### Create an Object

```python
scaler = StandardScaler()
```

### Fit the Scaler

```python
scaler.fit(X_train)
```

The `fit()` method calculates and stores:

- Mean of each training feature.
- Standard deviation of each training feature.

### Transform the Data

```python
X_train_scaled = scaler.transform(X_train)
```

The `transform()` method applies the standardization formula.

### Use fit_transform()

We can combine both operations:

```python
X_train_scaled = scaler.fit_transform(X_train)
```

This calculates the statistics and transforms the training data.

---

## 10. Understanding fit(), transform() and fit_transform()

These three methods are important.

| Method | Purpose |
|---|---|
| `fit()` | Learns mean and standard deviation |
| `transform()` | Applies the learned scaling |
| `fit_transform()` | Learns and transforms in one step |

### Workflow Diagram

```text
                 Original Dataset
                        |
                        |
                  Train-Test Split
                        |
              +---------+---------+
              |                   |
          Training Data        Testing Data
              |                   |
              |                   |
        scaler.fit()               |
              |                   |
      Learns Mean and SD           |
              |                   |
       fit_transform()             |
              |                   |
       Scaled Training Data        |
                                  |
                           scaler.transform()
                                  |
                           Scaled Testing Data
```

### Important Rule: Avoid Data Leakage

Always split the dataset before fitting the scaler.

Correct approach:

```python
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)
```

Incorrect approach:

```python
# Do not fit the scaler on the complete dataset
# before splitting into training and testing data.

X_scaled = scaler.fit_transform(X)
```

Why?

Because the test data should not influence the statistics learned from training data.

If we use the complete dataset to calculate the mean and standard deviation, information from the test set leaks into the training process.

This is called **Data Leakage**.

Remember:

- Fit on training data.
- Transform training data.
- Transform testing data using the same fitted scaler.

---

## 11. Why Does StandardScaler Return a NumPy Array?

When we apply:

```python
X_train_scaled = scaler.fit_transform(X_train)
```

Scikit-Learn returns a NumPy array instead of a Pandas DataFrame.

To convert it back into a DataFrame:

```python
X_train_scaled = pd.DataFrame(
    X_train_scaled,
    columns=X_train.columns,
    index=X_train.index
)
```

Now we can easily view the column names and use Pandas functions.

### Check the Mean

```python
print(X_train_scaled.mean())
```

The mean should be approximately zero.

### Check the Standard Deviation

```python
print(X_train_scaled.std())
```

The standard deviation should be close to one.

**Technical note:** `StandardScaler` uses population standard deviation (`ddof=0`). Pandas `std()` uses sample standard deviation (`ddof=1`) by default. Therefore, the displayed result may be slightly different from exactly 1.

---

## 12. Does Standardization Affect Outliers?

This is an important concept.

An outlier is a value that is unusually far from the other observations.

StandardScaler uses:

- Mean
- Standard deviation

Both can be affected by extreme values.

### Example

Suppose we have these salary values:

```text
20,000
25,000
30,000
35,000
40,000
500,000
```

The value 500,000 is much larger than the other values.

### Diagram: Salary With an Outlier

```text
Salary Values

20k   25k   30k   35k   40k                         500k
 |-----|-----|-----|-----|----------------------------*
                         Normal Values                Outlier
```

Because StandardScaler uses the mean and standard deviation, this extreme value can affect the scaling of all observations.

### Important Points

- StandardScaler does not remove outliers.
- It does not automatically handle extreme values.
- Outliers can still remain far from the center after standardization.

### What Can We Use Instead?

One alternative is `RobustScaler`.

It uses:

- Median
- Interquartile Range (IQR)

These statistics are less sensitive to extreme values.

Example:

```python
from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()

X_scaled = scaler.fit_transform(X_train)
```

**Remember:** StandardScaler is not an outlier-removal technique.

---

## 13. Does Standardization Always Improve Model Performance?

Not necessarily.

The effect of standardization depends on the machine learning algorithm and dataset.

Some algorithms are sensitive to feature scales, while others are generally not.

### Example: KNN

KNN calculates distances between data points.

If one feature has a much larger scale, it can dominate the distance calculation.

Therefore, standardization is usually important for KNN.

### Example: Logistic Regression

Logistic Regression is commonly trained using optimization techniques such as Gradient Descent.

Different feature scales can affect the optimization process.

Standardization can help make optimization more stable and efficient.

### Example: Comparing Accuracy

Suppose we train two KNN models:

- Model 1: Uses original data.
- Model 2: Uses standardized data.

We can compare their accuracy.

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Model without scaling
model1 = KNeighborsClassifier(n_neighbors=5)

model1.fit(X_train, y_train)

pred1 = model1.predict(X_test)

print("Without Scaling:")
print(accuracy_score(y_test, pred1))


# Model with scaling
model2 = KNeighborsClassifier(n_neighbors=5)

model2.fit(X_train_scaled, y_train)

pred2 = model2.predict(X_test_scaled)

print("With Scaling:")
print(accuracy_score(y_test, pred2))
```

The accuracy may improve after standardization, but the result depends on the data.

**Important:** Scaling does not guarantee better accuracy for every model.

---

## 14. Algorithms Where Standardization Is Important

Standardization is commonly useful for algorithms that:

- Calculate distances.
- Use gradient-based optimization.
- Are sensitive to feature magnitudes.

| Algorithm | Is Scaling Important? | Reason |
|---|---|---|
| KNN | Yes | Uses distance calculations |
| K-Means | Yes | Uses distance calculations |
| SVM | Yes | Sensitive to feature scales |
| PCA | Yes | Depends on feature variance |
| Logistic Regression | Usually yes | Helps optimization |
| Linear Regression | Often useful | Helps numerical optimization |
| Neural Networks | Usually yes | Helps training and optimization |
| Gradient Descent-based Models | Usually yes | Helps optimization |

### Why PCA Needs Standardization

PCA identifies directions of maximum variance.

If one feature has a much larger scale, it may dominate the variance calculation.

Standardization helps prevent features from dominating only because of their measurement units.

---

## 15. Algorithms Where Scaling Is Usually Not Required

Some algorithms are generally less sensitive to feature scales.

Examples:

- Decision Tree
- Random Forest
- Extra Trees
- Many Gradient Boosting Tree Models

### Why?

Tree-based algorithms make decisions using conditions such as:

```text
Is Age <= 30?
Is Salary <= 50,000?
```

They split data based on feature values and their ordering.

Changing a feature's scale generally does not change the ordering of its values.

Therefore, scaling is usually unnecessary for these models.

**Note:** Scaling can still be useful in some complete pipelines, but it is not normally required for tree-based models.

---

## 16. When Should You Use Standardization?

Consider Standardization when:

1. You are using KNN or K-Means.
2. You are using SVM.
3. You are applying PCA.
4. You are training Logistic Regression.
5. You are training Neural Networks.
6. Your model uses Gradient Descent.
7. Your input features have very different numerical scales.

### Quick Decision Diagram

```text
              Machine Learning Model
                         |
                         |
             Does it use distances,
             gradients or variance?
                         |
                  +------+------+
                  |             |
                 YES            NO
                  |             |
                  |        Is it a tree-based
                  |            model?
                  |             |
           Consider Scaling     |
                                |
                         Usually No Scaling
                         Required
```

Always check the requirements of the specific algorithm and preprocessing pipeline.

---

## 17. Standardization vs Normalization

| Standardization | Normalization |
|---|---|
| Uses mean and standard deviation | Min-Max Scaling uses minimum and maximum |
| Mean becomes approximately 0 | Values commonly fall between 0 and 1 |
| Standard deviation becomes approximately 1 | Does not guarantee a standard deviation of 1 |
| Can produce negative values | Min-Max Scaling commonly produces values from 0 to 1 |
| Uses `StandardScaler` | Uses `MinMaxScaler` |

### Standardization Formula

\[
z=\frac{x-\mu}{\sigma}
\]

### Min-Max Normalization Formula

\[
x'=\frac{x-x_{\min}}{x_{\max}-x_{\min}}
\]

We will study Normalization in the next lesson.

---

## 18. Important Points to Remember

1. Feature Scaling brings input features to a comparable scale.
2. It is important for many distance-based and gradient-based algorithms.
3. Standardization uses mean and standard deviation.
4. The formula is \(z=(x-\mu)/\sigma\).
5. Mean Centering moves the mean to zero.
6. Dividing by standard deviation adjusts the spread.
7. After standardization, mean is approximately 0 and standard deviation is approximately 1.
8. Standardization generally preserves the distribution shape.
9. StandardScaler does not remove outliers.
10. Fit the scaler only on training data.
11. Use the same fitted scaler to transform testing data.
12. Tree-based models generally do not require feature scaling.

---

## 19. Practice Tasks

Try these tasks yourself:

1. Load the Social Network Ads dataset.
2. Select Age and EstimatedSalary as input features.
3. Display the original mean and standard deviation.
4. Apply train-test split.
5. Create a StandardScaler object.
6. Fit the scaler on training data.
7. Transform training and testing data.
8. Display the standardized values.
9. Check whether the mean is approximately zero.
10. Check whether the standard deviation is approximately one.
11. Draw scatter plots before and after standardization.
12. Compare KNN accuracy with and without scaling.
13. Add an extreme salary value and observe its effect.
14. Try RobustScaler and compare the results.

---

## 20. Useful Documentation

- Scikit-Learn StandardScaler: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html
- Scikit-Learn Preprocessing: https://scikit-learn.org/stable/modules/preprocessing.html
- Scikit-Learn Data Leakage: https://scikit-learn.org/stable/common_pitfalls.html

---

## Quick Revision

**Feature Scaling:** Bringing input features to a comparable scale.

**Standardization:** Transforming features using mean and standard deviation.

**Mean Centering:** Subtracting the mean from each value.

**Standard Deviation Scaling:** Dividing mean-centered values by standard deviation.

**Z-score:** The standardized value of an observation.

**StandardScaler:** Scikit-Learn class used for standardization.

**Data Leakage:** When information from testing data influences the training process.

**RobustScaler:** A scaling technique based on median and IQR, useful when outliers are present.

**Final Takeaway:** Standardization changes the center and spread of a feature, making its scale more suitable for machine learning algorithms that are sensitive to feature magnitudes.
