""""
M4_assignment = [12, 21, 33, 14, 57, 6, 17, 10, 11, 28, 3, 32, 2, 4]

for i in M4_assignment:
    if i % 2 == 0:
        print("even no", i)
    else:
        print("odd no", i)
"""

"""
for number in range(1, 31):
    print(
        "FizzBuzz"
        if (number % 3 == 0) and (number % 5 == 0)
        else "Fizz"
        if number % 3 == 0
        else "Buzz"
        if number % 5 == 0
        else number
    )
"""

"""
import random

New_list = "MSFT, TSLA, GOOG, AAPL".split(",")
print("String converted to List is \n", New_list)
random.shuffle(New_list)
print("Random List is \n", New_list)
New_List = " and ".join(New_list)
print("Lists converted to string is", New_List)
print(New_List.lower())
"""

for number in range(4, 16):
    print(number * number)

Square = []

for number in range(4, 16):
    Square.append(number * number)
print(Square)
