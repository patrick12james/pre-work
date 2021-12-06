'''question 1'''
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.


def hello_name(user_name):
    print(user_name)


hello_name("hello_USERNAME!")

'''question 2'''
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing


def first_odds():
    range(1, 100, 2)
    for odd in range():
        print()


'''question 3'''
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.


def max_num_in_list(a_list):
    numbers = [55, 4, 92, 1, 104, 64, 73, 99, 20]
    max_value = None
    for num in numbers:
        if (max_value is None or num > max_value):
            max_value = num


print(max_num_in_list(1))


'''question 4'''
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type(true/false).


def is_leap_year(a_year):
    '''question 5'''
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2, 3, 4, 5, 6, 7] are consecutive numbers, but[1, 2, 4, 5] are not consecutive numbers. The return should be boolean Type.


def is_consecutive(a_list):
    a_list = [1, 2, 3, 4, 5, 6]
    for the_list in a_list:
        if a_list == [1, 2, 3, 4, 5, 6]:
            print(True)
        else:
            print(False)


# print(is_consecutive())
