#Matthew Marold
#in class lab text file handling
#SE126
#1/13/25

#Program Prompt:


#Variable Dictionary:

#------Imports-------
import csv
#header print
print(f"\n{'Room':5}\t{'Max':3}\t{'Min':3}\t{'Over'}")
total_records = 0

with open ("text files/classLab2.csv") as csvfile:
    #indent
    #processor read file data
    file = csv.reader(csvfile)

    for record in file:
        total_records += 1

        #print(record) 

    room = record[0]
    capacity =int(record[1])
    people = int(record[2])

    if people > capacity:
        over = (people - capacity)
            

    
    print(f"{room:5}\t {capacity:3}\t {people:2}\t {over}")
    print(f"There are total number of {total_records} records processed and {over} rooms are over the limit")
            


        

