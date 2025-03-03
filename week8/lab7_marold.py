#Matthew Marold
#Lab 7 - Dictionaries
#SE126
#02/28/2025

#---Imports ---
import csv

#program prompt -- 

#--- Variable Dictionary ---
# Function to load words from the CSV file into a dictionary
def load_dict(file_path):
    word_dict = {}
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if there's one
        for row in reader:
            word = row[0].strip().lower()  # Key (Word)
            definition = row[1].strip()  # Value (Definition)
            word_dict[word] = definition
    return word_dict

def show_all_words(word_dict):
    if word_dict:
        print("---PROGRAMMING DICTIONARY---")
        print("-" * 80)
        for word, definition in dictionary.items():
            print()
            print(f"{word.upper()}: {definition}")
        print("-" * 80)
    else:
        print("Dictionary is Empty!")

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
        print("-" * 80)
        print(f"{word.capitalize()}: {word_dict[word]}")
        print("-" * 80)
    else:
        print("Word not found!")

def add_word(word_dict):
    word = input("Enter The word You would like to add: ").strip().lower()
    if word in word_dict:
        print()
        print(f"'{word}' already exists in the dictionary.")
    else:
        definition = input(f"Enter the definition for {word}: ").strip()
        word_dict[word] = definition
        print("-" * 80)
        print(f"The word and definition have been added to the dictionary: {word.capitalize()}: {word_dict[word]}")
        print("-" * 80)
#--- MAIN CODE BELOW ---

file_path = "text_files/words.csv"
dictionary = load_dict(file_path)
answer = "y"

while answer == "y":
    display_menu()

    choice = input("Select an option [1-4]: ").strip()

    if choice == "1":
        show_all_words(dictionary)
    elif choice == "2":
        search_word(dictionary)
    elif choice == "3":
        add_word(dictionary)
    elif choice == "4":
        answer = "n"
        print("Thank you for using my program, goodbye :)")
    
    else:
        print("Invalid choice. Please select a valid option [1-4]")