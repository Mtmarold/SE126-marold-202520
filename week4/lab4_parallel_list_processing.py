#Matthew Marold
#Lab 4
#2/1/2025
#SE126

#imports
import random
import csv

# House to Department
house_to_department = {
    'House Stark': 'Research & Dev.',
    'House Targaryen': 'Marketing',
    'House Tully': 'Human Resources',
    'House Lannister': 'Accounting',
    'House Baratheon': 'Sales',
    "The Night's Watch": 'Auditing'
}

#House to Phone Extension Ranges
house_to_extension_range = {
    'House Stark': (100, 199),
    'House Targaryen': (200, 299),
    'House Tully': (300, 399),
    'House Lannister': (400, 499),
    'House Baratheon': (500, 599),
    "The Night's Watch": (600, 699)
}

#Parallel Lists
first_names = []
last_names = []
ages = []
screen_names = []
house_allegiances = []
emails = []
departments = []
phone_extensions = []

with open("text_files/got_emails.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        first_names.append(rec[0])
        last_names.append(rec[1])
        ages.append(int(rec[2]))
        screen_names.append(rec[3])
        house_allegiances.append(rec[4])

        # Generate Email
        email = f"{rec[3]}@westeros.net"
        emails.append(email)

        # Assign Department
        department = house_to_department.get(rec[4], 'Unknown')
        departments.append(department)

        #Assign Unique Phone Extension
        ext_min, ext_max = house_to_extension_range.get(rec[4], (700, 799))
        extension = random.randint(ext_min, ext_max)
        while extension in phone_extensions:
            extension = random.randint(ext_min, ext_max)
        phone_extensions.append(extension)

# Display the data
print(f"{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':3}")
print("-------------------------------------------------------------------------------")
for i in range(len(first_names)):
    print(f"{first_names[i]:8} {last_names[i]:10} {emails[i]:30} {departments[i]:23} {phone_extensions[i]:3}")

#Write data to westeros.csv
file = open("westeros.csv", "w",)
file.write("First Name,Last Name,Email,Department,Phone Extension\n")
#to avoid the extra line in westeros.csv
for i in range(len(first_names)):
    if i != len(first_names) - 1:
        file.write(f"{first_names[i]},{last_names[i]},{emails[i]},{departments[i]},{phone_extensions[i]}\n")
    else:
        file.write(f"{first_names[i]},{last_names[i]},{emails[i]},{departments[i]},{phone_extensions[i]}")

#close the file    
file.close
#output data
print("-------------------------------------------------------------------------------")
print("\nThe file 'westeros.csv' has been successfully created and closed.")
print(f"Total number of employees: {len(first_names)}")
department_counts = {} #list
# Counting the different Departments
for dept in departments:
    if dept in department_counts:
        department_counts[dept] += 1
    else:
        department_counts[dept] = 1

for dept, count in department_counts.items():
    print(f"{dept}: {count} employees")
