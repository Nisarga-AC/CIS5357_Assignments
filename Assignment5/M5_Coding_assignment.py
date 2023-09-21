"""
My Name is Nisarga Arsikere Chidananda
My Student Id is A05289369

"""


# defining the function string_stats
def string_stats(user_input_string):
    # defining the counter variables
    upper = 0
    lower = 0

    """
    converting the string into list by calling split function and 
    finding the length of list by calling len function and 
    assigned it to the variable called words 
    """
    words = len(user_input_string.split())

    # iterate through the user_input_string
    for c in user_input_string:
        if c.isupper():  # checks if the letter is upper
            upper += 1
        elif c.islower():  # checks if the letter is lower
            lower += 1
        else:
            pass

    # Printing the length of input string, number of upper & lower case letters and number of words in the string
    print("The length of the String is", len(user_input_string))
    print("The number of upper case letters are", upper)
    print("The number of lower case letters are", lower)
    print("The numbers of words in the string are", words)


user_input_string = input("enter the string  ")
# calling the string_stats function
string_stats(user_input_string)
