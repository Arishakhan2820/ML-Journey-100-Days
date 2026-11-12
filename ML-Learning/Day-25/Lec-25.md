# Day 25: Feature Scaling – Normalization

**Topics:** MinMaxScaler | Mean Normalization | MaxAbsScaler | RobustScaler

## 1. What is Feature Scaling?

Feature scaling is a data preprocessing technique used in Machine Learning.

It changes the scale or range of numerical features so that features with different units or ranges can be compared more fairly.

### Example

Imagine a dataset containing two features:

| Feature | Example values |
|---|---:|
| Age | 18–60 |
| Salary | 20,000–200,000 |

Salary values are much larger than age values. Some Machine Learning algorithms may give more importance to features with larger numerical values.

Feature scaling helps reduce this problem.

**Main purpose:** Bring numerical features to a suitable scale without unnecessarily changing the information they represent.

## 2. Why is Feature Scaling Important?

Some Machine Learning algorithms are sensitive to the scale of features.

Feature scaling can help algorithms such as:

- K-Nearest Neighbors (KNN)
- K-Means Clustering
- Support Vector Machines (SVM)
- Logistic Regression
- Linear Regression with regularization
- Principal Component Analysis (PCA)
- Neural Networks

Algorithms based on decision trees, such as Decision Trees and Random Forests, generally do not require feature scaling.

### Important points

- Features may have different units, such as kilograms, centimeters, and rupees.
- Large numerical ranges can influence distance-based algorithms.
- Scaling can improve optimization and model performance.
- Scaling does not automatically improve every model.

## 3. What is Normalization?

Normalization is a type of feature scaling.

It transforms numerical values into a different scale, often a fixed range such as 0 to 1.

There are different normalization techniques. In this lesson, we will study:

1. MinMax Scaling
2. Mean Normalization
3. MaxAbs Scaling
4. Robust Scaling

## 4. MinMax Scaling

MinMax Scaling is one of the most commonly used normalization techniques.

It transforms values into a specified range. By default, Scikit-learn uses the range **0 to 1**.

### Formula

\[
X_{scaled} = \frac{X-X_{min}}{X_{max}-X_{min}}
\]

Where:

- \(X\) = Original value
- \(X_{min}\) = Minimum value of the feature
- \(X_{max}\) = Maximum value of the feature
- \(X_{scaled}\) = Transformed value

### Example

Suppose we have the following weight values:

`[32, 60, 67, 130]`

Minimum value = 32

Maximum value = 130

For the value 67:

\[
X_{scaled} = \frac{67-32}{130-32}
\]

\[
X_{scaled} = \frac{35}{98} = 0.357
\]

The transformed values will be approximately:

| Original value | Scaled value |
|---:|---:|
| 32 | 0.000 |
| 60 | 0.286 |
| 67 | 0.357 |
| 130 | 1.000 |

### Diagram: MinMax Scaling

The original values are transformed into the 0–1 range.

```text
Original values:

32       60       67                    130
|--------|--------|----------------------|
Minimum                              Maximum


After MinMax Scaling:

0.00     0.286    0.357                 1.00
|--------|--------|----------------------|
Minimum                              Maximum
```

### Geometrical intuition

Imagine that your data points are spread across a large rectangular area.

MinMax Scaling compresses each feature into a fixed range between 0 and 1.

<escape>```text
Before Scaling                 After Scaling

  Height                          1.0
    |                              |
    |       •                      |    •
    |   •                          | •
    |             •                |         •
    | •                            | •
    +---------- Weight             +---------- Weight
      Large range                    0 to 1
```</escape>

### Python implementation

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

