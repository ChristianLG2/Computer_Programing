# Christian Lira Spring 2023

'''This program imports two CSV files and merge them based on the indexes after this merge adds another column based on a condition met on the merged columns defined in the able_to_vote function which describes as if were Boolean type and saves the data to a new CSV file named "Edited_data". '''

#%%
# Import required libraries
import csv
import pandas as pd

# Define file paths
data = "data.csv"
country = "Country.csv"

# Read CSV files as dataframes
dataframe = pd.read_csv(data)
countryfile = pd.read_csv(country)

# Merge dataframes using left and right indices
df = dataframe.merge(countryfile, left_index=True, right_index=True)

# Increment the index by 1
df.index = df.index + 1 

# Define a function to check if a person is eligible to vote
def able_to_vote(Age, Country):
    if Age >= 18 and Country == "United States": 
        return True   
    else:
        return False

# Apply the able_to_vote function to each row in the dataframe to create a new column called AbletoVote
df['abletovote'] = df.apply(lambda row: able_to_vote(row['Age'], row['Country ']), axis=1)

# Print the column names of the new dataframe
print(df.columns)

# Save the edited dataframe as a new CSV file
df.to_csv("edited_data.csv")

# %%
