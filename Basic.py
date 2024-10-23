# Introduction to Pandas:
# Pandas is a powerful and widely-used Python library for data manipulation and analysis. 
# It provides data structures like DataFrames and Series, which are particularly useful for handling structured data (like CSV files).
# Pandas makes it easy to perform data manipulation, cleaning, filtering, sorting, and grouping operations.

import pandas as pd  # Importing the Pandas library as 'pd'

# Path to the CSV file. Replace this path with the actual file location on your system.
file_path = r'PATH_csv'

# Reading the CSV file into a Pandas DataFrame
data = pd.read_csv(file_path) 

# Shuffling the rows of the DataFrame randomly. 'frac=1' ensures that all rows are returned in random order.
data = data.sample(frac=1)

# Creating an empty list to store DataFrames that will hold the partitioned data
sus = []

# Loop to divide the data into 4 equal parts. 
# We are selecting the columns "Full Name", "Roll No.", and "Branch" and splitting them in a staggered way.
for i in range(4):
    # Appending each partition of the data into the 'sus' list. 
    # Using slicing to select every 4th row starting from index i.
    sus.append(data.filter(["Full Name", "Roll No.", "Branch"])[i::4])

# Printing the first partition of the data, i.e., the first subset of the divided data.
print(sus[0])
