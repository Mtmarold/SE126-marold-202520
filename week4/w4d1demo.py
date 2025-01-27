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
        