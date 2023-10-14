##########################
# QUESTION 1 (10 points) # 
##########################
# The code below is a guessing game. Unfortunately, you cannot play because there are multiple errors.
# Identify at least 5 issues with the code below to explain (in your own words) why the code will not run.
# You do not need to rewrite the code just yet (that is question #2).

import random
u_num = input("Guess a number between 1 to 10: ")
w_num = random.uniform(1, 10)//1

for i in range(3):
if u_num = w_num:
    print(f"Congrats you win and you guessed this number in {i+1} tries!")
    break
elif u_num < w_num:
    if i == 2:
        print("That is too low, sorry you are out of turns")
    else: 
        print("That is too low")
else:
    if i == 2:
        print("That is too high, sorry you are out of turns")
    else
        print("That is too high")
u_unm = int(input("Guess again: "))

########################################
# TYPE YOUR ANSWER TO QUESTION 1 HERE # 
#######################################
1. The code within the for loop lacks consistent indentation.
2. In the line 13 assignment operator (=) is used instead of comparison operator (==).
3. In line 16, Invalid comparison becuase u_num is string and it is comapred with float number. So we need to convert the string to int/float using int() or float()
4. In line 24 colon(:) is missing for else
5. In line 26 undefined variable is used "u_unm" instead of "u_num".
6. Even after completing 3 attempts, "Guess again:" is printed on the terminal. So Inorder to avoid that we need to add break after the lines 18 and 23.



##########################
# QUESTION 2 (10 points) # 
##########################
# Now you will address the errors you identified above in Python. 
# Fix the guessing game code above so it will run as expected.

########################################
# TYPE YOUR ANSWER TO QUESTION 2 HERE # 
#######################################

import random

u_num = int(input("Guess a number between 1 to 10: "))
w_num = (random.uniform(1, 10) // 1)

for i in range(3):
    if u_num == w_num:
        print(f"Congrats you win and you guessed this number in {i+1} tries!")
        break
    elif u_num < w_num:
        if i == 2:
            print("That is too low, sorry you are out of turns")
            break
        else:
            print("That is too low")
    else:
        if i == 2:
            print("That is too high, sorry you are out of turns")
            break
        else:
            print("That is too high")

    u_num = int(input("Guess again: "))





##########################
# QUESTION 3 (20 points) # 
##########################
# Mad libs are a simple game where you create a story template with blanks for words. 
# A list of user selected words are placed into the story, creating an often silly or funny result. 
# Create a simple madlib program that prompts for a noun, a verb, an adverb, and an adjective.
# Then use those inputs in a short story or sentence that you create.

'''
Here is an example. Note that your story should be something you create.

Example Output:
Please enter a noun: dog
Now, enter a verb: walk
Give me an adjective: blue
Finally, can I get an adverb: quickly
Do you walk your blue dog quickly? That's hilarious!
'''

########################################
# TYPE YOUR ANSWER TO QUESTION 3 HERE # 
#######################################
import random

Expression = ["hilarious", "cool", "awesome", "mind blowing"]
noun = input("Please enter a noun: ")
verb = input("Now, enter a verb: ")
adjective = input("Give me an adjective: ")
adverb = input("Finally, can I get an adverb: ")
random_exp_index = random.randint(0, len(Expression) - 1)
print(
    f"Do you {verb} your {adjective} {noun} {adverb}? That's {Expression[random_exp_index]}!"
)



##########################
# QUESTION 4 (20 points) # 
##########################
# Imagine that we have a list of several hundred grades.
# We want to find the lowest grade in the list
# Write a function that returns the smallest element in a given list.

########################################
# TYPE YOUR ANSWER TO QUESTION 4 HERE # 
#######################################

#defining the small function
def small(list1):
    return min(list1)

#creating an empty list
grades = []
courses = int(input("Enter the number of courses that you have enrolled "))

for i in range(courses):
    grades_obtained = int(input(f"Enter the Marks obtained in {i+1} course "))
    grades.append(grades_obtained)

print("The grades obtained is ", grades)
lowest_grade = small(grades) #function call
print("the lowest grade obtained is ", lowest_grade) #printing the lowest grade



##########################
# QUESTION 5 (20 points) # 
##########################
# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, 
# and a boolean indicating if we are on vacation, return a string 
# of the form "7:00" indicating when the alarm clock should ring. 
# On weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". 
# Unless we are on vacation, then on weekdays it should be "10:00" and on weekends it should be "off".

'''
For example:
alarm_clock(1, False) → '7:00'
alarm_clock(5, True) → '10:00'
alarm_clock(0, False) → '10:00'
alarm_clock(0, True) → 'off'
'''
########################################
# TYPE YOUR ANSWER TO QUESTION 5 HERE # 
#######################################

#creating the dictionary
day_of_the_week = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
}

