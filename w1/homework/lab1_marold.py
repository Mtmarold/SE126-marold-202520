#Lab 1
#Matthew Marold
#1/10/24
#SE126

#Program Prompt - it is a program that determines whether a meeting room is in violation of fire regulations regarding the maximum room capacity. The program will accept the maximum room capacity and the number of people attending the meeting. If the number of people is less than or equal to the maximum room capacity, the program announces that it is legal to hold the meeting and tells how many additional people may legally attend. If the number of people exceeds the maximum room capacity, the program announces that the meeting cannot be held as planned due to the fire regulation and tells how many people must be excluded in order to meet the fire regulations. The user should be allowed to enter and check as many rooms as they would like without exiting the program

#variable dictionary - 
#max_cap - maximum capacity of room
#people - number of people attending meeting
# remaining_cap - difference of max_cap and people
#remove_ppl - if the attendance exceeds capacity, remove x amount of people

#first function for number of people attending meeting and maximum capacity of room.
def difference(people, max_cap):
    '''This function will ask the user to input the number of people attending the meeting and the maximum capacity of the room and tell them if they are following fire laws or not and tell them how many people need to be excluded or how many more people can enter'''
 
    diff = max_cap - people
    return diff




#fucntion to ask user if they want to input another rooms attendance
def decision(ans):
    '''This function asks the user if they want to enter another room's attendance information.'''
    #ans = input("Would you like to enter another room's attendance information? [y/n] ").lower()

    while ans != "y" and ans != "n":
        print("****Invalid Entry please try again!****")
        ans = input("Would you like to enter another room's attendance information? [y/n] ").lower()
    else:
        
        return ans


#main program code ----------------
response = "y"
while response == "y":
    meeting_name = input("Enter the name of this meeting: ")
    max_cap = int(input("Enter the maximum room capacity: "))
    people = int(input("Enter the amount of people attending this meeting: "))
    
    if people <= max_cap:
        diff = max_cap - people
        print(f"Its legal to hold this meeting, The remaining people that can enter this room is {diff}")
    else:
        diff = people - max_cap
        print(f"please exclude {diff} more people to legally hold this meeting")
    #call the difference function
    difference(people, max_cap)
    
    #ask if they want to enter another roooms info using the decision function
    ans = input("Would you like to enter another room's attendance information? [y/n] ").lower()
    response = decision(ans)
print("Thank you for using my program, goodbye :]")





        

    