#Matthew Marold
#W6D1 Demo - Searching Algorithms: Binary vs Sequential Search

#--- IMPORTS --- 
import csv


#variable Dictionary ---
lib_num = [] #only ordered field
title = []
author = []
genres = []
pages = []

with open("text_files/library_books.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        lib_num.append(rec[0])
        title.append(rec[1])
        author.append(rec[2])
        genres.append(rec[3])
        pages.append(rec[4])

print(f"{'LIB#':5}  {'TITLE':25}  {'AUTHOR':15}  {'GENRE':20} {'PAGES':5}")
print("------------------------------------------------------------------------------")
for i in range(0, len(lib_num)):
    print(f"{lib_num[i]:5} {title[i]:25}  {author[i]:15}   {genres[i]:20}   {pages[i]:5}")
print("---------------------------------------------------------------------------------")

#SEQUENTIAL SEARCH: allow a user to search for a speific title
#title[] is not ORDERED

found = []
search_num = input("Which title are you looking for? ")
seq_count = 0

for i in range(0, len(lib_num)):
    seq_count += 1
    if search_num.lower() in lib_num[i].lower():
        found.append(i)
print(f"SEARCH ITERATIONS: {seq_count}")
if not found:
    #found list is still empty meaning to matches to our search term were found
    print(f"Sorry, your search for {search_num} was not found :[")
else:
    print(f"Your search for {search_num} was found :]")
    
    print(f"{'LIB#':5}  {'TITLE':25}  {'AUTHOR':15}  {'GENRE':20} {'PAGES':5}")
    print
    ("---------------------------------------------------------------------------")
    for i in range(0,len(found)): #found is a list of locations (indexes)
            print(f"{lib_num[i]:5} {title[i]:25}  {author[i]:15}   {genres[i]:20}   {pages[i]:5}")  
    print("---------------------------------------------------------------------------------")



    #BINARY SEARCH: must be performed on ORDERED lists (lib_num)

    min = 0
    max = len(lib_num) - 1
    mid = int((min + max) / 2)

    bin_count = 0

while min < max and search_num != lib_num[mid]:
    #not exahausted of potential values yet
    if search_num < lib_num[mid]:
        #everything after mid point is not possible
        max = mid - 1
    else:
        #everything before mid point is not posssible
        min = mid + 1
    mid = int((min + max) / 2)
    bin_count += 1

    print(f"BINARY SEARCH ITERATIONS: {bin_count}")

if search_num == lib_num[mid]:
    print(f"Your Search for {search_num} was found!")
    print(f"{'LIB#':5}  {'TITLE':25}  {'AUTHOR':15}  {'GENRE':20} {'PAGES':5}")
    print("------------------------------------------------------------------------------")
    print(f"{lib_num[mid]:5} {title[mid]:25}  {author[mid]:15}   {genres[mid]:20}   {pages[mid]:5}")
    print("---------------------------------------------------------------------------------")
