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
    # Display the seating arrangement
    print("\nRow -----------------")
    for row_num in range(len(seating)):
        print(f" {row_num + 1} ", end="")  # Row numbers are 1-based
        for seat in seating[row_num]:
            print(seat, end=" ")  # Print each seat directly
        print()  # Move to the next line after printing a row

def ask_continue():
    # Ask the user if they want to continue or stop
    choice = input("\nDo you want to continue reserving seats? (Y/N): ").lower()
    while choice != 'y' and choice != 'n':
        print("Invalid input! Please enter y or n.")
        choice = input("\nDo you want to continue reserving seats? (Y/N): ").lower()
    return choice

def reserve_seat(seating):
    # Ask the user for a seat and reserve it if it's available
    seat = input("\nEnter the seat you want to reserve (ex: 1A, 2B): ").upper()

    if len(seat) != 2 or seat[1] not in "ABCD":
        print("Invalid seat format! Please enter a seat in the format RowLetter (e.g., 1A).")
        return
    
    
    # Manually check if the first character is a valid number (row)
    row_num = seat[0]
    if not row_num.isdigit():
        print("Invalid row number! Please enter a valid seat.")
        return
    
    row_num = int(row_num) - 1  # Row index
    seat_letter = seat[1]

    # Check if row number and seat letter are valid
    if row_num < 0 or row_num >= len(seating):
        print("Invalid row number! Please try again.")
        return
    
    # Find the column index for the seat letter
    seat_index = "ABCD".index(seat_letter)

    # Check if the seat is already occupied
    if seating[row_num][seat_index] == 'X':
        print(f"Seat {seat} is already occupied! Please choose another one.")
    else:
        # Mark the seat as reserved
        seating[row_num][seat_index] = 'X'


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

# Start reservation process
continue_reserving = 'y'
while continue_reserving == 'y':
    display_seating(seating_chart)
    
    # Ask the user to reserve a seat
    reserve_seat(seating_chart)

    # Ask if the user wants to continue or stop
    continue_reserving = ask_continue()
print("\nReservation process ended.")
print("\n Thank you for using my program :] goodbye!")
