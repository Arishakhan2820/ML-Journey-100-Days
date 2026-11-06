# Day 16 — Working with JSON and SQL in Machine Learning

**Topic:** Working with JSON and SQL  
**Learning Track:** Machine Learning  
**Level:** Beginner

## 1. Introduction

In Machine Learning, data can come from different sources, not only CSV files.

Common data sources include:

- JSON files
- APIs
- SQL databases
- CSV and Excel files

Before training a Machine Learning model, we need to collect, read, filter, and convert data into a usable format.

**Typical ML workflow:**

JSON / API / SQL Database → Python → Pandas DataFrame → Data Cleaning → Data Preprocessing → ML Model

---

## 2. What is JSON?

JSON stands for **JavaScript Object Notation**.

It is a lightweight data format used to store and exchange information between different programming languages.

Although JSON was originally derived from JavaScript, it is supported by Python, Java, C++, PHP, and many other languages.

### Why is JSON popular?

- It is easy to read and understand.
- It is lightweight.
- It supports different data types.
- It is widely used in APIs.
- Different programming languages can understand it.

### JSON Example

```json
{
    "name": "Ayesha",
    "age": 22,
    "city": "Karachi",
    "skills": ["Python", "SQL", "Machine Learning"],
    "is_student": true
}
```

### JSON Data Types

| JSON Type | Example | Python Equivalent |
|---|---|---|
| Object | {"name": "Ayesha"} | Dictionary |
| Array | [10, 20, 30] | List |
| String | "Python" | String |
| Number | 22 | Integer |
| Boolean | true / false | True / False |
| Null | null | None |

**Important:** JSON uses lowercase `true`, `false`, and `null`, whereas Python uses `True`, `False`, and `None`.

---

## 3. Working with JSON in Python

Python provides a built-in module called `json`.

We can use it to read and write JSON files.

### A. Import JSON

```python
import json
```

### B. Reading a JSON File

Python provides `json.load()` to read JSON data from a file.

```python
import json

with open("students.json", "r") as file:
    data = json.load(file)

print(data)
```

### C. Writing JSON Data

We can use `json.dump()` to save Python data into a JSON file.

```python
import json

student = {
    "name": "Ayesha",
    "age": 22,
    "city": "Karachi"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
```

### D. Difference Between load() and loads()

- `json.load()` reads JSON from a file.
- `json.loads()` reads JSON from a string.
- `json.dump()` writes JSON into a file.
- `json.dumps()` converts Python data into a JSON string.

---

## 4. Reading JSON with Pandas

Pandas provides a function called `read_json()`.

It works similarly to `read_csv()`.

```python
import pandas as pd

df = pd.read_json("recipes.json")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
```

### Important Pandas Functions

| Function | Purpose |
|---|---|
| `pd.read_json()` | Reads JSON into a DataFrame |
| `df.head()` | Displays first 5 rows |
| `df.tail()` | Displays last 5 rows |
| `df.shape` | Returns rows and columns |
| `df.columns` | Displays column names |
| `df.info()` | Displays DataFrame information |
| `df.describe()` | Shows statistical information |

**Note:** `read_json()` works directly with compatible JSON structures. Nested JSON may need `pd.json_normalize()`.

### Reading Nested JSON

```python
import pandas as pd

data = [
    {
        "name": "Ayesha",
        "address": {
            "city": "Karachi",
            "country": "Pakistan"
        }
    }
]

df = pd.json_normalize(data)

print(df)
```

---

## 5. Reading JSON from an API URL

JSON is commonly used in APIs.

An API allows different applications to communicate and exchange data.

Python can retrieve JSON data from an API using the Requests library.

Install Requests:

```bash
python -m pip install requests
```

Example:

```python
import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url, timeout=20)

response.raise_for_status()

data = response.json()

df = pd.json_normalize(data)

print(df.head())
```

**Important methods:**

- `requests.get()` sends an HTTP GET request.
- `response.json()` converts the JSON response into Python data.
- `pd.json_normalize()` converts nested JSON records into tabular data.
- `raise_for_status()` checks whether the HTTP request succeeded.

