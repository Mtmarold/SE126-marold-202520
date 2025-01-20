#Matthew Marold
#lab 2
#1/18/2025
#SE126


#program description - you have been asked to produce a report that lists all the computers in the csv file filehandling.csv. Your report should look like the following sample output. The last line should print the number of computers in the file.

#variable dictionary -
#type - desktop or laptop
#brand - dell or hp
#cpu - i5 or i7
#ram - 08 or 16
#hard_drive - 
#num_hd
#second_drive
#os - operating system
#yr - year computer was bought 

#--------- imports ----------
import csv
total_records = 0

#------ MAIN PROGRAM CODE BELOW ------
#------Connected to File--------
#header
print(f"\n{'Type':10}{'Brand':10}{'CPU':10}{'RAM':5}{'1st Disk':10}{'Num HDD':10}{'2nd Disk':10}{'OS':5}{'YR':5}")
print("--------------------------------------------------------------------------------------------")
with open("text_files/filehandling.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        total_records += 1

    #indent 1 level (new block)

    #allow processor to read the file data

        #

        type = rec[0]
        if type == "D":
            type = "Desktop"
        elif type == "L":
            type = "Laptop"


        brand = rec[1]
        if brand == "DL":
            brand = "Dell"
        elif brand == "HP":
            brand = "HP"
        elif brand == "GW":
            brand = "Gateway"
        


        processor = rec[2]

        ram = rec[3]

        hard_drive = rec[4]

        num_hd = rec[5]


        if num_hd == "1":
            second_drive = " "
            os = rec[6]
            year = rec[7]
        elif num_hd == "2":
            second_drive = rec[6]
            os = rec[7]
            year = rec[8]
        #display list output
        print(f"{type:10}{brand:10}{processor:10}{ram:5}{hard_drive:10}{num_hd:10}{second_drive:10}{os:5}{year:5}")
print("-------------------------------------------------------------------------------------------")
print(f"\nTotal records processed: {total_records}")

print("Thank you for using my program, goodbye :]")

        