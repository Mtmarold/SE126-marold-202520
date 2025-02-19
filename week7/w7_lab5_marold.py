#Matthew Marold
#SE126
#Lab 5
#02/19/2025


#--- imports ---
import csv


#--- program prompt --- Build a personal library search system using the file book_list.csv. It is set up as follows Store the file data into 1D parallel lists, then use the appropriate searching algorithms for the menu system options.Your program should give your user the following menu: Personal Library Menu 
# 1. Show All Titles – list all book data to the user alphabetically by title
#2. Search by Title – allow for an entire title or a title key word
#3. Search by Author – show all titles of the searched-for author
#4. Search by Genre - show all titles of the searched-for genre
#5. Search by Library Number – only allow for one specific library number item
#6. Show All Available – show all titles with status “available”
#7. Show All On Loan - show all titles with status “on loan”
#8. EXIT
#When your user runs any of the options 1 – 7, show all data associated with the search [Library Number, Title, Author,
#Genre, Page count, Status]. Do not allow the program to end unless the user chooses option 8 to exit. All searches
#should not be case sensitive.





def menu():
    '''This function shows a user the search menu and returns the user's choice'''
    print("\n\tPERSONAL LIBRARY MENU")
    print("\t1. Show All Titles") # – list all book data to the user alphabetically by title
    print("\t2. Show All Available")# – list all titles with status “available”
    print("\t3. Show All On Loan")# - show all titles with status “on loan”
    
    print("\t4. Search by Title") # – allow for an entire title or a title key word
    print("\t5. Search by Author")# – show all titles of the searched-for author
    print("\t6. Search by Genre")# - show all titles of the searched-for genre
    
    print("\t7. Search by Library Number")# – only allow for one specific library number item
    
    print("\t8. EXIT\n")
    
    choice = input("Enter your menu choice [1-8]: ")
    return choice
def display(x,records):
    print(f" {'LIB#':5}  {'TITLE':30}      {'AUTHOR':25}    {'GENRE':17}{'PGS':3}   {'STATUS'}")
    print("-------------------------------------------------------------------------------------------------------")
    if x != "x":
        #printing one record
        print(f"{libnums[x]:5}  {titles[x]:35}  {authors[x]:25}  {genres[x]:17}  {pgcount[x]:3}  {status[x]}")
    elif found: #the found list is checked from the main code - when it is populated (has data) this statement evals as TRUE / when found is empty, it evals as FALSE
        #printing multiples, based on length stored in 'foundList'
        for i in range(0, records):
            print(f"{libnums[found[i]]:5}  {titles[found[i]]:35}  {authors[found[i]]:25}  {genres[found[i]]:17}  {pgcount[found[i]]:3}  {status[found[i]]}")
    
    else:
        #printing full data, based on length stored in 'records'
        for i in range(0, records):
            print(f"{libnums[i]:5}  {titles[i]:35}  {authors[i]:25}  {genres[i]:17}  {pgcount[i]:3}  {status[i]}")

    print("---------------------------------------------------------------------------------------------------------\n")
def swap(i, listName):
    temp = listName[i]
    listName[i] = listName[i + 1]
    listName[i + 1] = temp
#--- variable dictionary ---

libnums = []
titles = []
authors = []
genres = []
pgcount = []
status = []
valid_menu = ["1", "2", "3", "4", "5", "6", "7", "8"]
#--- Main Executing Code ---- 

with open("text_files/book_list.csv") as csvfile:
    file = csv.reader(csvfile)


    for rec in file:

        libnums.append(int(rec[0]))
        titles.append(rec[1])
        authors.append(rec[2])
        genres.append(rec[3])
        pgcount.append(int(rec[4]))
        status.append(rec[5])
#disconnect from file

ans = "y"

