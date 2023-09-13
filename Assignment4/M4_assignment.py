"""
My Name is Nisarga Arsikere Chidananda
My Student Id is A05289369
"""

# Approach 1
M4_assignment = [12, 21, 33, 14, 57, 6, 17, 10, 11, 28, 3, 32, 2, 4]
odd_list = []  # initializing the empty odd list
even_list = []  # initializing the empty even list

# iterating the M4_assignment list by using for loop
for number in M4_assignment:
    even_list.append(number) if number % 2 == 0 else odd_list.append(number)
"""
 if the condition is True then the number will append/add to the even_list, 
 if the condition is False the number will append/add to the odd_list

"""
print("Approach 1 Output:")
print(f"odd numbers are {odd_list}")  # printing the odd_list
print(f"even numbers are {even_list}\n")  # printing the even_list


# Approach 2
M4_assignment = [12, 21, 33, 14, 57, 6, 17, 10, 11, 28, 3, 32, 2, 4]
odd_list = []  # initializing the empty odd list
even_list = []  # initializing the empty even list

for number in M4_assignment:
    even_list.append(number) if number % 2 == 0 else odd_list.append(number)

odd_list.sort()  # Sorting the odd_list in ascending order by calling the sort function
even_list.sort()  # Sorting the even_list in ascending order by calling the sort function

print("Approach 2 Output:")
print("odd numbers are", odd_list)  # printing the odd_list
print("even numbers are", even_list)  # printing the even_list
