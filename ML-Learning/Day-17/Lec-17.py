# Day 17: Fetching Data From an API
# Practical: Fetching Movie Data From TMDB API

# Install required libraries:
# pip install requests pandas

import os
import requests
import pandas as pd


# --------------------------------------------------
# 1. API CONFIGURATION
# --------------------------------------------------

# Get your own API key from:
# https://developer.themoviedb.org/

# Store your API key in an environment variable:
# Windows PowerShell:
# $env:TMDB_API_KEY="your_api_key_here"

API_KEY = os.getenv("TMDB_API_KEY")

if not API_KEY:
    raise ValueError(
        "API key not found. Set the TMDB_API_KEY environment variable first."
    )


# API endpoint for top-rated movies
BASE_URL = "https://api.themoviedb.org/3/movie/top_rated"


# --------------------------------------------------
# 2. SEND AN API REQUEST
# --------------------------------------------------

params = {
    "api_key": API_KEY,
    "page": 1
}

response = requests.get(
    BASE_URL,
    params=params,
    timeout=30
)

# Check whether the request was successful
print("Status Code:", response.status_code)

response.raise_for_status()

print("API request successful!")


# --------------------------------------------------
# 3. CONVERT RESPONSE INTO JSON
# --------------------------------------------------

data = response.json()

print("\nJSON Response Keys:")
print(data.keys())

# Get movie information
movies = data["results"]

print("\nFirst Movie:")
print(movies[0])


# --------------------------------------------------
# 4. CONVERT JSON DATA INTO DATAFRAME
# --------------------------------------------------

df = pd.DataFrame(movies)

print("\nFirst Five Movies:")
print(df.head())


# --------------------------------------------------
# 5. SELECT REQUIRED COLUMNS
# --------------------------------------------------

selected_columns = [
    "id",
    "title",
    "release_date",
    "overview",
    "popularity",
    "vote_average",
    "vote_count"
]

df = df[selected_columns]

print("\nSelected Movie Data:")
print(df.head())


# --------------------------------------------------
# 6. EXPLORE THE DATAFRAME
# --------------------------------------------------

print("\nDataFrame Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataFrame Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())


# --------------------------------------------------
# 7. FETCH DATA FROM MULTIPLE PAGES
# --------------------------------------------------

# First response tells us how many pages are available.
total_pages = data["total_pages"]

print("\nTotal Available Pages:", total_pages)

# Store all movie DataFrames here.
all_movies = []

# Fetch each page one by one.
for page in range(1, total_pages + 1):

    print(f"\nFetching Page {page}...")

    params = {
        "api_key": API_KEY,
        "page": page
    }

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=30
    )

    # Stop if the API returns an error.
    response.raise_for_status()

    # Convert response into JSON.
    page_data = response.json()

    # Extract movie list.
    movie_list = page_data["results"]

    # Convert the current page into a DataFrame.
    temp_df = pd.DataFrame(movie_list)

    # Keep only the required columns.
    temp_df = temp_df[selected_columns]

    # Add current page data to the list.
    all_movies.append(temp_df)

    print("Movies Fetched:", len(temp_df))


# --------------------------------------------------
# 8. COMBINE ALL DATAFRAMES
# --------------------------------------------------

final_df = pd.concat(
    all_movies,
    ignore_index=True
)

print("\nFinal Dataset:")
print(final_df.head())

print("\nFinal Dataset Shape:")
print(final_df.shape)

print("\nTotal Movies Collected:")
print(len(final_df))


# --------------------------------------------------
# 9. BASIC DATA CLEANING
# --------------------------------------------------

# Remove duplicate movies using their unique IDs.
final_df = final_df.drop_duplicates(subset=["id"])

# Reset the index after removing duplicates.
final_df = final_df.reset_index(drop=True)

# Handle missing values in text columns.
final_df["title"] = final_df["title"].fillna("Unknown")

final_df["overview"] = final_df["overview"].fillna("No description")

# Convert release_date into datetime format.
final_df["release_date"] = pd.to_datetime(
    final_df["release_date"],
    errors="coerce"
)

print("\nCleaned Dataset:")
print(final_df.head())

print("\nMissing Values:")
print(final_df.isnull().sum())


# --------------------------------------------------
# 10. SORT MOVIES BY RATING
# --------------------------------------------------

top_movies = final_df.sort_values(
    by="vote_average",
    ascending=False
)

print("\nTop 10 Movies:")
print(
    top_movies[
        ["title", "vote_average", "vote_count"]
    ].head(10)
)


# --------------------------------------------------
# 11. EXPORT DATAFRAME TO CSV
# --------------------------------------------------

final_df.to_csv(
    "movies.csv",
    index=False
)

print("\nDataset saved successfully as movies.csv")


# --------------------------------------------------
# 12. READ THE SAVED CSV FILE
# --------------------------------------------------

saved_df = pd.read_csv("movies.csv")

print("\nReading Saved CSV:")
print(saved_df.head())

print("\nSaved CSV Shape:")
print(saved_df.shape)


# --------------------------------------------------
# 13. PRACTICE TASKS
# --------------------------------------------------

# Task 1:
# Fetch only the first page of movies.

# Task 2:
# Display movies with a rating greater than 8.

# Task 3:
# Find the movie with the highest popularity.

# Task 4:
# Count how many movies were collected.

# Task 5:
# Save only the top 10 movies into a separate CSV file.

# Task 6:
# Find movies released after 2020.

print("\nDay 17 Practice Completed!")

Important setup before running the Python file
1. Install the libraries:
pip install requests pandas


2. Get your own API key from TMDB Developer Portal.
3. In VS Code terminal (PowerShell), set your key:
$env:TMDB_API_KEY="your_actual_api_key"


4. Run:
python Day_17_Fetching_Data_From_API.py


Day 17 complete
One important thing: The code fetches all pages reported by the API. The number of available pages and movies can change, so don't expect the exact same dataset size as the instructor's video.
