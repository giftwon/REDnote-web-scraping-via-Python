import pandas as pd

# Read Excel path
file_paths = [
    "url1.xlsx",
    "url2.xlsx"
]

# New Empty DataFrame for storing all URLs
all_urls = pd.DataFrame()

# Read URL
for file in file_paths:
    df = pd.read_excel(file)
    all_urls = pd.concat([all_urls, df.iloc[:, 0]], ignore_index=True)

# Cleaning
unique_urls = all_urls.drop_duplicates().reset_index(drop=True)

# Write the deduplicated URLs to a new Excel file
unique_urls.to_excel("urlall.xlsx", index=False, header = True)
