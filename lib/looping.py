#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count >= 1:
        print(count)
        count -= 1
        print("Happy New Year!")
    

def square_integers(int_list):
    return[x**2 for x in int_list]

def fizzbuzz():
    for num in range(1,101):
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz") 
        else:
            print(num)         

