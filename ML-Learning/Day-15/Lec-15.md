# Day 15: Working with CSV Files in Data Science 🚀

> **Context:** In Machine Learning, data collection is the first practical step. Most real-world datasets come in **CSV (Comma-Separated Values)** format. This guide covers how to efficiently load, parse, and handle CSV files using Python and Pandas.

---

## 1. What is a CSV File?
* **CSV** stands for **Comma-Separated Values**.
* It is a plain text file where each row represents a data record, and individual values in that row are separated by commas (`,`).
* It is the most popular data format for tabular data in Machine Learning because it is lightweight and easy to read.

---

## 2. Basic Loading (`pd.read_csv`)

To load a CSV file into a Pandas DataFrame, we use the `pd.read_csv()` function. You can load files stored locally on your machine or directly from an online server/URL.

---

## 3. Master Parameters of `pd.read_csv()`

Real-world CSV files are often messy. Pandas provides built-in parameters to handle almost every edge case:

### 1. `sep` (Separator / Delimiter)
* **What it does:** By default, Pandas looks for commas. If your file uses tabs (`.tsv`), semicolons, or pipes (`|`), you must change this parameter.
* **Example:** `pd.read_csv('file.tsv', sep='\t')`

### 2. `names` (Custom Column Headers)
* **What it does:** If your CSV file does not have header names in the first row, you can pass a custom list of column names manually.
* **Example:** `pd.read_csv('file.csv', names=['ID', 'Name', 'Score'])`

### 3. `header`
* **What it does:** Tells Pandas which row contains the column headers. Use `header=0` for the first row, or `header=None` if there are no headers.

### 4. `index_col`
* **What it does:** Sets an existing column as the DataFrame index instead of the default auto-generated integer numbers (0, 1, 2...).
* **Example:** `pd.read_csv('file.csv', index_col='Student_ID')`

### 5. `usecols`
* **What it does:** Loads only specific columns instead of the entire dataset, which saves system memory (RAM).
* **Example:** `pd.read_csv('file.csv', usecols=['Name', 'CGPA'])`

### 6. `skiprows` & `nrows`
* **`skiprows`:** Skips specific row numbers when loading the file.
* **`nrows`:** Loads only a limited number of rows (great for testing code on giant files quickly).

### 7. `encoding`
* **What it does:** Fixes character reading errors when handling files with special symbols or non-standard text (e.g., `encoding='utf-8'` or `encoding='latin-1'`).

### 8. `on_bad_lines`
* **What it does:** Skips corrupted rows that contain extra commas or missing values so your code doesn't crash.
* **Example:** `pd.read_csv('file.csv', on_bad_lines='skip')`

### 9. `dtype`
* **What it does:** Forces specific data types on columns during loading to save RAM and optimize performance.
* **Example:** `pd.read_csv('file.csv', dtype={'Placed': int})`

### 10. `parse_dates`
* **What it does:** Automatically converts date columns from plain text (strings) into proper `datetime64` objects so you can perform time-series operations.
* **Example:** `pd.read_csv('file.csv', parse_dates=['Join_Date'])`

### 11. `na_values`
* **What it does:** Converts custom missing placeholders (like `?`, `-`, `N/A`) into true `NaN` (Not a Number) missing values.
* **Example:** `pd.read_csv('file.csv', na_values=['?', 'N/A', '-'])`

### 12. `chunksize`
* **What it does:** Reads giant datasets in smaller batches (chunks) instead of loading everything into RAM at once, preventing memory crashes.
* **Example:** 
  ```python
  for chunk in pd.read_csv('huge_file.csv', chunksize=5000):
      print(chunk.shape)

  4. Modern Industry Update (2027 Context)
While CSV is standard for learning and small tasks, modern enterprise pipelines use Apache Parquet (.parquet) formats. Parquet files are compressed, store data types natively, and read up to 10x faster than CSV files.
