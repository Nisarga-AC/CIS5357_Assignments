"""

squares = []
numbers = [1, 2, 3]

for number in numbers:
    n = number * number
    squares.append(n)
print(squares)
print(numbers)
new_dict = dict(zip(numbers, squares))
print(new_dict)
print(new_dict.keys())
print(new_dict.values())
avg = sum(new_dict.values()) / len(new_dict)
print(avg)
maximum = max(new_dict.values())
print(maximum)

"""

subjects = ["Analytics", "DBMS", "Python"]
scores = []
analytics_marks = int(input("Enter the marks obtained in Analytics subject "))
scores.append(analytics_marks)
DBMS_marks = int(input("Enter the marks obtained in DBMS subject "))
scores.append(DBMS_marks)
Python_marks = int(input("Enter the marks obtained in Python subject "))
scores.append(Python_marks)
print(scores)
Subjects_Scores = dict(zip(subjects, scores))
print(Subjects_Scores)
Average = sum(Subjects_Scores.values()) / len(Subjects_Scores)
print("Average Marks is ", Average)
Highest_score = max(Subjects_Scores.values())
Lowest_score = min(Subjects_Scores.values())
print("The highest score among 3 subjects is ", Highest_score)
print("The highest score among 3 subjects is ", Lowest_score)