Some APIs require authentication or have request limits.

---

## 6. What is SQL?

SQL stands for **Structured Query Language**.

It is used to communicate with relational databases.

SQL allows us to:

- Retrieve data.
- Filter records.
- Sort data.
- Insert records.
- Update records.
- Delete records.
- Create database tables.

### Popular SQL Databases

1. MySQL
2. PostgreSQL
3. SQLite
4. Microsoft SQL Server

### Database Structure

A relational database stores data in tables.

Example: Students Table

| ID | Name | City | Marks |
|---|---|---|---|
| 1 | Ayesha | Karachi | 88 |
| 2 | Sara | Lahore | 76 |
| 3 | Hamza | Karachi | 91 |
| 4 | Zain | Islamabad | 69 |

- **Table:** Collection of related records.
- **Row:** One complete record.
- **Column:** A particular field.
- **Database:** Collection of organized data.

---

## 7. Important SQL Commands

### A. SELECT

Retrieves data from a table.

```sql
SELECT * FROM students;
```

`*` means all columns.

To retrieve specific columns:

```sql
SELECT name, marks
FROM students;
```

### B. WHERE

Filters records based on a condition.

```sql
SELECT *
FROM students
WHERE city = 'Karachi';
```

### C. ORDER BY

Sorts the results.

```sql
SELECT *
FROM students
ORDER BY marks DESC;
```

- ASC = Ascending order
- DESC = Descending order

### D. LIMIT

Restricts the number of returned records.

```sql
SELECT *
FROM students
LIMIT 5;
```

### E. COUNT()

Counts records.

```sql
SELECT COUNT(*)
FROM students;
```

### F. AVG()

Calculates an average.

```sql
SELECT AVG(marks)
FROM students;
```

### G. GROUP BY

Groups records based on a particular column.

```sql
SELECT city, COUNT(*)
FROM students
GROUP BY city;
```

### H. Other Useful Functions

```sql
SELECT MAX(marks) FROM students;

SELECT MIN(marks) FROM students;

SELECT SUM(marks) FROM students;
```

---

## 8. Connecting Python with SQL

Python can communicate with databases using database connector libraries.

The connector acts as a bridge between Python and the database.

**Basic workflow:**

Python → Database Connector → SQL Database → SQL Query → Pandas DataFrame

There are different connectors for different databases.

Examples:

- SQLite: `sqlite3`
- MySQL: `mysql-connector-python`
- PostgreSQL: `psycopg`

---

## 9. SQLite Database Connection

SQLite is a lightweight database included with Python.

It does not require a separate database server.

```python
import sqlite3

connection = sqlite3.connect("practice.db")

print("Database connected successfully!")

connection.close()
```

Here:

- `sqlite3.connect()` creates or connects to a database.
- `connection` stores the database connection object.
- `connection.close()` closes the connection.

---

## 10. Connecting Python with MySQL

The video demonstrates MySQL using XAMPP and phpMyAdmin.

### Step 1: Install XAMPP

Download and install XAMPP.

### Step 2: Start Services

Open XAMPP Control Panel and start:

- Apache
- MySQL

### Step 3: Open phpMyAdmin

Open:

`http://localhost/phpmyadmin`

### Step 4: Create a Database

Create a new database, for example:

`world`

You can import a sample SQL database containing tables such as:

- city
- country
- countrylanguage

### Step 5: Install MySQL Connector

```bash
python -m pip install mysql-connector-python
```

### Step 6: Import Libraries

```python
import mysql.connector
import pandas as pd
```

### Step 7: Create Connection

```python
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="world"
)

print("Connected successfully!")
```

**Note:** The username and password depend on your MySQL configuration. A blank password is not guaranteed.

Never upload database credentials to GitHub.

---

## 11. Reading SQL Data into Pandas

Pandas provides `read_sql_query()`.

It executes a SQL query and converts the returned data into a DataFrame.

```python
query = "SELECT * FROM city"

df = pd.read_sql_query(query, connection)

print(df.head())
```

### Reading Specific Columns

```python
query = """
SELECT Name, CountryCode, Population
FROM city
"""

df = pd.read_sql_query(query, connection)

print(df.head())
```

