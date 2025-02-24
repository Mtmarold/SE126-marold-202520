#Matthew Marold
#Lab 6 - Collections & Logic
#2/22/2025
#SE126


#imports
import csv
import random



#program prompt - 6. (Absolute C++, 3rd Edition. Savitch, Walter. P. 223 #10)
#Write a Python program using lists (1D or 2D) to assign passengers seats in an airplane. Assume a
#small airplane with seat numbering as follows.
#Row
#1 A B C D
#2 A B C D
#3 A B C D
#4 A B C D
#5 A B C D
#6 A B C D
#7 A B C D
#The program should display the seat pattern, with an ‘X’ making the seats already assigned. For
#example, after seats 1A, 2B and 4C are taken the display should look like this:
#row
#1 X B C D
#2 A X C D
#3 A B C D
#4 A B X D
#5 A B C D
#6 A B C D
#7 A B C D
#After displaying the seats available, the program prompts for the seat desired, the user types in a seat
#and then the display of available seats is updated. This continues until all seats are filled or until the
#user signals that the program should end. If a user types in a seat that is already assigned, the
#program should say that the seat is occupied and ask for another choice.
#• You must use a function to display the seating map
#• You must use a function that asks the user in they want to continue reserving seats or stop.
#The function should only accept an uppercase or lowercase ‘y’ or ‘n’


#---- Variable Dictionary


#---- Main Code Below -----
# Initialize the seating chart as a 2D list with all seats available
seating_chart = [
    ['A', 'B', 'C', 'D'],  # Row 1
    ['A', 'B', 'C', 'D'],  # Row 2
    ['A', 'B', 'C', 'D'],  # Row 3
    ['A', 'B', 'C', 'D'],  # Row 4
    ['A', 'B', 'C', 'D'],  # Row 5
    ['A', 'B', 'C', 'D'],  # Row 6
    ['A', 'B', 'C', 'D']   # Row 7
]

def display_seating(seating):
    """Display the seating chart with reserved seats marked as 'X'."""
    print(f"{'ROW':3}   {'A':5}  {'B':5}  {'C':5}  {'D':5}")
    print("-------------------------------------------------")
    for row_num in range(len(seating)):
        print(f" {row_num + 1} ", end="")  # Row numbers are 1-based
        for seat in seating[row_num]:
            print(f"   {seat:3}", end=" ")  # Print each seat directly
        print()  # Move to the next line after printing a row
    print("------------------------------------------------")


def ask_to_continue():
    # Ask the user if they want to continue or stop
    choice = input("\nDo you want to continue reserving seats? (Y/N): ").lower()
    while choice != 'y' and choice != 'n':
        print("Invalid input! Please enter y or n.")
        choice = input("\nDo you want to continue reserving seats? (Y/N): ").lower()
    return choice

def reserve_seat(seating):
    """Prompts the user to reserve a seat and marks it as taken."""
    seat = input("\nEnter the seat you want to reserve (example: 1A, 2B): ").strip().upper()

    # Check for valid input format (1A, 2B, etc.)
    if len(seat) != 2 or seat[1] not in "ABCD":
        print("Invalid seat format! Please enter a seat in the format RowLetter (example: 1A).")
        return
    
    row_num_str = seat[0]  # Get the row number as a string
    seat_letter = seat[1]  # Seat letter (A, B, C, D)

    # List of valid row numbers (1 to 7)
    valid_rows = ['1', '2', '3', '4', '5', '6', '7']

    # Check if the row number is in the list of valid rows
    if row_num_str not in valid_rows:
        print("Invalid row number! Please enter a valid seat.")
        return
    
    row_num = int(row_num_str) - 1  # Convert row number to 0-based index
    
    # Check if the seat letter is valid and find the corresponding seat index
    seat_index = -1  # Default invalid value
    seat_letters = ['A', 'B', 'C', 'D']
    for i in range(len(seat_letters)):
        if seat_letter == seat_letters[i]:
            seat_index = i  # Update seat_index when we find a match
    
    # If seat_index is still -1, the seat letter is invalid
    if seat_index == -1:
        print("Invalid seat letter! Please try again.")
        return

    # Check if the seat is already occupied
    if seating[row_num][seat_index] == 'X':
        print(f"Sorry, seat {seat} is already taken! Choose another seat.")
    else:
        seating[row_num][seat_index] = 'X'  # Mark seat as reserved
        print(f"Seat {seat} has been successfully reserved.")





# Start reservation process
continue_reserving = 'y'
while continue_reserving == 'y':
    display_seating(seating_chart)
    
    # Ask the user to reserve a seat
    reserve_seat(seating_chart)

    # Ask if the user wants to continue or stop
    continue_reserving = ask_to_continue()
print("\nReservation process ended.")
print("\n Thank you for using my program :] goodbye!")
