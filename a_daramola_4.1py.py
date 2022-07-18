#Akinola Daramola Jr
#Programming Exercise 4.1
#Due Date: 06/26/2022



"""
A bug collector collects bugs every day for five days.
Write a program that keeps a running total of the number of bugs collected during the five days.
The loop should ask for the number of bugs collected for each day,
and when the loop is finished, the program should display the total number of bugs collected.

"""


#Declaring value of days variable
days = 0

#Declaring value of bugs variable
bugs = 0

#Assigning value of total bugs collected to bugs 
total_bugs_collected = bugs

final_day = 5

while days < final_day: #Iterating through days
    days += 1 #increase value of day by 1 each iteration
    print(f"Day: {days}") #Displays number of days
    bugs_collected = int(input("How many bugs were collected today? ")) #Asks number of bugs collected each day
    total_bugs_collected = total_bugs_collected + bugs_collected #Calculates number of bugs collected in total
    if days == final_day: #Conditional statement - determins if days equals final day
        print(f"Total bugs collected: {total_bugs_collected}") #Displays total number of bugs collected after 5 days
