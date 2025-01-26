#Lab 3 - 1D & Parallel Lists
#Matthew Marold
#1/25/2025
#SE126

#imports --
import csv


#program prompt -- This lab is a continuation of the Voter Registration Lab from SE116.  The original prompt is as follows: (Source: QBasic Fundamentals and Style, Quasney, Maniotes, Foremant; P. 190 #3) Construct a program that will analyze potential voters. The program should generate the following totals:
#Number of individuals not eligible to register.
#Number of individuals who are old enough to vote but have not registered.
#Number of individuals who are eligible to vote but did not vote.
#Number of individuals who did vote.
#Number of records processed.


#variable dictionary --






#---- MAIN CODE BELOW --------
#initialize variables / lists
total_records = 0
idnum = []
age = []
registered = []
voted = []



with open ("text_files/voters_202040.csv") as csvfile:
    file = csv.reader
    for rec in file:
        total_records += 1



        idnum.append(rec[1])


        age.append(rec[2])

        registered.append(rec[3])

        voted.append(rec[4])

        if rec[2] < "18":
            
