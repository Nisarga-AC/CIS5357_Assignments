"""
numbers = [1, 2, 3]
squares = []
for number in numbers:
    n = number * number
    squares.append(n)
print(squares)
print(numbers)
New_Dict = dict(zip(squares, numbers))
print(New_Dict)
"""

original_dict = {1: 1, 2: 4, 3: 9}
swapped_dict = {}

for k in original_dict.keys():
    swapped_dict[original_dict[k]] = k
print(swapped_dict)