while ans == "y":
    found = []
    menu_choice = menu()
        #filter for what the user chose:
    if menu_choice not in valid_menu:
        #user did not follow the menu directions; alerts to them and then they will re-enter the loop
        print("***INVALID MENU CHOICE***")
        print("Please try again.\n")
    elif menu_choice == "1":
        print("\t1. Show All Titles") # – list all book data to the user alphabetically by title
        
        #sort the data by title 
        for i in range(0, len(titles) - 1):#outter loop
            for index in range(0, len(titles) - 1):#inner loop
                #below if statement determines the sort
                #list used is the list being sorted
                # > is for increasing order, < for decreasing
                if(titles[index] > titles[index + 1]):
                    #swap data
                    swap(index, titles)
                    swap(index, libnums)
                    swap(index, authors)
                    swap(index, genres)
                    swap(index, pgcount)
                    swap(index, status)           

        # then display to the user -- "x" signifies to function that more than one location of data needs to be displayed!
        display("x", len(titles))
    
    elif menu_choice == "2":
        print("\t2. Show All Available")# – list all titles with status “available”
        
        #sequential search 
        search = "available"
        
        for i in range(0, len(status)):
            if search == status[i].lower():
                found.append(i)
        
        if not found: #this is true when the found list is empty
            print(f"I'm sorry, your search for {search} could not be completed.")
        else:
            display("x", len(found))
    
    elif menu_choice == "3":
        print("\t3. Show All On Loan")# - shlistow all titles with status “on loan”
        search = "on loan"
        for i in range(0, len(status)):
            if search == status[i].lower():
                found.append(i)
        
        if not found: #this is true when the found list is empty
            print(f"I'm sorry, your search for {search} could not be completed.")
        else:
            display("x", len(found))
    
    elif menu_choice == "4":
        print("\t4. Search by Title") # – allow for an entire title or a title key word
        
        search = input("\nEnter the TITLE or keyword of a title: ")
        
        for i in range(len(titles)):
            if search.lower() in titles[i].lower():
                found.append(i)
                
        if not found: #this is true when the found list is empty
            print(f"I'm sorry, your search for {search} could not be completed.")
        else:
            print(f"Your search for {search} is complete, please see details below: ")
            display("x", len(found))
    
    
    elif menu_choice == "5":
        print("\t5. Search by Author")# – show all titles of the searched-for author
        
        search = input("\nEnter the Author or keyword of an Author: ")
        
        for i in range(len(authors)):
            if search.lower() in authors[i].lower():
                found.append(i)
                
        if not found: #this is true when the found list is empty
            print(f"I'm sorry, your search for {search} could not be completed.")
        else:
            print(f"Your search for {search} is complete, please see details below: ")
            display("x", len(found))
    
    elif menu_choice == "6":
        print("\t6. Search by Genre")# - show all titles of the searched-for genre
        
        search = input("\nEnter the Gemre or keyword of a Genre: ")
        
        for i in range(len(genres)):
            if search.lower() in genres[i].lower():
                found.append(i)
                
        if not found: #this is true when the found list is empty
            print(f"I'm sorry, your search for {search} could not be completed.")
        else:
            print(f"Your search for {search} is complete, please see details below: ")
            display("x", len(found))
    
    elif menu_choice == "7":
        print("\t7. Search by Library Number")# – only allow for one specific library number item
        
        search = int(input("Enter the LIBRARY NUMBER you are looking for: "))
        #SORT BY LIBRARY NUMBER
        for i in range(0, len(libnums) - 1):#outter loop
            for index in range(0, len(libnums) - 1):#inner loop
                #below if statement determines the sort
                #list used is the list being sorted
                # > is for increasing order, < for decreasing
                if(libnums[index] > libnums[index + 1]):
                    #swap data
                    swap(index, titles)
                    swap(index, libnums)
                    swap(index, authors)
                    swap(index, genres)
                    swap(index, pgcount)
                    swap(index, status)
                    
        #binary search algorithm
        min = 0 
        max = len(libnums) - 1
        mid = int((min + max) / 2)
        
        while min < max and search != libnums[mid]:
            if search < libnums[mid]:
                max = mid - 1
            else:
                min = mid + 1
            mid = int((min + max) / 2)
        
        if search == libnums[mid]:
            print(f"Your search for {search} is complete, please see details below: ")
            display(mid, 0)
        else:
            print(f"Sorry, your search for {search} came up empty :[")
                
                    
    else:
        print("\t8. EXIT\n")
        ans = "x"
print ("Thank you for using my program, goodbye :]")