### Filtering SQL Data

To retrieve cities from India:

```python
query = """
SELECT *
FROM city
WHERE CountryCode = 'IND'
"""

df = pd.read_sql_query(query, connection)

print(df)
```

### Filtering Countries by Life Expectancy

```python
query = """
SELECT Name, LifeExpectancy
FROM country
WHERE LifeExpectancy > 60
"""

df = pd.read_sql_query(query, connection)

print(df)
```

### Using Parameters Safely

For SQLite:

```python
country_code = "IND"

query = """
SELECT Name, CountryCode, Population
FROM city
WHERE CountryCode = ?
"""

df = pd.read_sql_query(
    query,
    connection,
    params=(country_code,)
)
```

Parameterized queries help prevent SQL injection. Placeholder syntax differs between database drivers.

---

## 12. Important Pandas SQL Function Options

`pd.read_sql_query()` supports useful options.

| Parameter | Purpose |
|---|---|
| `sql` | SQL query |
| `con` | Database connection |
| `index_col` | Column to use as DataFrame index |
| `params` | Query parameters |
| `chunksize` | Read data in smaller chunks |
| `parse_dates` | Convert selected columns into dates |

Example:

```python
df = pd.read_sql_query(
    "SELECT * FROM city",
    connection,
    chunksize=1000
)
```

When `chunksize` is provided, the result is an iterator of DataFrame chunks rather than one complete DataFrame.

---

## 13. JSON vs SQL

| JSON | SQL |
|---|---|
| Data exchange format | Database query language |
| Often used with APIs | Used with relational databases |
| Stores objects and arrays | Retrieves and manages table data |
| Read using `json` or Pandas | Queries using SQL |
| Supports nested structures | Organizes data into tables |

JSON and SQL can work together in the same project.

---

## 14. Importance of JSON and SQL in Machine Learning

Machine Learning requires data from different sources.

Example: A house-price prediction project.

1. Collect house information from an API.
2. Receive the data in JSON format.
3. Convert JSON into a Pandas DataFrame.
4. Retrieve historical house data from SQL.
5. Filter relevant records using SQL queries.
6. Clean the data using Pandas.
7. Perform preprocessing.
8. Train a Machine Learning model.

Therefore, JSON and SQL are important data-access skills for ML engineers and data scientists.

---

## 15. Important Takeaways

- JSON stands for JavaScript Object Notation.
- JSON is commonly used for data exchange and APIs.
- Python's `json` module reads and writes JSON.
- `pd.read_json()` converts compatible JSON data into a DataFrame.
- SQL stands for Structured Query Language.
- SQL is used to communicate with relational databases.
- `SELECT` retrieves records.
- `WHERE` filters records.
- `ORDER BY` sorts records.
- `GROUP BY` groups records.
- `pd.read_sql_query()` loads SQL query results into Pandas.
- Database connectors allow Python to communicate with databases.
- SQLite is useful for local practice.
- JSON and SQL help collect data for Machine Learning projects.

---

## 16. Practice Questions

1. What is JSON?
2. Why is JSON used in APIs?
3. What is the difference between JSON and Python dictionaries?
4. What is the difference between `json.load()` and `json.loads()`?
5. What does `pd.read_json()` do?
6. What is SQL?
7. What is the difference between a row and a column?
8. What is the purpose of SELECT?
9. What is the purpose of WHERE?
10. What is the difference between ASC and DESC?
11. What does GROUP BY do?
12. What is a database connector?
13. What does `pd.read_sql_query()` do?
14. Why do we convert database data into a Pandas DataFrame?
15. How are JSON and SQL useful in Machine Learning?

---

## 17. Documentation and Learning Resources

- Pandas JSON: https://pandas.pydata.org/docs/reference/api/pandas.read_json.html
- Pandas SQL: https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html
- Python JSON: https://docs.python.org/3/library/json.html
- Python SQLite: https://docs.python.org/3/library/sqlite3.html
- MySQL Connector: https://dev.mysql.com/doc/connector-python/en/

**End of Day 16 — Working with JSON and SQL**
