#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error! Division by zero is not allowed."

def power(x, y):
    return math.pow(x, y)

def sqrt(x):
    try:
        return math.sqrt(x)
    except ValueError:
        return "Error! Square root of negative number is not allowed."

def calculator():
    while True:
        print("Enter 'exit' to end the program")
        num1 = input("Enter first number: ")
        if num1.lower() == 'exit':
            break

        print("Select operation:")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Power")
        print("6.Square root (only first number)")

        choice = input("Enter choice(1/2/3/4/5/6): ")
        if choice.lower() == 'exit':
            break

        try:
            num1 = float(num1)
            if choice in ['1', '2', '3', '4', '5']:
                num2 = input("Enter second number: ")
                if num2.lower() == 'exit':
                    break
                num2 = float(num2)

            if choice == '1':
                result = add(num1, num2)

            elif choice == '2':
                result = subtract(num1, num2)

            elif choice == '3':
                result = multiply(num1, num2)

            elif choice == '4':
                result = divide(num1, num2)

            elif choice == '5':
                result = power(num1, num2)

            elif choice == '6':
                result = sqrt(num1)

            else:
                print("Invalid operation choice")
                continue

            print("The result is: ", result)

        except ValueError:
            print("Invalid number input")

calculator()


# In[ ]:




