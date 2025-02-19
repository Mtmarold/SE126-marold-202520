#W4D1 - Sequential Search

#PROGRAM PROMPT: We will continue to work with the class_grades.csv file, as used in the W3D2 Demo. We will practice connecting to a file


#this file uses: class_grades.csv

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

with open("text_files/class_grades.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
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
print(f"{'FNAME':10}      {'LNAME':10}     {'T1':3}     {'T2':3}    {'T3':3}   {'# AVG':6}   {'L AVG'}")
print("-------------------------------------------------------------------------------------")
for i in range(0, len(fname)):
    print(f"{fname[i]:10}  {lname[i]:10}  {test1[i]:3}   {test2[i]:3}   {test3[i]:3}  {num_avg[i]:6.2f}   {let_avg[i]}")

print("-----------------------------------------------------------------------------------------------------------")

print("\n\n Welcome to the Student Search program\n\n")

answer = input("Would you like to begin searching? [y/n]: ").lower()

while answer == "y":


    #get search type from user 
    print("\tSEARCH MENU OPTIONS")
    print("1. Search by LAST name")
    print("2. Search by LETTER grade")
    print("3. EXIT")

    search_type = input("Enter your search type [1-3]: ")

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
    elif search_type == "2":
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

    elif search_type == "3":
        print("\t EXIT")
    else:
        print("********INVALID ENTRY********")
    
    if search_type == "1" or search_type == "2": #only when user doesnt specify 3 to exit
        answer = input("Would you like to search again? [y/n]:  ").lower()
