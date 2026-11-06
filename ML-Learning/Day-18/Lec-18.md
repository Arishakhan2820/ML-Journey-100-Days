# Day 18: Fetching Data Using Web Scraping

## 1. What is Web Scraping?

Web scraping is the process of automatically collecting information from websites using code.

We use web scraping when the required data is available on a website but there is no API available to access it.

### Simple Example

Suppose we want to collect information about different companies:

- Company name
- Company rating
- Number of reviews
- Headquarters
- Company age
- Number of employees
- Company type
- Company description

Instead of visiting every company page and copying the information manually, we can write a Python program to collect it automatically.

**Simple Definition:** Web scraping means extracting useful information from website pages using a program.

---

## 2. API vs Web Scraping

| API | Web Scraping |
|---|---|
| Gets data through an API endpoint | Extracts data from website HTML |
| Usually returns structured data like JSON | Usually starts with HTML |
| Uses libraries like Requests | Uses Requests and BeautifulSoup |
| Often easier to work with | Requires understanding HTML structure |
| Requires API access or permission | Requires permission to access and collect website content |

**Important:** If a website provides an API, prefer using the API. Web scraping is useful when an API is unavailable and website access is permitted.

---

## 3. Python Libraries Used for Web Scraping

We will use three main libraries.

### A. Requests

Requests is used to send HTTP requests and download webpage content.

Install:

```bash
pip install requests
```

Example:

```python
import requests

url = "https://example.com"

response = requests.get(url, timeout=15)

print(response.status_code)
print(response.text)
```

- `requests.get()` sends a GET request.
- `response.status_code` returns the HTTP status code.
- `response.text` contains the webpage HTML.

### B. BeautifulSoup

BeautifulSoup is a Python library used to parse HTML and extract information from it.

Install:

```bash
pip install beautifulsoup4
```

Import:

```python
from bs4 import BeautifulSoup
```

### C. Pandas

Pandas is used to organize extracted information into a DataFrame and save it as a CSV file.

Install:

```bash
pip install pandas
```

Import:

```python
import pandas as pd
```

---

## 4. Understanding HTTP Status Codes

When we send a request to a website, the server returns a status code.

| Status Code | Meaning |
|---|---|
| 200 | Request successful |
| 301 | Page permanently redirected |
| 302 | Temporary redirect |
| 403 | Access forbidden |
| 404 | Page not found |
| 429 | Too many requests |
| 500 | Internal server error |

### What is 403 Forbidden?

A `403` status code means the server understood the request but refused access.

A website may restrict automated requests or require authorization.

**Important:** Do not try to bypass access restrictions. Check the website's terms, permissions and available access methods instead.

---

## 5. What is HTML?

HTML stands for **HyperText Markup Language**.

It is used to create the structure of web pages.

HTML contains different elements called tags.

Common HTML tags:

| HTML Tag | Purpose |
|---|---|
| `<html>` | Main HTML document |
| `<head>` | Page information |
| `<body>` | Visible webpage content |
| `<h1>` | Main heading |
| `<p>` | Paragraph |
| `<div>` | Container for other elements |
| `<span>` | Inline content |
| `<a>` | Link |
| `<img>` | Image |
| `<ul>` | Unordered list |
| `<li>` | List item |

### Example HTML

```html
<div class="company-card">
    <h2>Example Company</h2>
    <p class="rating">4.5</p>
    <p class="reviews">1200 Reviews</p>
</div>
```

In this example:

- `div` is a container.
- `class="company-card"` identifies the container.
- `h2` contains the company name.
- `p` contains the rating and reviews.

Understanding HTML is important because BeautifulSoup uses HTML tags, classes and other attributes to locate information.

---

## 6. What is BeautifulSoup?

BeautifulSoup converts HTML into a structure that Python can search and navigate.

Example:

```python
from bs4 import BeautifulSoup

html = """
<div class="company-card">
    <h2>Example Company</h2>
    <p class="rating">4.5</p>
</div>
"""

soup = BeautifulSoup(html, "html.parser")

print(soup.prettify())
```

### What is `html.parser`?

It is Python's built-in HTML parser.

It helps BeautifulSoup understand the HTML structure.

### What is `prettify()`?

`prettify()` formats HTML with indentation and line breaks.

It makes the HTML easier to read.

---

## 7. Understanding find() and find_all()

These are two important BeautifulSoup methods.

### A. find()

`find()` returns the first matching element.

Example:

```python
company = soup.find("h2")

print(company.text)
```

Output:

```text
Example Company
```

### B. find_all()

`find_all()` returns all matching elements in a list.

Example:

```python
companies = soup.find_all("h2")

for company in companies:
    print(company.text)
```

### Difference

| find() | find_all() |
|---|---|
| Returns the first matching element | Returns all matching elements |
| Returns one element or None | Returns a list |
| Useful for one value | Useful for multiple values |

Example:

```python
soup.find("p", class_="rating")
```

