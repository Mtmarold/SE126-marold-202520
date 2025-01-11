#Lab 1
#Matthew Marold
#1/10/24
#SE126

#Program Prompt - it is a program that determines whether a meeting room is in violation of fire regulations regarding the maximum room capacity. The program will accept the maximum room capacity and the number of people attending the meeting. If the number of people is less than or equal to the maximum room capacity, the program announces that it is legal to hold the meeting and tells how many additional people may legally attend. If the number of people exceeds the maximum room capacity, the program announces that the meeting cannot be held as planned due to the fire regulation and tells how many people must be excluded in order to meet the fire regulations. The user should be allowed to enter and check as many rooms as they would like without exiting the program

#variable dictionary - 


def difference(people, max_cap):
    if people <= max_cap:
        remaining_cap = max_cap - people
        print(f"Its legal to hold this meeting, The remaining people that can enter this room is {remaining_cap}")
        return remaining_cap
    else:
        remove_ppl = people - max_cap
        print(f"please exclude {remove_ppl} more people to legally hold this meeting")
        return remove_ppl

def decision(response):
    response = "y"
    while response == "y":
        max_cap = int(input("Enter the maximum room capacity: "))
        people = int(input("Enter the number of people attending this meeting"))

        difference(people, max_cap)
        return response
    else:
        print("Thank you for using my program! goodbye :]")




    #main program code ----------------


meeting_name = input("Enter the name of this meeting: ")
max_cap = int(input("Enter the maximum room capacity: "))
people = int(input("Enter the amount of people attending this meeting: "))

difference(people, max_cap)


response = input("Would you like to enter another meeting's attendance information?:[y/n] ")
decision(response)




        

    