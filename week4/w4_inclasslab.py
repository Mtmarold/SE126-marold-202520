#W4 in class lab
#Matthew Marold
#1/27/2025
#SE126

#PROGRAM PROMPT: Write a program that reads the data file (below) and stores the data into 1D parallel lists (remember, one list for every field).  Once the lists are populated (and the file is "closed"), process the lists to reprint the file data, record by record as they originally appear in the file.
#Next, reprocess the lists to find each student's current average score, letter grade equivalent, and the class average.  While processing in the for loop, store each student's average into a new list called 'num_avg' and their letter grade into a list called 'let_avg'. Then, print each student's full information, record by record including average score and average letter equivalent.  After this print of the original file data from the lists, print to the console the total number of student's in the class along with the class numeric average. 


#this file uses: class_grades-2.csv

#--IMPORTS-------
import csv

#-- FUNCTIONS -----------
def letter(num):
    if num >= 90:
        let = "A"
    elif num >= 80:
        let = "B"
    elif num >= 70:
        let = "C"
    elif num >= 60:
        let = "D"
    elif num < 50:
        let = "F"
    else:
        let = "ERROR"

    return let #let value replaces the function call in the main executing code
    
#-- MAIN EXECUTING CODE ------

#create empty lists to hold the file data
fname = []
lname = []
test1 = []
test2 = []
test3 = []
total_students = 0
with open("text_files/class_grades-2.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        total_students += 1
        #append the file data into appropriate list 
        fname.append(rec[0])
        lname.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

#disconnected from file -- can still access the stored data via the lists

#process the list data to calc an avg score for each student, and find the letter grade equivalent
num_avg = []
let_avg = []
for i in range(0, len(fname)):
    a = (test1[i] + test2[i] + test3[i]) /3
    num_avg.append(a)

    l = letter(a)#return value of letter() stored to l
    let_avg.append(l) #can also do: let_avg.append(letter(a))
    # or num_avg.append(test1[i] + test2[i] + test3[i]) /3
    #add avg to num_avg list

#process the lists to display all student data back to user
print(f"{'FNAME':10}    {'LNAME':10} {'T1':3}   {'T2':3}   {'T3':3}  {'# AVG':6}   {'L AVG'}")
print("-------------------------------------------------------------------------------------")
for i in range(0, len(fname)):
    print(f"{fname[i]:10}  {lname[i]:10}  {test1[i]:3}   {test2[i]:3}   {test3[i]:3}  {num_avg[i]:6.2f}     {let_avg[i]}")

print("-----------------------------------------------------------------------------------------------------------")

print("\n\n Welcome to the Student Search program\n\n")

answer = input("Would you like to begin searching? [y/n]: ").lower()

while answer == "y":


    #get search type from user 
    print("\tSEARCH MENU OPTIONS")
    print("1. Search by LAST name")
    print("2. Search by FIRST name")
    print("3. Search by LETTER GRADE")
    print("4. EXIT")

    search_type = input("Enter your search type [1-4]: ")

    if search_type == "1":
        print("\t SEARCH BY LAST NAME")
        found = -1 #invalid index number, will use to check later to see if a student has been found


        #get search item from user
        search_name = input("Enter the LAST NAME of the student you are searching for:  ")


        #perform search
        for i in range(0, len(lname)):
            #the FOR loop allows for the "sequence" part -> FROM BEGINNING TO END
            if search_name.lower() == lname[i].lower():
                #the IF STATEMENT allows for the "search" part
                found = i #make found current index, can be used later to display
        #display results
        if found != -1:
            #last name has been found! display data
            print(f"Your search for {search_name} was FOUND!")
            print(f"{'FNAME':10}  {'LNAME':10}  {'T1':3}  {'T2':3}  {'T3':3}  {'# AVG':6}  {'L AVG'}")
            print("-------------------------------------------------------------------------------------")
            print(f"{fname[found]:10}  {lname[found]:10}  {test1[found]:3}   {test2[found]:3}   {test3[found]:3}  {num_avg[found]:6.2f}   {let_avg[found]}")
        else:
            print(f"Your search for {search_name} was *NOT* FOUND")
            print(f"This is a cAsE sEnSiTiVe program - check ur spelling and casing and try again.")
    elif search_type == "3":
        print("\t SEARCH BY LETTER GRADE")

        found = [] #invalid index number, will use to check later to see if a student has been found


        #get search item from user
        search_grade = input("Enter the LETTER GRADE of the student you are searching for:  ").upper()


        #perform search
        for i in range(0, len(let_avg)):
            #the FOR loop allows for the "sequence" part -> FROM BEGINNING TO END
            if search_grade.upper() == let_avg[i]:
                #the IF STATEMENT allows for the "search" part
                found.append(i) #make found current index, can be used later to display


        if not found: #this list is empty
            print(f"Your search for {search_grade} was *NOT* FOUND")
            print(f"This is a cAsE sEnSiTiVe program - check ur spelling and casing and try again.")
            #last name has been found! display data


        else:
            print(f"Your search for {search_grade} was FOUND!")
            print(f"{'FNAME':10}  {'LNAME':10}  {'T1':3}  {'T2':3}  {'T3':3}  {'# AVG':6}  {'L AVG'}")
            print("-------------------------------------------------------------------------------------")
            for i in range(0, len(found)):
                print(f"{fname[found[i]]:10}  {lname[found[i]]:10}  {test1[found[i]]:3}   {test2[found[i]]:3}   {test3[found[i]]:3}  {num_avg[found[i]]:6.2f}   {let_avg[found[i]]}")


    elif search_type == "2":
        print("\t SEARCH BY FIRST NAME")
        found = -1 #invalid index number, will use to check later to see if a student has been found


        #get search item from user
        search_name = input("Enter the FIRST NAME of the student you are searching for:  ")


        #perform search
        for i in range(0, len(fname)):
            #the FOR loop allows for the "sequence" part -> FROM BEGINNING TO END
            if search_name.lower() == fname[i].lower():
                #the IF STATEMENT allows for the "search" part
                found = i #make found current index, can be used later to display
        #display results
        if found != -1:
            #last name has been found! display data
            print(f"Your search for {search_name} was FOUND!")
            print(f"{'FNAME':10}  {'LNAME':10}  {'T1':3}  {'T2':3}  {'T3':3}  {'# AVG':6}  {'L AVG'}")
            print("-------------------------------------------------------------------------------------")
            print(f"{fname[found]:10}  {lname[found]:10}  {test1[found]:3}   {test2[found]:3}   {test3[found]:3}  {num_avg[found]:6.2f}   {let_avg[found]}")

        else:
            print(f"Your search for {search_name} was *NOT* FOUND")
            print(f"This is a cAsE sEnSiTiVe program - check ur spelling and casing and try again.")

  
    elif search_type == "4":
        answer = "n"
        print("Thank you for using my program, goodbye :)")
    else:
        print("********INVALID ENTRY********")
    
    if search_type == "1" or search_type == "2" or search_type == "3": #only when user doesnt specify 3 to exit
        answer = input("Would you like to search again? [y/n]:  ").lower()
    
num_avg = []

#process the current student data to find and store each student's test score avg to the avg list

for i in range(0, len(test1)):
    a = (test1[i] + test2[i] + test3[i]) /3
    num_avg.append(a)
    #could also: avg.append((test1[i] + test2[i] + test3[i])) /3




    #find current average of class by processing the avg list data
total_avg = 0
for i in range(0, len(num_avg)):
    total_avg += num_avg[i] #adds each avg value to the total avg variable
class_avg = total_avg / len(num_avg)
#calculate the average
print(f"\nThe CLASS AVERAGE of these {len(num_avg)} students is: {class_avg:.2f}")
print(f"Total Students in Class:  {total_students}")