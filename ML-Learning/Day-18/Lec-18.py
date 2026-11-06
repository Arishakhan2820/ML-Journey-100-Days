# Day 18: Fetching Data Using Web Scraping

# Install required libraries:
# pip install requests beautifulsoup4 pandas

import requests
import pandas as pd
import time

from bs4 import BeautifulSoup


# ==================================================
# PART 1: UNDERSTANDING BEAUTIFULSOUP
# ==================================================

html = """
<html>
<head>
    <title>Company Information</title>
</head>

<body>

    <div class="company-card">

        <h2>ABC Technologies</h2>

        <p class="rating">4.5</p>

        <p class="reviews">1200 Reviews</p>

        <p class="company-type">Public</p>

        <p class="headquarters">Karachi</p>

    </div>


    <div class="company-card">

        <h2>XYZ Solutions</h2>

        <p class="rating">4.2</p>

        <p class="reviews">800 Reviews</p>

        <p class="company-type">Private</p>

        <p class="headquarters">Lahore</p>

    </div>


    <div class="company-card">

        <h2>Tech World</h2>

        <p class="rating">4.0</p>

        <p class="reviews">500 Reviews</p>

        <p class="company-type">Private</p>

    </div>

</body>
</html>
"""


# ==================================================
# PART 2: CREATE BEAUTIFULSOUP OBJECT
# ==================================================

soup = BeautifulSoup(html, "html.parser")


# Print formatted HTML
print("\nFormatted HTML:")
print(soup.prettify())


# ==================================================
# PART 3: USING find()
# ==================================================

# Find the first company heading

first_company = soup.find("h2")

print("\nFirst Company:")
print(first_company.get_text(strip=True))


# ==================================================
# PART 4: USING find_all()
# ==================================================

# Find all company headings

all_companies = soup.find_all("h2")

print("\nAll Companies:")

for company in all_companies:

    print(company.get_text(strip=True))


# ==================================================
# PART 5: FIND ELEMENTS USING CLASS
# ==================================================

# Find the first rating

first_rating = soup.find("p", class_="rating")

print("\nFirst Rating:")
print(first_rating.get_text(strip=True))


# Find all ratings

all_ratings = soup.find_all("p", class_="rating")

print("\nAll Ratings:")

for rating in all_ratings:

    print(rating.get_text(strip=True))


# ==================================================
# PART 6: EXTRACT HTML ATTRIBUTES
# ==================================================

link_html = """
<a href="https://example.com">
    Visit Website
</a>
"""

link_soup = BeautifulSoup(link_html, "html.parser")

link = link_soup.find("a")

print("\nLink Text:")
print(link.get_text(strip=True))

print("\nLink URL:")
print(link.get("href"))


# ==================================================
# PART 7: EXTRACT DATA FROM COMPANY CONTAINERS
# ==================================================

company_cards = soup.find_all(
    "div",
    class_="company-card"
)

company_data = []

for card in company_cards:

    # Company Name
    name_element = card.find("h2")

    # Rating
    rating_element = card.find(
        "p",
        class_="rating"
    )

    # Reviews
    reviews_element = card.find(
        "p",
        class_="reviews"
    )

    # Company Type
    type_element = card.find(
        "p",
        class_="company-type"
    )

    # Headquarters
    headquarters_element = card.find(
        "p",
        class_="headquarters"
    )

    # Extract text safely
    name = (
        name_element.get_text(strip=True)
        if name_element else None
    )

    rating = (
        rating_element.get_text(strip=True)
        if rating_element else None
    )

    reviews = (
        reviews_element.get_text(strip=True)
        if reviews_element else None
    )

    company_type = (
        type_element.get_text(strip=True)
        if type_element else None
    )

    headquarters = (
        headquarters_element.get_text(strip=True)
        if headquarters_element else None
    )

    # Store one company's information together
    company_data.append({

        "Company Name": name,

        "Rating": rating,

        "Reviews": reviews,

        "Company Type": company_type,

        "Headquarters": headquarters

    })


# ==================================================
# PART 8: CONVERT DATA INTO PANDAS DATAFRAME
# ==================================================

df = pd.DataFrame(company_data)

print("\nCompany DataFrame:")
print(df)


# ==================================================
# PART 9: DATAFRAME INFORMATION
# ==================================================

print("\nFirst Five Rows:")
print(df.head())

