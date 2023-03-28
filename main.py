import pandas as pd

# Reading the dataset
data = pd.read_csv("nato_phonetic_alphabet.csv")
data_dict = {}

# To convert the dataframe into a dictionary
for index, row in data.iterrows():
    key = row.letter
    value = row.code
    data_dict[key] = value
print(data_dict)

# User input
user_input = input("Enter the word you want to convert: ")
output_list = [data_dict[letter] for letter in user_input.upper() if letter != " "]

# Printing the final output as a list
print(output_list)
