#W6D2 - Binary Search + Bubble Sort

#this file uses: party.csv

#program prompt - BUILD a repeatable menu-driven program to access and search for data within the file 

#--IMPORTS-----------------------------------
import csv

#--FUNCTIONS---------------------------------
def display():
    print(f"{practice}")

def swap(i, listName):
    temp = listName[i]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp
    return listName
#main executing code ---------------------------------------
class_type = []
name = []
meaning = []
culture = []

practice = ["Ray",
            "Rob",
            "Matt",
            "Tyler",
            "Chris"]

with open("text_files/party.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        class_type.append(rec[0])
        name.append(rec[1])
        meaning.append(rec[2])
        culture.append(rec[3])
#disconnected from file --------------------------------------------------
#BUBBLE SORT----------------------------------------

for i in range(0, len(name) - 1):#outter loop

    print("OUTER LOOP! i = ", i)


    for index in range(0, len(name) - 1):#inner loop

        print("\t INNER LOOP! k = ", index)

        #below if statement determines the sort
        #list used is the list being sorted
        # > is for increasing order, < for decreasing

        if(name[index] > name[index + 1]):

            print("\t\t SWAP! ", name[index], "<-->", name[index + 1])

            #if above is true, swap places!
            swap(index, name)

            #swap all other values
            swap(index, class_type)
            swap(index, meaning)
            swap(index, culture)
            
            display("x", 0, len(name))
