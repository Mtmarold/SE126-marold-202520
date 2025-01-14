#Matthew Marold
#in class lab text file handling
#SE126
#1/13/25

#Program Prompt:


#Variable Dictionary:
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

with open("text files/classLab2.csv") as csvfile:
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

        total_records += 1
    print(f"There are total number of {total_records} records processed and {rooms_over} rooms are over the limit")
            


        

