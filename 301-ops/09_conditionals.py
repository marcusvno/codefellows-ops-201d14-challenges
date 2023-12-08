""" 
    Author:                       Marcus Nogueira
    Date of latest revision:      12/07/2023
    Purpose:                      Learn about Python Conditional Statements
"""

import time

def con_test(a, b):
    if a == b:
        print("a is equal to b")

    if a != b:
        print("a does not equal b")

    if a < b:
        print("a is less than b")

    if a <= b:
        print("a is less than or equal to b")

    if a > b:
        print("a is great than b")

    if a >= b:
        print("a is great than or equal to b")

    if type(b) == bool:
        print("b is a boolean.")
    elif type(b) == str:
        print("b is an string")
    elif type(b) == int:
        print("b is an integer.")
    else:
        print("b is not a string, an integer, or boolean")
        
        
    if a > 0 and type(a) == str:
        print("a is a str and greater than zero.")
    if a > 0 and type(a) == int:
        print("a is an integer that is great than zero.")
    if a > 0:
        if a < 10:
            print("b is between 0 and 10")
    if b > 0:
        if b < 10:
            print("b is between 0 and 10")
    


def tests():
    print("\n\nTEST 01\n--------------------------------\na = 1     b = 2\n--------------------------------")
    con_test(1, 2)
    print("--------------------------------\n")
    time.sleep(1.5)
    
    print("\nTEST 02\n--------------------------------\na = 3     b = 3\n--------------------------------")
    con_test(3, 3)
    print("--------------------------------\n")
    time.sleep(1.5)
    
    print("\nTEST 03\n--------------------------------\na = 5     b = 4\n--------------------------------")
    con_test(5, 4)
    print("--------------------------------\n")
    time.sleep(1.5)

def input_test():
    print("\nUSER INPUT TEST\n--------------------------------")
    x = int(input("Enter a number for variable a: "))
    y = int(input("Enter a number for variable b: "))
    print("--------------------------------")
    con_test(x, y)
    print("--------------------------------\n")

if __name__ == "__main__":
    tests()
    input_test()
