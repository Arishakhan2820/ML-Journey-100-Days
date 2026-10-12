---

### File 2: Python Practice Script (`code.py`)

```python
# ==========================================================
# Day 15: Working with CSV Files - Practice Script (`code.py`)
# ==========================================================

import pandas as pd
import numpy as np

print("=" * 60)
print(" 1. CREATING AND SAVING A LOCAL CSV FILE")
print("=" * 60)

# Creating sample student dataset
data = {
    'Student_ID': [101, 102, 103, 104, 105],
    'Name': ['Areesha', 'Ali', 'Sara', 'Zain', 'Fatima'],
    'CGPA': [3.6, 2.9, 3.9, 3.2, 3.8],
    'IQ': [115, 95, 130, 105, 125],
    'Placed': [1, 0, 1, 0, 1]
}

df_sample = pd.DataFrame(data)

# Save to CSV locally
csv_filename = 'students_data.csv'
df_sample.to_csv(csv_filename, index=False)
print(f"-> Created local file: '{csv_filename}' successfully!")


print("\n" + "=" * 60)
print(" 2. LOADING SPECIFIC COLUMNS WITH pd.read_csv()")
print("=" * 60)

# Load only specific columns and optimize data types
df_filtered = pd.read_csv(
    csv_filename,
    usecols=['Name', 'CGPA', 'Placed'],
    dtype={'Placed': int}
)

print("-> Loaded Data (Selected Columns):")
print(df_filtered)


print("\n" + "=" * 60)
print(" 3. HANDLING MISSING VALUES (na_values)")
print("=" * 60)

# Creating a messy dataset with custom placeholders like '?' or 'N/A'
messy_data = {
    'User': ['User1', 'User2', 'User3', 'User4'],
    'Score': [85, '?', 92, 'N/A'],
    'Age': [22, 25, '-', 24]
}

df_messy = pd.DataFrame(messy_data)
messy_csv = 'messy_sample.csv'
df_messy.to_csv(messy_csv, index=False)

# Parse '?', 'N/A', and '-' as proper NaN missing values during load
df_clean_load = pd.read_csv(messy_csv, na_values=['?', 'N/A', '-'])

print("-> Cleaned Load (Converted custom placeholders to true NaN):")
print(df_clean_load)
print("\n-> Null Values Summary:")
print(df_clean_load.isnull().sum())


print("\n" + "=" * 60)
print(" 4. CHUNKING LARGE CSV FILES FOR MEMORY EFFICIENCY")
print("=" * 60)

# Process file in small batches using chunksize
chunk_size = 2
print(f"-> Reading '{csv_filename}' in chunks of {chunk_size} rows:")

for batch_num, chunk in enumerate(pd.read_csv(csv_filename, chunksize=chunk_size)):
    print(f"\n[Batch {batch_num + 1}]")
    print(chunk[['Name', 'CGPA']])

print("\n" + "=" * 60)
print(" Practice script execution completed successfully!")
print("=" * 60)
