"""
My Name is Nisarga Arsikere Chidananda
My Student Id is A05289369

"""


# defining the get_key_by_value function in order to get the key for the respective value
def get_key_by_value(dictionary, target_value):
    for key, value in dictionary.items():
        if value == target_value:
            return key


# Creating the empty dictionary Student_record
Student_record = {}
number_of_course = int(
    input("Enter the number of courses that you are enrolled this semester ")
)
for i in range(number_of_course):
    # taking the course_names as an input from the user
    course_names = input(f"Enter the course {i+1} name ")

    # taking the Marks_obtained as an input from the user
    Marks_obtained = int(input(f"Enter the Marks obtained in course {course_names}  "))

    # adding course_names as keys and Marks_obtained as values to the Student_record dictionary
    Student_record[course_names] = Marks_obtained

print("\n")
# Printing the dictionary Student_record with course names as keys and Marks_obtained as values
print(
    f"Student_record dictionary with course names and Marks_obtained - {Student_record} \n"
)

# calculating the Average of marks obtained in all courses
Average_of_Marks = sum(Student_record.values()) / number_of_course
print(f"Average of {number_of_course} Courses is {Average_of_Marks} \n")

# finding the Highest marks obtained among the courses using .values() method and max function
Highest_Marks = max(Student_record.values())

# finding the name of the course in which the highest marks is obtained by calling the function get_key_by_value
Highest_Marks_obtained_course = get_key_by_value(Student_record, Highest_Marks)

print(
    f"The Highest Marks obtained among {number_of_course} courses is {Highest_Marks_obtained_course} = {Highest_Marks} \n"
)

# finding the Lowest marks obtained among the courses using .values() method and min function
Lowest_Marks = min(Student_record.values())

# finding the name of the course in which the lowest marks is obtained by calling the function get_key_by_value
Lowest_marks_obtained_course = get_key_by_value(Student_record, Lowest_Marks)
print(
    f"The Lowest Marks obtained among {number_of_course} courses is {Lowest_marks_obtained_course} = {Lowest_Marks}"
)
