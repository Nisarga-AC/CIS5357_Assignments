"""
temp = int(input("what is the temperature of water? "))
print("It is boiling" if temp >= 100 else "It is Freezing" if temp <= 0 else "neither")
"""

"""
list = [1, 0, 2, 0, 4, 6]
zero_list = []

for number in list:
    if number == 0:
        list.remove(number)
        list.append(number)
        continue

print(list)

"""

"""
old_price = {"milk": 1.02, "coffee": 2.5, "bread": 2.5}

new_price = {}

for key in old_price:
    if old_price[key] > 2:
        new_price[key] = old_price[key] * 1.5
    else:
        new_price[key] = old_price[key]

print(new_price)

"""

"""
def get_city(address):
    return address.split(",")[2][0:2]


address = "3022 Broadway,New York,NY 10027,USA"
city = get_city(address)
print(city)

"""

"""
def upper_reverse(list1):
    return ",".join(reversed(list1))


list1 = ["apple", "banana"]
print(upper_reverse(list1))

"""


"""
document = {
    "name": "nisarga",
    "age": 26,
    "occupation": {"digital": "analyst", "software": "data_engineer"},
}

print(document["occupation"]["digital"])

"""

"""
square = {1: 1, 2: 4, 3: 9}

reversed_square = {value: key for key, value in square.items()}
print(reversed_square)



numbers = [1, 2, 3]

new_dict = {num: num**2 for num in numbers}
print(new_dict)

"""

number = int(input("Enter the number for which you need table "))

for count in range(1, 11):
    product = number * count
    print(f"{number} * {count} =", product)
