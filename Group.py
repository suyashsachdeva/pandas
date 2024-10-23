import pandas as pd  # Importing pandas for data manipulation
import re  # Importing regular expressions, though not used in this case

# Path to the CSV file. Update the path to the actual location of your file.
link = r'C:\Users\suyash\Desktop\KACHRA\laohub\SmileinPain\zzz...zzz...\Pokemon.csv'

# Reading the CSV file into a Pandas DataFrame
df = pd.read_csv(link)

# Grouping the DataFrame by 'Type 1' and 'Type 2', then calculating the mean of each group.
# Sorting the result by the 'Attack' column in descending order to find Pokémon types with the highest mean attack values.
print(df.groupby(['Type 1', 'Type 2']).mean().sort_values('Attack', ascending=False))

# Adding a 'count' column to the DataFrame to count occurrences of each Pokémon type
df['count'] = 1

# Grouping by 'Type 1' and 'Type 2' again, counting the occurrences for each group
# This effectively gives the number of Pokémon for each combination of 'Type 1' and 'Type 2'
print(df.groupby(['Type 1', 'Type 2']).count()['count'])
