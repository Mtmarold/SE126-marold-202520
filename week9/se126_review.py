#W9D2 - SE126 Course Review

#---IMPORTS----------------------------------------------------
import csv


#---FUNCTIONS--------------------------------------------------



#---MAIN EXECUTING CODE----------------------------------------

#creation & population of lists 
names_list = ["Abby", "Bobby", "Carol"]
print(names_list)       #entire list
print(names_list[0])    #first value  
print(names_list)       #last value

#creation & population of dictionaries
people_dictionary ={
    #"key" : value
}


#gaining data from a text file 
with open("text_files/dragons.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        print() #we will replace this during demo

        #adding data to a list 


        #adding data to a dictionary



#processing data from collections
print(f"{'NAMES':12} {'RIDERS':20}  {'NUM':3}   {'COLOR1':8} {'COLOR@'}")
print("-" * 75)
for i in range(0, len(names)):
    print(f"")
print("-" * 75)

#searching & sorting
#BINRARY SEARCH *requires* the sorting of data before searching
#we must also ensure the collection we search through is populated with unique values / no repeats
def swap(j, listName):
    temp = listName [j]
    listName[j] = listName[j + 1]
    listName[j + 1] = temp

#bubble sort algorithm - a loop in a loop
for i in range(len(names) -1)
    for j in range(len(names) - 1)
        if names[j] > names[j + 1]
            swap




#2D lists - lists of lists! 