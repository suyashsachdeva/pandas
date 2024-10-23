# Introduction:
# This program demonstrates how to read different file formats (CSV, Excel, TXT), perform basic data exploration 
# such as viewing headers, specific rows/columns, and sorting. It also shows how to use iloc, loc, and other useful 
# Pandas functions for data analysis.

import pandas as pd  # Importing pandas for data manipulation
import numpy as np   # Importing numpy for numerical operations

# File paths for the Pokémon data files. Update these paths to your local file locations.
link = r'...\Pokemon.csv'
# link1 = r'C:\Users\suyash\Desktop\KACHRA\laohub\SmileinPain\zzz...zzz...\pokemon_data.xlsx'
link2 = r'...\pokemon_data.txt'

# Reading the CSV file into a Pandas DataFrame
df = pd.read_csv(link)

# Uncomment the line below to read the Excel file if available
# df1 = pd.read_excel(link1)

# Reading the TXT file with tab-separated values into a Pandas DataFrame
df2 = pd.read_csv(link2, delimiter='\t')

# Displaying the first 5 rows of the DataFrame (the default for head() is 5)
print("First 5 rows of the CSV file:")
print(df.head())

# Displaying the last 5 rows of the DataFrame using tail()
print("\nLast 5 rows of the CSV file:")
print(df.tail())

# Displaying the first 3 rows of the TXT file
print("\nFirst 3 rows of the TXT file:")
print(df2.head(3))

# Reading the column headers
print("\nColumn headers of the CSV file:")
print(df.columns)

# Reading specific columns (multiple columns can be selected by passing a list)
print("\nSpecific columns (Name, Type 1, HP):")
print(df[['Name', 'Type 1', 'HP']][:5])  # Displaying the first 5 rows of selected columns

# Reading a single column using dot notation (works only for single-word columns)
print("\nFirst 5 Pokémon names:")
print(df.Name[:5])

# Reading a specific row using iloc (integer location-based indexing)
print("\nSecond row of the DataFrame:")
print(df.iloc[1])

# Reading a specific element using iloc (row 2, column 1)
print("\nElement at row 3, column 2 (iloc[2,1]):")
print(df.iloc[2, 1])

# Looping through each row using iterrows() and printing the index and row content
print("\nIterating through each row:")
for index, row in df.iterrows():
    print(index, row)

# Using loc to filter data based on conditions (e.g., Pokémon of Type 'Fire')
print("\nPokémon with 'Type 1' as Fire:")
print(df.loc[df['Type 1'] == 'Fire'])

# Displaying summary statistics of the numerical columns in the dataset
print("\nSummary statistics of the numerical columns:")
print(df.describe())

# Sorting the DataFrame by 'HP' (descending) and 'Name' (ascending)
print("\nData sorted by 'HP' (descending) and 'Name' (ascending):")
print(df.sort_values(["HP", "Name"], ascending=[False, True]))