print("\nDataFrame Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataFrame Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())


# ==================================================
# PART 10: BASIC DATA CLEANING
# ==================================================

# Convert rating into numeric values

df["Rating"] = pd.to_numeric(
    df["Rating"],
    errors="coerce"
)

# Remove the word Reviews and convert the count to numbers

df["Reviews"] = (
    df["Reviews"]
    .str.replace(" Reviews", "", regex=False)
)

df["Reviews"] = pd.to_numeric(
    df["Reviews"],
    errors="coerce"
)

print("\nCleaned Data:")
print(df)


# ==================================================
# PART 11: FILTER DATA
# ==================================================

# Companies with rating greater than 4.0

high_rated_companies = df[
    df["Rating"] > 4.0
]

print("\nCompanies With Rating Above 4.0:")
print(high_rated_companies)


# ==================================================
# PART 12: EXPORT DATA TO CSV
# ==================================================

df.to_csv(
    "companies.csv",
    index=False
)

print("\nCompany dataset saved as companies.csv")


# ==================================================
# PART 13: READ SAVED CSV
# ==================================================

saved_df = pd.read_csv("companies.csv")

print("\nReading Saved Dataset:")
print(saved_df.head())


# ==================================================
# PART 14: LIVE WEBSITE SCRAPING TEMPLATE
# ==================================================

# IMPORTANT:
# Use this section only on a website where automated
# access and data collection are permitted.
#
# Before scraping:
# 1. Read the website's Terms of Service.
# 2. Check its robots.txt rules.
# 3. Confirm that the page is publicly accessible.
# 4. Do not bypass 403, login, CAPTCHA or other restrictions.
#
# The URL and CSS classes below are examples.
# Replace them only after inspecting an authorized webpage.


def scrape_company_page(url):

    headers = {
        "User-Agent": "EducationalWebScraper/1.0 (learning project)"
    }

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        print("\nHTTP Status:", response.status_code)

        # Stop if the website refuses the request.
        response.raise_for_status()

        # Parse downloaded HTML.
        page_soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        # Replace this class with the actual parent
        # container found using the Inspect tool.
        cards = page_soup.find_all(
            "div",
            class_="company-card"
        )

        page_data = []

        for card in cards:

            # Replace these selectors after inspecting
            # the permitted website's HTML.

            name_element = card.find("h2")

            rating_element = card.find(
                "p",
                class_="rating"
            )

            reviews_element = card.find(
                "p",
                class_="reviews"
            )

            name = (
                name_element.get_text(strip=True)
                if name_element else None
            )

            rating = (
                rating_element.get_text(strip=True)
                if rating_element else None
            )

            reviews = (
                reviews_element.get_text(strip=True)
                if reviews_element else None
            )

            page_data.append({

                "Company Name": name,

                "Rating": rating,

                "Reviews": reviews

            })

        return page_data

    except requests.exceptions.HTTPError as error:

        print("Website returned an HTTP error:", error)

    except requests.exceptions.Timeout:

        print("Request timed out.")

    except requests.exceptions.RequestException as error:

        print("Request failed:", error)

    return []


# ==================================================
# PART 15: PAGINATION TEMPLATE
# ==================================================

# Example only:
# Replace the URL pattern with the actual pagination
# pattern of a website that permits scraping.

def scrape_multiple_pages(base_url, page_numbers):

    all_page_data = []

    for page in page_numbers:

        url = f"{base_url}?page={page}"

        print(f"\nChecking Page {page}")

        page_data = scrape_company_page(url)

        if page_data:

            all_page_data.append(
                pd.DataFrame(page_data)
            )

        # Wait before requesting another page.
        time.sleep(2)

    if all_page_data:

        final_df = pd.concat(
            all_page_data,
            ignore_index=True
        )

        return final_df

    return pd.DataFrame()


# ==================================================
# PART 16: PRACTICE TASKS
# ==================================================

# Task 1:
# Add a new company to the sample HTML.

# Task 2:
# Extract all company names.

# Task 3:
# Extract all ratings.

# Task 4:
# Add company age and employee information.

# Task 5:
# Extract company tags from a nested HTML element.

# Task 6:
# Find companies with a rating greater than 4.

# Task 7:
# Save only high-rated companies into another CSV file.

print("\nDay 18 Practice Completed!")
