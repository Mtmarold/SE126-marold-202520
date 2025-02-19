#Matthew Marold
#In class lab w3 d2
#1/21/2025
#SE126



#program prompt ------ 

#variable dictionary ----------
#type - desktop or laptop
#brand - dell or hp
#cpu - i5 or i7
#ram - 08 or 16
#hard_drive - 
#num_hd
#second_drive
#os - operating system
#yr - year computer was bought

#imports ---------
import csv
#functions -------

#------ MAIN PROGRAM CODE BELOW ------

total_records = 0
type = []
brand = []
processor = []
ram = []
hdd1 = []
numhdd = []
hdd2 = []
os = []
year = []
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

        type.append(rec[0])
        if type == "D":
            type = "Desktop"
        elif type == "L":
            type = "Laptop"


        brand.append(rec[1])
        if brand == "DL":
            brand = "Dell"
        elif brand == "HP":
            brand = "HP"
        elif brand == "GW":
            brand = "Gateway"
        


        processor.append(rec[2])

        ram.append(rec[3])

        hdd1.append(rec[4])

        numhdd.append(rec[5])

        replaceD = 0
        replaceL = 0
        if numhdd == "1":
            second_drive = " "
            os.append(rec[6])
            year.append(rec[7])
        elif numhdd == "2":
            hdd2.append(rec[6])
            os.append(rec[7])
            year.append(rec[8])
    for index in range (0, len(year)): 
        if year[index] <= 16 and type[index] == "Desktop":
            replaceD += 1
            
        elif year[index] <= 16 and type[index] == "Laptop":
            replaceL += 1
            #if type[index] == "Desktop":
                #replaceD += int(2000)
            #elif type[index] == "Laptop":
                #replaceL += int(2000)
        #display list output
    #print(f"{type:10}{brand:10}{processor:10}{ram:5}{hdd1:10}{numhdd:10}{second_drive:10}{os:5}{year:5}")
    rep_cost_d = replaceD * 2000
    rep_cost_l = replaceL * 1500
    print(f"To replace 8 it will cost: ${replaceD}")
    print(f"To Replace 2 it will cost: ${replaceL}")
print("-------------------------------------------------------------------------------------------")
print(f"\nTotal records processed: {total_records}")

print("Thank you for using my program, goodbye :]")