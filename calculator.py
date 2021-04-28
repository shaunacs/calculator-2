"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
# while True loop:
while True:
    user_input = input("Enter your equation here: ")
    #user input statement "put equation here:"
    #user inputs operator and number
    tokens = user_input.split(" ")

    #if quit statement
    if "quit" in tokens:
        print("Exiting calculator.")
        break

    #not enough inputs statement
    if len(tokens) < 2:
        print("Need more inputs.")
        break   
    
    # name operator variable
    operator = tokens[0]

    # name number variable
    num1 = tokens[1]