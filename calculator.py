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
    num2 = tokens[2]

    #calling operator functions
    if operator == "+":
        result = add(float(num1), float(num2))

    elif operator == "-":
        result = subtract(float(num1), float(num2))

    elif operator == "*":
        result = multiply(float(num1), float(num2))

    elif operator == "/":
        result = divide(float(num1), float(num2))

    elif operator == "square":
        result = square(float(num1))
    
    elif operator == "cube":
        result = cube(float(num1))
    
    elif operator == "pow":
        result = power(float(num1), float(num2))

    elif operator == "mod":
        result = mod(float(num1), float(num2))    

    print(result)    