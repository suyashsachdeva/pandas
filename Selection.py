# Introduction:
# This script demonstrates several Pandas functionalities such as adding new columns, filtering data, 
# reshaping DataFrames, exporting to CSV, and applying regular expressions for advanced filtering.

import pandas as pd  # Importing the pandas library for data manipulation
import numpy as np   # Importing numpy for numerical operations
import re            # Importing regular expressions for pattern matching

# Path to the CSV file. Make sure to provide the correct path to your CSV file.
link = r'C:\Users\suyash\Desktop\KACHRA\laohub\SmileinPain\zzz...zzz...\Pokemon.csv'

# Reading the CSV file into a DataFrame
df = pd.read_csv(link)

# Add all the stats to find the most powerful Pokémon
# We sum the columns 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', and 'Speed' to compute the total stats.
df['total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print("With total stats column added:")
print(df.head())

# Dropping the 'total' column
df = df.drop(columns=['total'], axis=1)
print("\nAfter dropping the 'total' column:")
print(df.head())

# Another way of calculating total stats by using .iloc to select specific columns
# Here, we use iloc to slice the DataFrame and sum columns 4 to 10 (which correspond to the stats columns)
df['total'] = df.iloc[:, 4:10].sum(axis=1)
print("\nTotal stats calculated using iloc:")
print(df.head())

# Reordering columns: Placing the 'total' column after the 'Name' and before the stats columns
col = list(df.columns.values)
df = df[col[1:4] + [col[-1]] + col[4:-1]]  # Adjusting the column order
print("\nReordered DataFrame with 'total' column in desired position:")
print(df.head())

# Exporting the modified DataFrame to a CSV file with tab-separated values
# The 'sep' argument specifies the delimiter as '\t' (tab).
df.to_csv('mod.txt', index=False, sep='\t')  # 'index=False' avoids writing the DataFrame's index to the file

# Using multiple filters: Finding all 'Grass' type Pokémon that also have 'Poison' as 'Type 2' and HP > 70
filtered_pokemon = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
print("\nFiltered Pokémon (Grass Type 1, Poison Type 2, HP > 70):")
print(filtered_pokemon)

# Using filters with string operations: Exclude Pokémon whose name contains 'Mega'
non_mega_pokemon = df.loc[~df['Name'].str.contains('Mega')]
print("\nPokémon without 'Mega' in their name:")
print(non_mega_pokemon)

# Resetting the index of the DataFrame
df = df.reset_index(drop=True)  # 'drop=True' prevents the old index from being added as a column
print("\nDataFrame with reset index:")
print(df.head())

# Regular expressions with Pandas: 
# Finding Pokémon with 'Type 1' containing 'Fire' or 'Water' (case-insensitive match using re.I flag)
regex_filtered_pokemon = df.loc[df['Type 1'].str.contains('Fire|Water', flags=re.I, regex=True)]
print("\nPokémon with 'Type 1' containing 'Fire' or 'Water' (case-insensitive):")
print(regex_filtered_pokemon)

# Using regular expressions to find Pokémon whose name starts with 'Pi' followed by any characters
name_pattern_pokemon = df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]
print("\nPokémon with names starting with 'Pi' (case-insensitive):")
print(name_pattern_pokemon)
