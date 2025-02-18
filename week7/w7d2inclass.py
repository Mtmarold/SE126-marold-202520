#Matthew Marold 
#W7D2 - Live Class: Review of Binary Search & Bubble Sort + 2D Lists


def menu():
    print("Simple Searching Menu")
    print("1. Search by Name: ")
    print("2. Search by Num")
    print("3. Search by Color")
    print("4. EXIT")

    menu_choice = input("Enter your Search type [1-4]: ")
    return menu_choice

def swap(index, listName):
    temp = listName[i]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp
    return listName

import csv
#create your empty 1d parallel lists
names = []
nums = []
colors = []
valid_menu = ["1", "2", "3", "4"]

with open("text_files/simple-2.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        names.append(rec[0])
        nums.append(rec[1])
        colors.append(rec[2].title())
#disconnected from file(indentation)

ans = "y"

while ans == "y":
    choice = menu()

    if choice not in valid_menu:
        print("INVALID ENTRY!\n Please try again.\n")

    elif choice == "1": #search by name
        print("\n~Search By Name~")

        for i in range(len(names) -1):
            for j in range(len(names) - 1):
                #see if heavier value is in front of smaller value
                if names[j] > names[j + 1]:
                    #swap places - not just THIS value, but all ASSSOCIATED values!
                    swap(j, colors)
                    swap(j, names)
                    swap(j, nums)

        min = 0     #always starting value ---> First Index
        max = len(names) -1 #LAST INDEX / highest value in ascending ordered list
        mid = int((min + max) /2) #MIDDLE INDEX / middle value in ascending ordered list

        search = input("ENTER the NAME you are looking for: ")
        
        while min < max and search.lower() != names[mid].lower():
            if search.lower() < names[mid].lower():
                max = mid - 1
            else:
                #search.lower() > names[mid].lower()
                mid = mid + 1
            mid = int((min + max) /2)

        if search.lower() == names[mid].lower():
            #we found it!
            print(f"Your Search for {search} is complete, see below details")
            print(f"{'NAME':8}    {'NUM':3}  {'COLOR'}")
            print("-------------------------------------------------------")
            print(f"{names[mid]:8}    {nums[mid]:3}   {colors[mid]}")
            print("-------------------------------------------------------")
        else:
            print(f"Your Search for {search} is complete, and no information was found. ")
    
    elif choice == "2":
        print("\n~Search By Num~")

    elif choice == "3":
        print("\n~Search by Color~")

        # bubble SORT before you binary search
        for i in range(len(colors) -1):
            for j in range(len(colors) - 1):
                #see if heavier value is in front of smaller value
                if colors[j] > colors[j + 1]:
                    #swap places - not just THIS value, but all ASSSOCIATED values!
                    swap(j, colors)
                    swap(j, names)
                    swap(j, nums)
    

        min = 0     #always starting value ---> First Index
        max = len(colors) -1 #LAST INDEX / highest value in ascending ordered list
        mid = int((min + max) /2) #MIDDLE INDEX / middle value in ascending ordered list

        search = input("ENTER the COLOR you are looking for: ")
        
        while min < max and search.lower() != colors[mid].lower():
            if search.lower() < colors[mid].lower():
                max = mid - 1
            else:
                #search.lower() > names[mid].lower()
                mid = mid + 1
            mid = int((min + max) /2)

        if search.lower() == colors[mid].lower():
            #we found it!
            print(f"Your Search for {search} is complete, see below details")
            print(f"{'NAME':8}    {'NUM':3}  {'COLOR'}")
            print("-------------------------------------------------------")
            print(f"{names[mid]:8}    {nums[mid]:3}   {colors[mid]}")
            print("-------------------------------------------------------")
        else:
            print(f"Your Search for {search} is complete, and no information was found. ")
    else:
        print ("\n~EXIT~")
        ans = "X" #ans changes from "y" to end the loop (condition wil now eval as false)

print("\nThank you for using my program. \n\t GOODBYE!\n")



