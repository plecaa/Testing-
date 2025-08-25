import math


def generate_full_name():
    first_name = 'Arnold'
    last_name = 'Muleya'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name()) 


def subtract_numbers():
    num_one = 10
    num_two = 5
    subtraction = num_one - num_two
    return subtraction
print(subtract_numbers()) 


def greetings (name):
    text =' welcome to me world of python ' + name
    return text
print (greetings('Muleya'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def area_of_sircle (r):
    PI = math.pi
    area = PI * r ** 2
    return area
print(area_of_sircle(10))