X_scaled = scaler.fit_transform(X)
```

### Advantages

- Easy to understand and use.
- Converts features into a fixed range.
- Useful when a model expects values within a specific range.
- Commonly used in image processing, where pixel values can be scaled from 0–255 to 0–1.

### Disadvantage

MinMax Scaling is sensitive to outliers.

If a feature contains an extremely large or small value, most other values may become compressed into a small portion of the 0–1 range.

### When should you use it?

Use MinMax Scaling when:

- You need values within a known range.
- Your data does not contain extreme outliers.
- You are working with image data or algorithms that benefit from bounded inputs.

## 5. Mean Normalization

Mean Normalization transforms values by subtracting the feature mean and dividing by the feature's range.

### Formula

\[
X_{scaled} = \frac{X-\mu}{X_{max}-X_{min}}
\]

Where:

- \(X\) = Original value
- \(\mu\) = Mean of the feature
- \(X_{max}\) = Maximum value
- \(X_{min}\) = Minimum value

### How does it work?

- First, calculate the mean.
- Subtract the mean from every value.
- Divide the result by the difference between maximum and minimum values.

Values below the mean become negative.

Values above the mean become positive.

The mean becomes zero after transformation.

### Diagram

```text
Values below mean       Mean       Values above mean

      Negative           0              Positive

---------|---------------|------------------->
       -1               0                  +1
```

The output is not guaranteed to be between -1 and +1.

### Python implementation

Scikit-learn does not provide a dedicated `MeanNormalization` scaler, but we can implement it using Pandas:

```python
X_mean_scaled = (X - X.mean()) / (X.max() - X.min())
```

### When should you use it?

Mean Normalization can be useful when you want to center values around zero while scaling them by their range.

It is less commonly used than StandardScaler in many Machine Learning workflows.

**Important:** Mean Normalization and Standardization are not the same thing.

## 6. MaxAbs Scaling

MaxAbs Scaling divides every value by the maximum absolute value of its feature.

It usually transforms values into the range -1 to +1.

### Formula

\[
X_{scaled} = \frac{X}{|X|_{max}}
\]

Where:

- \(X\) = Original value
- \(|X|_{max}\) = Maximum absolute value in the feature

### Example

Suppose the values are:

`[-10, -5, 0, 5, 10]`

Maximum absolute value = 10

After MaxAbs Scaling:

`[-1, -0.5, 0, 0.5, 1]`

### Diagram

```text
Original range:

-10       -5        0        5        10
 |---------|--------|--------|---------|


Scaled range:

 -1      -0.5       0       0.5        1
 |---------|--------|--------|---------|
```

### Python implementation

```python
from sklearn.preprocessing import MaxAbsScaler

scaler = MaxAbsScaler()

X_scaled = scaler.fit_transform(X)
```

### Advantages

- Preserves zero values.
- Does not shift or center the data.
- Useful for sparse datasets.
- Works with both positive and negative values.

### Disadvantage

It is sensitive to outliers because the maximum absolute value determines the scaling factor.

### When should you use it?

Use MaxAbs Scaling when:

- Your dataset contains many zero values.
- You are working with sparse matrices.
- You want to preserve zero values.
- You do not want to center the data.

## 7. Robust Scaling

Robust Scaling is useful when your dataset contains outliers.

Unlike MinMax Scaling, it uses the median and interquartile range (IQR).

### Formula

\[
X_{scaled} = \frac{X-\text{Median}}{IQR}
\]

Where:

\[
IQR = Q3-Q1
\]

- Median = 50th percentile
- Q1 = 25th percentile
- Q3 = 75th percentile
- IQR = Difference between Q3 and Q1

### Example

Suppose:

- Median = 50
- Q1 = 30
- Q3 = 70
- Original value = 60

First, calculate IQR:

\[
IQR = 70-30=40
\]

Now apply Robust Scaling:

\[
X_{scaled} = \frac{60-50}{40}
\]

\[
X_{scaled}=0.25
\]

### Diagram: Robust Scaling

```text
Dataset with an outlier:

10   20   30   40   50   60   70                 500
                       ^
                     Median

Q1 = 30
Median = 50
Q3 = 70
IQR = 40
```

Robust Scaling uses the median and IQR, which are less affected by extreme values than the mean and range.

### Python implementation

```python
from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()

