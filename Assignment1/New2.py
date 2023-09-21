Guest_name = input("Guest name: ")
Staying = float(input("Number of nights staying: "))
print(
    """ 
Membership Types:
(1) Non-Member - NM
(2) Basic - B
(3) Advanced - A
(4) Premium - P 
(5) VIP -V
    """
)
Type = input("Please enter membership type: ")

print("\n")
print(f"Name: {Guest_name}")
print(f"Number of Nights: {Staying}")
print(f"Membership Type: {Type}")

if Type == "NM" or Type == "nm" or Type == "Nm" or Type == "nM":
    Price = 79.99 * Staying
    print(f"Price: ${Price}")
    print("Discounts are not available for Non-member type")
elif Type == "B" or Type == "b":
    Price = 79.99 * Staying
    print(f"Price: ${Price}")
    Discount = Price * 0.1
    Discounted_Price = Price - Discount
    print(f"Discounted Price : {Discounted_Price}")
elif Type == "A" or Type == "a":
    Price = 79.99 * Staying
    print(f"Price: ${Price}")
    Discount = Price * 0.15
    Discounted_Price = Price - Discount
    print(f"Discounted Price : {Discounted_Price}")
elif Type == "P" or Type == "p":
    Price = 79.99 * Staying
    print(f"Price: ${Price}")
    Discount = Price * 0.25
    Discounted_Price = Price - Discount
    print(f"Discounted Price : {Discounted_Price}")
elif Type == "V" or Type == "v":
    Price = 79.99 * Staying
    print(f"Price: ${Price}")
    Discount = Price * 0.40
    Discounted_Price = Price - Discount
    print("Discounted Price :", (Discounted_Price))
else:
    print(" Please enter the valid Membership Type")
