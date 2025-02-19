#W5 Midterm Westeros.csv
#Matthew Marold
#2/10/25
#SE126

#--- IMPORTS ------
import csv
import random


#list names
first_name = []
last_name = []
email = []
department = []
phone_ext = []
total_rec = 0
office_num = []



#open file
with open("text_files/westeros.csv") as csvfile:
    file = csv.reader(csvfile)



    for rec in file:
        total_rec += 1
        first_name.append(rec[0])
        last_name.append(rec[1])
        email.append(rec[2])
        department.append(rec[3])
        phone_ext.append(rec[4])

for i in range(0, len(first_name)):
    office_num.append(random.randint(100, 200))
#display lists
print(f"{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':3}    {'OFFICE#'}")
print("------------------------------------------------------------------------------------------")
for i in range(0, len(first_name)):
    print(f"{first_name[i]:8} {last_name[i]:10} {email[i]:30} {department[i]:23} {phone_ext[i]:3}      {office_num[i]}")
print("------------------------------------------------------------------------------------------")
for i in range(0, len(first_name)):
    office_num.append(random.randint(100, 200))


found_email = []
search_email = input("Enter the EMAIL you are looking for: ")

for i in range(0, len(email)):
    if search_email.lower() in email[i].lower():
        found_email.append(i)
if not found_email:
    print(f"Your search for {search_email} was not found! Please try again!")
else:
    print(f"Your search for {search_email} was found! ")
    print(f"{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':3}    {'OFFICE#'}")
    print("------------------------------------------------------------------------------------------")
    for i in range(0, len(found_email)):
        print(f"{first_name[found_email[i]]:8} {last_name[found_email[i]]:10} {email[found_email[i]]:30} {department[found_email[i]]:23} {phone_ext[found_email[i]]:3}    {office_num[found_email[i]]}")

found_dep = []
search_dep = input("Enter the Department you are looking for: ")

# its ok thank u katie :]

for i in range(0, len(department)):
    if search_dep.lower() in department[i].lower():
        found_dep.append(i)
if not found_dep:
    print(f"Your search for {search_dep} was not found! Please try again!")
else:
    print(f"Your search for {search_dep} was found!")
    print(f"{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':3}     {'OFFICE#'}")
    print("-----------------------------------------------------------------------------------------")
    for i in range(0, len(found_dep)):
        print(f"{first_name[found_dep[i]]:8} {last_name[found_dep[i]]:10} {email[found_dep[i]]:30} {department[found_dep[i]]:23} {phone_ext[found_dep[i]]:3} {office_num[found_dep[i]]}")
print(f"Total Records processed: {total_rec}")

    







