# Introduction:
# This program reads a CSV file, processes it in chunks (for memory efficiency), and counts the occurrences of 
# different 'Type 1' values in the dataset. It demonstrates Pandas' chunk processing and groupby operations.

import pandas as pd  # Importing Pandas for data manipulation

# Path to the CSV file. Make sure to provide the correct path to your CSV file.
link = r'...\Pokemon.csv'

# Reading the CSV file to display the column names and get a preview
df = pd.read_csv(link)

# Print the column names of the dataset for reference
print("Columns in the dataset:", df.columns)

# Add a 'count' column to keep track of occurrences
df['count'] = 1

# Create an empty DataFrame to store the combined result after processing chunks
newdf = pd.DataFrame(columns=df.columns)

# Process the CSV file in chunks to avoid memory issues when working with large files
for chunk in pd.read_csv(link, chunksize=20):
    # Group by 'Type 1' and count occurrences within each chunk
    grouped_chunk = chunk.groupby('Type 1').count()
    # Concatenate the result with the newdf DataFrame
    newdf = pd.concat([newdf, grouped_chunk])

# Print the final DataFrame with the counts of 'Type 1'
print(newdf)
