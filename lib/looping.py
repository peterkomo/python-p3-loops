#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    countdown=10
    while countdown >=1:
         print (countdown)
         countdown -= 1
    print("Happy New Year!")



def square_integers(numbers):
    squared_list = [num ** 2 for num in numbers]
    return squared_list

input_list = [1, 2, 3, 4, 5]
result = square_integers(input_list)
print(result)

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

def reverse_string(input_str):
    reversed_str = ""
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str

print(reverse_string("hello"))  
print(reverse_string("world")) 


def square_integers(int_list):
    squared_list = [num ** 2 for num in int_list]
    return squared_list

print(square_integers([1, 2, 3, 4, 5]))  
print(square_integers([0, -1, 2, -3]))   
