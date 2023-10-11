# Liam Toebbe
# 10/11/2023
# returning information exercise
#

num1 = input("write a number:")
num2 = input("write another number:")


def add_two_numbers(num1, num2):
    """
    adds two numbers
    :param num1: a number entered by the user
    :param num2: another number entered by the user
    :return: sum of the two numbers
    """

    sum_of_numbers = int(num1)+int(num2)
    return sum_of_numbers


print(add_two_numbers(num1, num2))