Finds the first paragraph with the class `rating`.

```python
soup.find_all("p", class_="rating")
```

Finds all paragraphs with the class `rating`.

**Important:** In BeautifulSoup, use `class_` instead of `class` because `class` is a reserved keyword in Python.

---

## 8. How to Inspect a Website's HTML

Before extracting data, we need to understand where the information is stored in the HTML.

### Step 1: Open the Website

Visit the webpage you are allowed to inspect.

### Step 2: Open Developer Tools

Right-click the information you want to extract and select **Inspect**.

You can also press:

```text
F12
```

### Step 3: Find the HTML Element

The browser highlights the HTML element responsible for displaying the selected information.

For example, if you want a company rating, inspect the rating displayed on the webpage.

You may find something like:

```html
<p class="rating">4.5</p>
```

### Step 4: Identify the Tag and Class

In this example:

- Tag: `p`
- Class: `rating`
- Text: `4.5`

Now we can use BeautifulSoup to extract it.

```python
rating = soup.find("p", class_="rating")

if rating:
    print(rating.get_text(strip=True))
```

**Important:** Class names are not universal. They depend on the website and can change over time.

---

## 9. Extracting Text From HTML

BeautifulSoup provides different ways to extract text.

### A. `.text`

Returns the text inside an element.

```python
name = soup.find("h2")

print(name.text)
```

### B. `.get_text()`

Extracts text from an element.

```python
print(name.get_text())
```

### C. `.get_text(strip=True)`

Extracts text and removes unnecessary spaces around it.

```python
print(name.get_text(strip=True))
```

### D. `.get()`

Extracts an HTML attribute.

Example:

```html
<a href="https://example.com">Visit Website</a>
```

Python:

```python
link = soup.find("a")

print(link.get("href"))
```

Output:

```text
https://example.com
```

---

## 10. Why Do We Need to Extract a Parent Container First?

Imagine a webpage contains 100 company cards.

Each company card contains:

- Company name
- Rating
- Reviews
- Company type
- Headquarters
- Company age
- Employees
- Tags
- Description

If we extract every rating separately and every company name separately, it can become difficult to match the correct information.

For example, one company may have four fields and another may have only three.

This can create incorrect data when combining separate lists.

### Better Approach: Extract Each Company Container

First, identify the parent container that holds all the information for one company.

Example:

```html
<div class="company-card">

    <h2>Example Company</h2>

    <p class="rating">4.5</p>

    <p class="reviews">1200 Reviews</p>

    <p class="company-type">Public</p>

</div>
```

Now we can extract each company's information separately.

```python
companies = soup.find_all("div", class_="company-card")

for company in companies:

    name = company.find("h2")
    rating = company.find("p", class_="rating")
    reviews = company.find("p", class_="reviews")
```

This approach keeps each company's information together.

**Remember:** First find the parent container, then extract the child elements inside it.

---

## 11. Understanding Nested HTML Elements

Sometimes information is stored inside multiple HTML elements.

Example:

```html
<div class="company-card">

    <div class="company-info">

        <h2>Example Company</h2>

        <div class="rating-section">
            <p class="rating">4.5</p>
        </div>

    </div>

</div>
```

Here, the rating is inside two nested containers.

We can navigate through them:

```python
company = soup.find("div", class_="company-card")

company_info = company.find("div", class_="company-info")

rating_section = company_info.find(
    "div",
    class_="rating-section"
)

rating = rating_section.find("p", class_="rating")

print(rating.get_text(strip=True))
```

You can also search directly inside the parent:

```python
rating = company.find("p", class_="rating")
```

This is often simpler.

---

## 12. Extracting Multiple Companies

Suppose the webpage contains several company containers.

We can use `find_all()` to collect them.

```python
company_cards = soup.find_all(
    "div",
    class_="company-card"
)

company_data = []

for card in company_cards:

    name = card.find("h2")
    rating = card.find("p", class_="rating")
    reviews = card.find("p", class_="reviews")

    company_data.append({
        "Company Name": name.get_text(strip=True) if name else None,
        "Rating": rating.get_text(strip=True) if rating else None,
        "Reviews": reviews.get_text(strip=True) if reviews else None
    })
```

Now we have a list of dictionaries.

Each dictionary represents one company.

---

## 13. Handling Missing Information

Not every company has all the information.

For example, one company may not display its company age.

If we directly call `.get_text()` on a missing element, Python will produce an error.

Incorrect:

```python
age = card.find("p", class_="company-age").get_text()
```

If the element does not exist, this causes an error.

Correct:

```python
age_element = card.find("p", class_="company-age")

age = age_element.get_text(strip=True) if age_element else None
```

This checks whether the element exists before extracting its text.

We can use the same technique for all optional fields.

---

## 14. Extracting Company Information

In the lesson, the goal is to collect information such as:

