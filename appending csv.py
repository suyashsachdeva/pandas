# Introduction:
# This program demonstrates how to modify values within a Pandas DataFrame based on conditions.
# It reads a CSV file, changes certain values in specific columns based on logical conditions, 
# and displays the modified data.

import pandas as pd  # Importing the pandas library for data manipulation

# Path to the CSV file. Make sure to provide the correct path to your CSV file.
link = r'C:\Users\suyash\Desktop\KACHRA\laohub\SmileinPain\zzz...zzz...\Pokemon.csv'

# Reading the CSV file into a DataFrame
df = pd.read_csv(link)

# Modifying values in the 'Type 1' column where the value is 'Fire'
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Fav'

# Modifying values in the 'Type 1' column where the 'Legendary' column is True
df.loc[df['Legendary'] == True, 'Type 1'] = 'Tomper'

# For rows where 'HP' is greater than 100, modify 'Type 1' to 'Good' and 'Type 2' to 'Tomper'
df.loc[df['HP'] > 100, ['Type 1', 'Type 2']] = ['Good', 'Tomper']

# Display the rows where 'HP' is greater than 100 to verify the changes
print(df.loc[df['HP'] > 100])
