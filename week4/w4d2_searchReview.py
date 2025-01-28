#W4D2 - Sequential Search Review + Creating & Writing to text files

#PROGRAM PROMPT: In the W4D2 demo, we will review utilizing sequential search for simple singular and multi returns. We will then create and write data to a text file using Python.

#-- IMPORTS -----------------------
import csv
#--FUNCTIONS---------------------------------------

#---MAIN EXECUTING CODE-------------------------
dragons = []
riders = []
count = []
color1 = []
color2 = []

with open("text_files/dragons.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        dragons.append(rec[0])
        riders.append(rec[1])
        count.append(rec[2])
        color1.append(rec[3])
    

    if rec[2] == "2":
        color2.append(rec[4])
    else:
        color2.append("---")
        

