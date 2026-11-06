# Day 17: Fetching Data From an API

## 1. What is an API?

API stands for **Application Programming Interface**.

An API allows two different software applications to communicate and exchange data with each other.

### Simple Example

Imagine you book a railway ticket through different platforms:

- IRCTC website
- MakeMyTrip
- Yatra

All these platforms can show train and seat availability.

But the railway database belongs to IRCTC. How can another platform access this information?

Through an **API**.

IRCTC provides an API that allows authorized applications to request information. The API returns the requested data.

### Simple Definition

An API is a way for two software applications to communicate and share information.

Think of an API as a bridge between two applications.

---

## 2. How Does an API Work?

The basic API communication process has four steps:

1. A client sends a request to an API.
2. The API processes the request.
3. The server sends a response.
4. The client receives and uses the response.

### Example

Suppose we want to get information about movies.

- Our Python program sends a request.
- The movie API receives the request.
- The API gets movie information from its database.
- The API returns the data in JSON format.
- Python converts that data into a Pandas DataFrame.

### API Workflow

Python Program → API Request → Server → API Response → JSON Data → Pandas DataFrame

---

## 3. What is an API Request?

An API request is a message sent from one application to another to ask for information or perform an action.

For example, we can request:

- Movie information
- Weather information
- User details
- Product information
- Stock prices

An API usually provides an endpoint (URL) where we send our request.

### Example Endpoint

`https://api.themoviedb.org/3/movie/top_rated`

This endpoint provides information about top-rated movies.

An API may also require an API key for authentication.

---

## 4. What is an API Key?

An API key is a unique value used by an API provider to identify and authorize an application.

Some APIs require an API key before allowing access to their data.

For example, TMDB requires authentication to access its movie data.

**Important:** Never upload your private API key to GitHub. Store it in an environment variable or a `.env` file.

---

## 5. What is JSON in API Responses?

Most APIs return data in JSON format.

JSON stands for **JavaScript Object Notation**.

It stores information using key-value pairs, similar to a Python dictionary.

Example:

```json
{
    "id": 101,
    "title": "Example Movie",
    "release_date": "2025-01-10",
    "vote_average": 8.5
}
```

In Python, we can convert an API response into JSON using:

```python
response.json()
```

The returned JSON data can be handled like Python dictionaries and lists.

---

## 6. Important Python Libraries

We will use two main libraries.

### A. Requests

The `requests` library is used to send HTTP requests to APIs.

Install it:

```bash
pip install requests
```

Example:

```python
import requests

url = "https://api.example.com/data"

response = requests.get(url)

print(response.status_code)
```

### B. Pandas

Pandas is used to organize and analyze data in DataFrame format.

Install it:

```bash
pip install pandas
```

Example:

```python
import pandas as pd

data = [
    {"name": "Ali", "age": 22},
    {"name": "Sara", "age": 24}
]

df = pd.DataFrame(data)

print(df)
```

---

## 7. Understanding API Responses

When we send a request, the server returns a response.

We should check its status code to understand whether the request was successful.

| Status Code | Meaning |
|---|---|
| 200 | Request successful |
| 201 | Resource created |
| 400 | Bad request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Resource not found |
| 429 | Too many requests |
| 500 | Internal server error |

Example:

```python
response = requests.get(url)

if response.status_code == 200:
    print("Request successful")
else:
    print("Something went wrong")
```

We can also use:

```python
response.raise_for_status()
```

It raises an error if the response contains an unsuccessful HTTP status code.

---

## 8. Converting API Data into a Pandas DataFrame

After receiving JSON data, we can convert it into a DataFrame.

Example JSON-like Python data:

```python
data = [
    {"name": "Ali", "age": 22},
    {"name": "Sara", "age": 24},
    {"name": "Ahmed", "age": 21}
]
```

Convert it:

```python
df = pd.DataFrame(data)

print(df)
```

Output:

| | name | age |
|---|---|---|
| 0 | Ali | 22 |
| 1 | Sara | 24 |
| 2 | Ahmed | 21 |

Now we can use Pandas functions:

```python
df.head()
df.shape
df.info()
df.columns
df.describe()
```

---

## 9. Practical Project: Fetching Movie Data From TMDB API

In this lesson, we use the **TMDB (The Movie Database) API** to create our own movie dataset.

### Step 1: Create a TMDB Account

1. Visit https://www.themoviedb.org/
2. Create an account or log in.
3. Open your account settings.
4. Find the API section.
5. Apply for API access and obtain your API key.

Keep your API key private.

### Step 2: Select the API Endpoint

We will use the top-rated movies endpoint:

`https://api.themoviedb.org/3/movie/top_rated`

It returns information about top-rated movies.

### Step 3: Send an API Request

We use `requests.get()` to send a request.

```python
response = requests.get(url, params=params)
```

The API returns a response containing movie information.

### Step 4: Convert the Response into JSON

```python
data = response.json()
```

