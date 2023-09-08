marks = int(input("what is your marks? "))
print(
    "Grade A"
    if 90 <= marks <= 100
    else "Grade B"
    if 80 <= marks <= 89
    else "Grade C"
    if 70 <= marks <= 79
    else "Fail"
    if 0 <= marks <= 69
    else "invalid input"
)
