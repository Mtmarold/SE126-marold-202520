#Matthew Marold
#Lab 7 - Dictionaries
#SE126
#02/28/2025

#---Imports ---
import csv

#program prompt -- 

#--- Variable Dictionary ---
# Function to load words from the CSV file into a dictionary
def load_words_from_csv(file_path):
    word_dict = {}
    file_path = 'text_files/words.csv'
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if there's one
        for row in reader:
            word = row[0].strip().lower()  # Key (Word)
            definition = row[1].strip()  # Value (Definition)
            word_dict[word] = definition
    return word_dict


# Function to display the menu and interact with the dictionary
def display_menu():
    print("\nMy Programming Dictionary Menu")
    print("1. Show all words")
    print("2. Search for a word")
    print("3. Add a word")
    print("4. EXIT")


def search_word(word_dict):
    word = input("Enter the word to search for: ").strip().lower()
    if word in word_dict:
        print(f"{word.capitalize()}: {word_dict[word]}")
    else:
        print("Word not found!")

def add_word(word_dict):
    word = input("Enter The word You would like to add: ")
    if word not in word_dict:
        print()
#--- MAIN CODE BELOW ---