The response contains information such as:

- page
- results
- total_pages
- total_results

The `results` key contains a list of movie dictionaries.

### Step 5: Understand the Movie Data

Each movie contains several fields.

| Field | Description |
|---|---|
| id | Unique movie ID |
| title | Movie title |
| release_date | Movie release date |
| overview | Movie description |
| popularity | Popularity score |
| vote_average | Average rating |
| vote_count | Number of votes |

We select only the columns that we need.

### Step 6: Convert Movie Data into a DataFrame

```python
df = pd.DataFrame(data["results"])
```

We can select specific columns:

```python
df = df[
    [
        "id",
        "title",
        "release_date",
        "overview",
        "popularity",
        "vote_average",
        "vote_count"
    ]
]
```

Now our movie information is organized in a DataFrame.

---

## 10. What is API Pagination?

Sometimes an API returns data in multiple pages instead of returning everything at once.

This is called **pagination**.

For example:

- Page 1 contains 20 movies.
- Page 2 contains the next 20 movies.
- Page 3 contains another 20 movies.

We can request different pages by passing a page number.

Example:

```python
params = {
    "api_key": API_KEY,
    "page": 1
}
```

To fetch the next page:

```python
params = {
    "api_key": API_KEY,
    "page": 2
}
```

### Why Do We Need Pagination?

Fetching a large amount of data in one request can be difficult or inefficient.

Pagination allows us to collect data in smaller parts.

### Using a Loop

Instead of sending requests manually, we can use a loop:

```python
for page in range(1, total_pages + 1):
    # Fetch data from each page
    pass
```

For each page:

1. Send an API request.
2. Receive the JSON response.
3. Extract the movie results.
4. Convert them into a temporary DataFrame.
5. Add the data to the main DataFrame.

The final DataFrame contains movies collected from all requested pages.

**Important:** Do not assume the total number of pages will always be the same. Read `total_pages` from the API response.

---

## 11. Combining Multiple DataFrames

We can combine multiple DataFrames using:

```python
pd.concat()
```

Example:

```python
df1 = pd.DataFrame([
    {"name": "Ali", "age": 22}
])

df2 = pd.DataFrame([
    {"name": "Sara", "age": 24}
])

final_df = pd.concat(
    [df1, df2],
    ignore_index=True
)

print(final_df)
```

`ignore_index=True` creates a fresh index for the combined DataFrame.

This is useful when we fetch data page by page.

---

## 12. Exporting the Dataset to CSV

After collecting the data, we can save it as a CSV file.

```python
df.to_csv("movies.csv", index=False)
```

### What does `index=False` mean?

It prevents Pandas from saving the DataFrame index as an extra column.

Now we have our own movie dataset in CSV format.

We can use this dataset for:

- Data analysis
- Data visualization
- Machine Learning projects
- Recommendation systems
- Portfolio projects

---

## 13. Why is Fetching API Data Important in Machine Learning?

Machine Learning models need data for training and testing.

Sometimes datasets are not available as ready-made CSV files.

APIs allow us to collect data directly from online services.

Examples:

- Weather API → Weather prediction projects
- Movie API → Movie recommendation systems
- Sports API → Sports data analysis
- Financial API → Financial data analysis
- News API → Text classification projects

API data can be collected, cleaned, transformed and then used in Machine Learning.

---

## 14. Important Things to Remember

1. API stands for Application Programming Interface.
2. APIs allow different applications to communicate.
3. Requests is used to send HTTP requests.
4. `requests.get()` sends a GET request.
5. `response.status_code` tells us the request status.
6. `response.json()` converts a JSON response into Python data.
7. `pd.DataFrame()` converts suitable structured data into a DataFrame.
8. Pagination helps fetch data from multiple pages.
9. `pd.concat()` combines multiple DataFrames.
10. `to_csv()` saves a DataFrame as a CSV file.
11. API keys should be kept private.
12. Always check API limits and error responses.

---

## 15. Practice Questions

1. What is an API?
2. Why do applications use APIs?
3. What is an API endpoint?
4. What is an API key?
5. What is the purpose of the Requests library?
6. What does `response.json()` do?
7. What is the difference between JSON and a Pandas DataFrame?
8. What is pagination?
9. Why do we use `pd.concat()`?
10. How can we save API data into a CSV file?

## 16. Practice Tasks

- Create a TMDB account and obtain your own API key.
- Fetch top-rated movies using Python.
- Display the first five movies.
- Select the seven movie columns discussed in this lesson.
- Fetch data from multiple pages.
- Combine all pages into one DataFrame.
- Export the final dataset to `movies.csv`.

## 17. Useful Documentation

- Requests: https://requests.readthedocs.io/
- Pandas: https://pandas.pydata.org/docs/
- TMDB API: https://developer.themoviedb.org/docs
- Python JSON: https://docs.python.org/3/library/json.html

**Day 17 Complete — Fetching Data From an API**