X_scaled = scaler.fit_transform(X)
```

### Advantages

- Less affected by extreme outliers.
- Uses median and IQR instead of minimum and maximum.
- Useful for datasets with skewed distributions and unusual extreme values.

### Important point

Robust Scaling does not remove outliers. It only reduces their influence on the scaling calculation.

### When should you use it?

Use Robust Scaling when:

- Your dataset contains many outliers.
- Minimum and maximum values are not representative of the main data.
- You want scaling that is less sensitive to extreme values.

## 8. Normalization vs Standardization

These two terms are often confused.

**Normalization** generally transforms values into a selected range or uses another normalization formula.

**Standardization** transforms data using its mean and standard deviation.

### Standardization formula

\[
Z = \frac{X-\mu}{\sigma}
\]

Where:

- \(X\) = Original value
- \(\mu\) = Mean
- \(\sigma\) = Standard deviation

After standardization:

- Mean is approximately 0.
- Standard deviation is approximately 1.
- Values are not restricted to a fixed range.

### Comparison

| Technique | Main calculation | Typical output |
|---|---|---|
| MinMax Scaling | Minimum and maximum | 0 to 1 |
| Mean Normalization | Mean and range | Centered around 0 |
| MaxAbs Scaling | Maximum absolute value | -1 to 1 |
| Robust Scaling | Median and IQR | No fixed range |
| Standardization | Mean and standard deviation | Mean 0, standard deviation 1 |

### Practical selection guide

```text
Need feature scaling?
        |
        v
Choose a suitable method
        |
        +---- Need a fixed 0 to 1 range?
        |          |
        |          +---- MinMaxScaler
        |
        +---- Need to preserve zero values?
        |          |
        |          +---- MaxAbsScaler
        |
        +---- Dataset contains strong outliers?
        |          |
        |          +---- RobustScaler
        |
        +---- Want mean 0 and standard deviation 1?
        |          |
        |          +---- StandardScaler
        |
        +---- Want mean-centered range scaling?
                   |
                   +---- Mean Normalization
```

## 9. Important Rules for Feature Scaling

### Rule 1: Split the data first

Always split your dataset into training and testing sets before fitting a scaler.

### Rule 2: Fit only on training data

Use `fit()` or `fit_transform()` on training data only.

### Rule 3: Transform both datasets

Use the same fitted scaler to transform training and testing data.

### Correct workflow

```text
          Original Dataset
                 |
                 v
          Train-Test Split
             /       \
            v         v
       Training     Testing
            |
            v
       Fit Scaler
            |
            v
      Transform Train
            |
            +----------------+
                             |
                             v
                    Transform Test
                    using the same
                    fitted scaler
```

Why is this important?

If you calculate scaling values using the complete dataset, information from the testing set can leak into the training process. This is called **data leakage**.

### Rule 4: Scale numerical features

Do not blindly scale every column.

- Numerical features: Usually consider scaling.
- Categorical features: Use appropriate encoding techniques.
- Target column: Do not scale it automatically; it depends on the problem.

### Rule 5: Experiment with different scalers

No single scaling technique is best for every dataset.

Test suitable methods and compare model performance using the same evaluation approach.

## 10. Quick Revision

| Technique | Uses | Best suited for |
|---|---|---|
| MinMaxScaler | Min and max | Fixed range |
| Mean Normalization | Mean and range | Centering with range scaling |
| MaxAbsScaler | Maximum absolute value | Sparse data |
| RobustScaler | Median and IQR | Outliers |
| StandardScaler | Mean and standard deviation | Many scale-sensitive algorithms |

## 11. Practice Tasks

1. Create a small dataset with different numerical ranges.
2. Apply MinMaxScaler.
3. Apply Mean Normalization manually.
4. Apply MaxAbsScaler.
5. Apply RobustScaler.
6. Compare the minimum and maximum values before and after scaling.
7. Add an extreme outlier and observe how MinMaxScaler and RobustScaler behave.
8. Use the Wine dataset and compare the Alcohol and Malic Acid features.
9. Split the data before fitting the scaler.
10. Compare a Machine Learning model with and without feature scaling.

## 12. Important Documentation

- [Scikit-learn: Preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html)
- [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html)
- [MaxAbsScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html)
- [RobustScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html)
- [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)

**Final Reminder:** Feature scaling changes the numerical scale of features. It does not mean that the original data is being deleted or that outliers are automatically removed.
