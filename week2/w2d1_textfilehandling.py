#w2D1 - Text File Handling - Introduction 

#STEP 1: Import the csv (comma separated value) library
import csv

total_records = 0 #the total number of records (rows) in the file

#connecting to the files path - switch \ to /
#----- Connected to file ----------------
print (f"\n{'NAME':10} \t {'Num':3} \t {'COLOR'}")
#header print
print ("----------------------------------------")
with open ("text_files/simple.csv") as csvfile:
    #indent 1 level (new block)

    #allow processor to read teh file data
    file = csv.reader(csvfile)

    #loop through every record(row) in the file
    for record in file:

        #add +1 to total_records
        total_records += 1

       # print(record) #the list vew of each record(row)

        name = record[0]
        number = record[1]
        color= record[2]
        print(f"{name:10} \t {number:3} \t {color.title()}")
print ("------------------------------------------")
#------ disconnected from file --------
print(f"\nTOTAL RECORDS: {total_records}\n")