| Column | Information |
|---|---|
| Company Name | Name of the company |
| Rating | Company's rating |
| Reviews | Number of reviews |
| Company Type | Public or private |
| Headquarters | Main company location |
| Company Age | How old the company is |
| Employees | Number of employees |
| Tags | Related company categories |
| Description | About the company |

The exact HTML tags and classes must be identified using the browser's Inspect tool.

For example, the transcript demonstrates inspecting a parent container with a class similar to `company-contact-wrapper`.

Do not assume that the same class names will work on every website.

---

## 15. What is Pagination in Web Scraping?

Some websites divide their information into multiple pages.

For example:

- Page 1 contains companies 1–10.
- Page 2 contains companies 11–20.
- Page 3 contains companies 21–30.

This is called pagination.

To collect data from multiple pages, we can use a loop.

Example:

```python
for page in range(1, 4):

    url = f"https://example.com/companies?page={page}"

    response = requests.get(url)

    # Parse the webpage
    # Extract company information
```

The exact URL pattern depends on the website.

Always inspect how the page URL changes when you click Next.

---

## 16. Combining Data From Multiple Pages

We can store each page's company information in a DataFrame.

Then combine all DataFrames using:

```python
final_df = pd.concat(
    all_dataframes,
    ignore_index=True
)
```

`ignore_index=True` creates a fresh index after combining the DataFrames.

---

## 17. Exporting Scraped Data to CSV

After collecting the information, we can save it.

```python
final_df.to_csv(
    "companies.csv",
    index=False
)
```

Now we have a CSV file containing company information.

This dataset can be used for:

- Data analysis
- Data cleaning
- Data visualization
- Machine Learning projects

---

## 18. Important Web Scraping Rules

1. Check the website's Terms of Service.
2. Check its `robots.txt` rules.
3. Scrape only data you are allowed to access.
4. Do not bypass login, CAPTCHA, paywalls or access restrictions.
5. Do not send too many requests in a short time.
6. Use a reasonable delay between requests.
7. Handle missing HTML elements.
8. Check the HTTP status code.
9. Keep extracted data organized in a DataFrame.
10. Prefer an official API when available.

### What is robots.txt?

`robots.txt` is a file that websites use to communicate crawling rules to automated bots.

Example:

```text
https://example.com/robots.txt
```

It can indicate which website paths crawlers are allowed or disallowed to access.

It is important to remember that robots.txt is not a replacement for the website's Terms of Service or permission requirements.

### What if a Website Uses JavaScript?

Some websites load their information using JavaScript after the initial HTML is downloaded.

In that case, the information may not appear in `response.text`.

You may need an official API or an approved browser automation tool, depending on the website's rules.

---

## 19. API vs Web Scraping vs Machine Learning

These topics are connected:

1. API or Web Scraping collects data.
2. Pandas organizes the collected data.
3. Data cleaning prepares the data.
4. Data analysis helps us understand the data.
5. Machine Learning uses prepared data to train models.

Example:

A company dataset can be collected using web scraping, cleaned using Pandas and used for a suitable prediction or analysis project.

---

## 20. Important Takeaways

- Web scraping means collecting website data using code.
- Requests downloads webpage content.
- BeautifulSoup parses HTML.
- `find()` extracts the first matching element.
- `find_all()` extracts all matching elements.
- `get_text(strip=True)` extracts clean text.
- `get()` extracts an HTML attribute.
- `prettify()` makes HTML easier to read.
- `class_` is used to search by HTML class.
- Inspect helps us identify HTML tags and classes.
- Parent containers help keep related information together.
- Pagination helps collect data from multiple pages.
- Pandas organizes extracted data.
- `pd.concat()` combines DataFrames.
- `to_csv()` saves the final dataset.

---

## 21. Practice Questions

1. What is web scraping?
2. Why do we use web scraping?
3. What is the difference between an API and web scraping?
4. What is HTML?
5. What is BeautifulSoup?
6. What is the purpose of `requests.get()`?
7. What is the difference between `find()` and `find_all()`?
8. Why do we use `class_` instead of `class`?
9. What does `get_text(strip=True)` do?
10. Why should we extract a parent container first?
11. How do we handle missing HTML elements?
12. What is pagination?
13. Why do we use `pd.concat()`?
14. What is the purpose of robots.txt?

## 22. Practice Tasks

- Install Requests, BeautifulSoup and Pandas.
- Create a small HTML example and parse it.
- Extract a heading using `find()`.
- Extract multiple paragraphs using `find_all()`.
- Extract text using `get_text(strip=True)`.
- Extract a link using `get("href")`.
- Create a list of dictionaries from multiple company cards.
- Convert the list into a DataFrame.
- Save the DataFrame as `companies.csv`.

## 23. Useful Documentation

- Requests: https://requests.readthedocs.io/
- BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Pandas: https://pandas.pydata.org/docs/
- HTML: https://developer.mozilla.org/en-US/docs/Web/HTML

**Day 18 Complete — Fetching Data Using Web Scraping**
