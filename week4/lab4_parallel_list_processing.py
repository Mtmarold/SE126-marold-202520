#Matthew Marold
#Lab 4
#2/1/2025
#SE126

#imports
import random
import csv

#program prompt -
#first_names = 
#last_names = 
#ages = 
#screen_names = 
#house_allegiances = 
#emails = 
#departments = 
#phone_extensions = 

#var dictionary -

# House to Department and Phone Extension Ranges
house_info = {
    'House Stark': ('Research & Development', (100, 199)),
    'House Targaryen': ('Marketing', (200, 299)),
    'House Tully': ('Human Resources', (300, 399)),
    'House Lannister': ('Accounting', (400, 499)),
    'House Baratheon': ('Sales', (500, 599)),
    "The Night's Watch": ('Auditing', (600, 699))
}

# Parallel Lists
first_names = []
last_names = []
ages = []
screen_names = []
house_allegiances = []
emails = []
departments = []
phone_extensions = []

with open("text_files/got_emails.csv") as file:
    next(file)  # Skip header if present

    for rec in file:
        rec = rec.strip().split(',')
        first_names.append(rec[0])
        last_names.append(rec[1])
        ages.append(int(rec[2]))
        screen_names.append(rec[3])
        house_allegiances.append(rec[4])

        #Generate Email
        email = f"{rec[3]}@westeros.net"
        emails.append(email)

        #Assign Department and Phone Extension
        department, (ext_min, ext_max) = house_info.get(rec[4], ('Unknown', (700, 799)))
        departments.append(department)

        #Ensure unique phone extensions
        extension = random.randint(ext_min, ext_max)
        while extension in phone_extensions:
            extension = random.randint(ext_min, ext_max)
        phone_extensions.append(extension)

# Display the data
for i in range(len(first_names)):
    print(f"Name: {first_names[i]} {last_names[i]}")
    print(f"Age: {ages[i]}")
    print(f"Department: {departments[i]}")
    print(f"Email: {emails[i]}")
    print(f"Phone Extension: {phone_extensions[i]}")
    print("-----------------------------------------")