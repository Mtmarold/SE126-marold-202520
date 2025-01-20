#Matthew Marold
#in class lab text file handling
#SE126 w2d2
#1/13/25

#Program Prompt:Write a program that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list. After the file is completely processed the program should display the number of records processed and the number of rooms that are over the limit.


#Variable Dictionary:
#total_records - number of records in the file
#rooms_over - rooms over capacity limit
#room - room name
#max - max capacity of room
#ppl - number of ppl in the room






def difference(people,capacity):
    '''This function is passed 2 values and returns the difference between them'''
    diff = capacity - people
    return diff
#------Imports-------
import csv
#header print
total_records = 0
rooms_over = 0
print(f"\n {'Room':20}      {'Max':5}   {'PPL':5}    {'Over'}")
print("-------------------------------------------------")

with open("text_files/classLab2.csv") as csvfile:
    #indent
    #processor read file data
    file = csv.reader(csvfile)

    for record in file:
        total_records += 1
        #below code occurs for every record (row) in the text file

        #assign each field data value to a friendly var name

        #print(record) 

        room = record[0]
        max =int(record[1])
        ppl = int(record[2])


        remaining = difference(ppl, max)
    
        if remaining < 0:
            rooms_over += 1
            print(f"{room:20}\t {max:5}\t {ppl:5}\t {abs(remaining):5}")

        
    print(f"There are total number of {total_records} records processed and {rooms_over} rooms are over the limit")
            


        

