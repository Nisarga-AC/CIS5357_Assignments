"""
My Name is Nisarga Arsikere Chidananda
My Student Id is A05289369
"""
M4_assignment = [12, 21, 33, 14, 57, 6, 17, 10, 11, 28, 3, 32, 2, 4]
odd_list = []
even_list = []
for number in M4_assignment:
    if number % 2 == 0:
        even_list.append(number)

    else:
        odd_list.append(number)
print("odd no's are", odd_list)
print("even no's are", even_list)
