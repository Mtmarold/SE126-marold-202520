#Matthew Marold
#W8D1 Demo 
#SE126

#Dictionaries in Python are a collection set similar to associative arrays in JavaScript but also look similar to JS object builds. Most importantly, they store data in key and value pairs. They keys are referred to as properties and the values can be any data type. 

#------------ IMPORTS ----------------


#------------ MAIN EXECUTING CODE ---------------

#start by creating a populated dictionary


myCar = {
    #'key' : value,
    "make": "Ford",
    "model": "SE Hatchback",
    "year": 2014,
    "name": "Gwendoline",
    "color": "black",
    #keys cannot be repeated / no duplicated allowed
    #"color" : "red"
}

#display the entire dictionary -> 'myCar'
print(myCar)

#display just the ' make ' and 'model' values of the dictionary 'myCar'
print(f"My car is a {myCar['make']} {myCar['model']}")

#kes cannot be repeated within a dictionary, but they can be reused across unique dictionary names: myCar vs yourCar
yourCar = {
    #'key' : value,
    "make": "GMC",
    "model": "Canyon",
    "year": 2019,
    "name": "Jolly",
    "color": "black",
    "friends": ["Duncan", "Matt", "Ray"],
    #keys cannot be repeated / no duplicated allowed
    #"color" : "red"
}

print(f"My car is a {yourCar['make']} {yourCar['model']}")

print(f"{yourCar["friends"][2]}")

for key in myCar:
    print(f"{key.upper()}  :  {myCar[key]}")

yourCar["plate"] = "12345"