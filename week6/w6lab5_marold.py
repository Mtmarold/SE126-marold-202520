#Matthew Marold
#2/13/2025
#SE126

#imports
import csv

#program prompt --Store the file data into 1D parallel lists, then use the appropriate searching algorithms for the menu system options. Your program should give your user the following menu: Personal Library Menu
#1. Show All Titles – list all book data to the user alphabetically by title
#2. Search by Title – allow for an entire title or a title key word
#3. Search by Author – show all titles of the searched-for author
#4. Search by Genre - show all titles of the searched-for genre
#5. Search by Library Number – only allow for one specific library number item
#6. Show All Available – show all titles with status “available”
#7. Show All On Loan - show all titles with status “on loan”



#variable dictionary ---- 


#MAIN CODE BELOW --------
#list creation
libnum = []
title = []
author = []
genre = []
page_ct = []
status = []
total_records = 0
with open("text_files/book_list.csv") as csvfile:
    file = csv.reader(csvfile)
    

    for rec in file:
        total_records += 1
        #adding to lists
        libnum.append(rec[0])
        title.append(rec[1])
        author.append (rec[2])
        genre.append(rec[3])
        page_ct.append(rec[4])
        status.append(rec[5])