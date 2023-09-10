""""
win_no = 6
no_of_attempts = 3
i = 1

while i <= no_of_attempts:
    user_input = int(input("Enter the number from 1 to 9 "))
    if user_input == win_no:
        print("you win... Congrats")
        break
    elif i == no_of_attempts:
        print(" you lost 3 chances...")
    else:
        print("Try again")
        i += 1
"""


marks = []
i = 1
subjects = input("Enter the number of subjects that you enrolled this year? ")
if not subjects.isdigit():
    while True:
        subjects = input("Please enter the valid subjects that you have enrolled? ")
        if not subjects.isdigit():
            continue
        else:
            break


while i <= int(subjects):
    score = int(input(f"enter the marks of subject {i} "))
    if 0 < score <= 100:
        marks.append(score)
        i += 1

    else:
        print("enter the valid score")
        continue
Total = sum(marks)
print(f"Total is {Total}")
Average = Total / int(subjects)
print(f"Average is {Average}")
print(
    "Grade A"
    if 90 <= Average <= 100
    else "Grade B"
    if 80 <= Average <= 89
    else "Garde C"
    if 70 <= Average <= 79
    else "fail"
)
