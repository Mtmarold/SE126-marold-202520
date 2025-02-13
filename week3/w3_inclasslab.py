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
replaceD = 0
replaceL = 0
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
#print(f"\n{'Type':10}{'Brand':10}{'CPU':10}{'RAM':5}{'1st Disk':10}{'Num HDD':10}{'2nd Disk':10}{'OS':5}{'YR':5}")
with open("text_files/filehandling.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        total_records += 1

    #indent 1 level (new block)

    #allow processor to read the file data

        #lists

        type.append(rec[0])


        brand.append(rec[1]) 
        


        processor.append(rec[2]) #amd took over

        ram.append(rec[3]) #16 gb ddr 5 or else

        hdd1.append(rec[4]) #ssd please

        numhdd.append(rec[5]) #if u dont have 2 wyd bro

        if rec[5] == "1":
            second_drive = " "
            os.append(rec[6])
            year.append(rec[7])
        elif rec[5] == "2":
            hdd2.append(rec[6])
            os.append(rec[7])
            year.append(rec[8])
    for index in range (0, len(year)): 
        if year[index] <= "16" and type[index] == "D":
            replaceD += 1
        elif year[index] <= "16" and type[index] == "L":
            replaceL += 1
        
    rep_desktop = replaceD * 2000
    rep_laptop = replaceL * 1500

        #display list output
    #print(f"{type[index]:10}{brand[index]:10}{processor[index]:10}{ram[index]:5}{hdd1[index]:10}{numhdd[index]:10}{hdd2[index]:10}{os[index]:5}{year[index]:5}")
print("-------------------------------------------------------------------------------------------")
print(f"To replace {replaceD} Desktops it will cost: ${rep_desktop}")
print(f"To Replace {replaceL} Laptops it will cost: ${rep_laptop}")
print(f"\nTotal records processed: {total_records}")
print("-------------------------------------------------------------------------------------------")
print("Thank you for using my program, goodbye :]")