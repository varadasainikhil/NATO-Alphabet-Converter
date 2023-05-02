import pandas as pd

# Reading the dataset
data = pd.read_csv("nato_phonetic_alphabet.csv")

# Converting dataframe into a dictionary
data_dict = {row.letter: row.code for index, row in data.iterrows()}
print(data_dict)

onlyAlphabets = False

while not onlyAlphabets:
    # User input
    user_input = input("Enter the word you want to convert: ")
    try:
        output_list = [data_dict[letter] for letter in user_input.upper() if letter != " "]
    except KeyError:
        print("Please do not enter Special Characters or numbers.")
        onlyAlphabets = False
    else:
        # Printing the final output as a list
        print(output_list)
        onlyAlphabets = True
