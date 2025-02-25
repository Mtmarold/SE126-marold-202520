#Matthew Marold
#Dictionary and Text file data Demo


#---IMPORTS----------------
import csv

#-- MAIN EXECUTING CODE ----------------

#mini review on dictionaries

library = {
    #indexes are strings set by the developer
    #'key' : value
    "1230" : "Red Rising",
    "1231" : "The Little Prince",




}

with open("text_files/dictionary_file.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #add each records data as a new key + value pair from the text file
        #key --> rec[0] ; value --> rec[1]
        library.update({rec[0]  :  rec[1]})
        #when using the update method ---- > pass ('key'  :   value)

#disconnect from file
print(f"{'key':6}\t{'TITLE'}")
print("-" * 50)
for key in library:
    #for every key and value pair found within the library collection / dictionary / structure
    print(f"{key:6}\t {library[key]}")
print("-" * 50)

#SEQUENTIAL SEARCH FOR A TITLE
search = input("ENTER the TITLE you are looking for:  ")
found = 0


for key in library:
    if search.lower() == library[key].lower():
        found = key

if found != 0:
    print(f"\n KEY :{found:6}\tTITLE : {library[found]}")
else:
    print(f"\nYour search for {search} came up empty :[")


#BINARY SEARCH for LIBRARY NUMBER (dictionary keys)

#type() returns the class type of the data passed to it
if type(library) is dict:
    print("'library' is a dictionary!")
