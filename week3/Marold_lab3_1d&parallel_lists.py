#Lab 3 - 1D & Parallel Lists
#Matthew Marold
#1/25/2025
#SE126

#program prompt -- This lab is a continuation of the Voter Registration Lab from SE116.  The original prompt is as follows: (Source: QBasic Fundamentals and Style, Quasney, Maniotes, Foremant; P. 190 #3) Construct a program that will analyze potential voters. The program should generate the following totals:
#Number of individuals not eligible to register.
#Number of individuals who are old enough to vote but have not registered.
#Number of individuals who are eligible to vote but did not vote.
#Number of individuals who did vote.
#Number of records processed.


#imports -----------
import csv



#variables -----
#reg = registered
#age = age
#voted --- amount of people who voted
#idNum --  Identification number
#not_eligible_to_register - not old enough to register
#registered_didnt_vote - registered to vote but didnt actually vote
#reg_voted - user registered AND voted
#old_enough_not_reg - old enough to register but didnt register


#------MAIN CODE BELOW-------------------
#initializing vars and lists
total_records = 0
idnum = []
age = []
registered = []
voted = []
not_eligible_to_register = 0
old_enough_not_reg = 0
registered_didnt_vote = 0
reg_voted = 0
with open ("text_files/voters_202040.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        total_records += 1


        
        #initializing lists
        idnum.append(rec[0])
        age.append(rec[1])
        registered.append(rec[2])
        voted.append(rec[3])

        #header    
    print(f"{'ID Number':10}{'Age':3}   {'Registered':5}    {'Voted':6}")
    print("-------------------------------------------------")
    # process and display each record
    for index in range(len(idnum)):
        if int(age[index]) < 18:
            not_eligible_to_register += 1   
        elif registered[index] == "N":
            old_enough_not_reg += 1
        elif registered[index] == "Y" and voted[index] == "N":
            registered_didnt_vote += 1
        elif registered[index] == "Y" and voted[index] == "Y":
            reg_voted += 1
        #output lists
        print(f"{idnum[index]:<10}{age[index]:<5}    {registered[index]:5}       {voted[index]:<6}")
#output results 
print("-------------------------------------------------")
print("\nSummary of Voter Analysis:")
print(f"Total Records Processed: {total_records}")
print(f"Number of individuals not eligible to register or vote: {not_eligible_to_register}")
print(f"Number of individuals old enough to vote but not registered: {old_enough_not_reg}")
print(f"Number of individuals eligible to vote but didn't vote: {registered_didnt_vote}")
print(f"Number of individuals who voted: {reg_voted}")
print("Thank you for using my voter analysis program :D")
