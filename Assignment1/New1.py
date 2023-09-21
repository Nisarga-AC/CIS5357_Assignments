print("welcome to your new premium account")
name = input("Please enter your name: ")
pin = input("Please enter the PIN number: ")
current_year = int(input("please enter the current year:  "))
original_savings = float(input("Please enter a savings amount: "))
print("\n")
print(
    "------------------------------------------------------------------------------------------------------------------------"
)
print(f"Year:{current_year}")
print(f"Original Savings: ${original_savings}")
Earned_interest = original_savings * 0.04
print(f"Earned Interest: ${Earned_interest} (interest rate 4.0%)")
current_savings = Earned_interest + original_savings
print(f"current Savings :${current_savings}")
print(
    "-------------------------------------------------------------------------------------------------------------------------\n"
)
print(
    "-------------------------------------------------------------------------------------------------------------------------"
)
for i in range(2):
    if i < 2:
        current_year += 1
        print(f"Year:{current_year}")
        previous_savings = current_savings
        print(f"Previous savings: {previous_savings}")
        Earned_interest = previous_savings * 0.04
        print(f"Earned Interest: ${Earned_interest} (interest rate 4.0%)")
        current_savings = Earned_interest + previous_savings
        print(f"current Savings :${current_savings}")
        i += 1
        print(
            "----------------------------------------------------------------------------------------------------------------\n"
        )
        print(
            "----------------------------------------------------------------------------------------------------------------"
        )