#defining the alarm_clock function
def alarm_clock(day, onVacation):
    if onVacation:
        if day_of_the_week[day] == "Saturday" or day_of_the_week[day] == "Sunday":
            return "off"
        else:
            return "10:00"
    else:
        if day_of_the_week[day] == "Saturday" or day_of_the_week[day] == "Sunday":
            return "10:00"
        else:
            return "7:00"


monday_no_vacation = alarm_clock(1, False)
print("alarm clock (1,False) -> ", monday_no_vacation)
friday_on_vacation = alarm_clock(5, True)
print("alarm clock (5,True)  -> ", friday_on_vacation)
sunday_no_vacation = alarm_clock(0, False)
print("alarm clock (0,False) -> ", sunday_no_vacation)
sunday_on_vacation = alarm_clock(0, True)
print("alarm clock (0,True)  -> ", sunday_on_vacation)
saturday_on_vacation = alarm_clock(6, True)
print("alarm clock (6,True)  -> ", saturday_on_vacation)
saturday_on_vacation = alarm_clock(6, False)
print("alarm clock (6,False) -> ", saturday_on_vacation)
thursday_no_vacation = alarm_clock(4, False)
print("alarm clock (4,False) -> ", thursday_no_vacation)



##########################
# QUESTION 6 (20 points) # 
##########################
# Given the dictionary below, count the frequency of each Hogwarts house present in the dictionary.
harry_potter_dict = {
    "Harry Potter": "Gryffindor",
    "Ron Weasley": "Gryffindor",
    "Hermione Granger": "Gryffindor",
    "Albus Dumbledore": "Gryffindor",
    "Luna Lovegood": "Ravenclaw",
    "Draco Malfoy": "Slytherin",
    "Cedric Diggory": "Hufflepuff",
    "Nymphadora Tonks": "Hufflepuff",
    "Susan Bones": "Hufflepuff",
    "Helena Ravenclaw": "Ravenclaw",
    "Cho Chang": "Ravenclaw",
    "Severus Snape": "Slytherin",
    "Horace Slughorn": "Slytherin",
    "Voldemort": "Slytherin"
}

########################################
# TYPE YOUR ANSWER TO QUESTION 6 HERE # 
#######################################


harry_potter_dict = {
    "Harry Potter": "Gryffindor",
    "Ron Weasley": "Gryffindor",
    "Hermione Granger": "Gryffindor",
    "Albus Dumbledore": "Gryffindor",
    "Luna Lovegood": "Ravenclaw",
    "Draco Malfoy": "Slytherin",
    "Cedric Diggory": "Hufflepuff",
    "Nymphadora Tonks": "Hufflepuff",
    "Susan Bones": "Hufflepuff",
    "Helena Ravenclaw": "Ravenclaw",
    "Cho Chang": "Ravenclaw",
    "Severus Snape": "Slytherin",
    "Horace Slughorn": "Slytherin",
    "Voldemort": "Slytherin",
}

# Create an empty dictionary to store the frequency of each house
house_frequency = {}


for name, house in harry_potter_dict.items():
    if house in house_frequency:
        house_frequency[house] += 1
    else:
        house_frequency[house] = 1

# Print the frequency of each house
for house, frequency in house_frequency.items():
    print(f"{house}: {frequency}")
