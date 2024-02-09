
# Define functions for basic arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function to get a valid numeric input from the user
def get_number_input(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Please enter a valid number.")

# Function to get a valid operator input from the user
def get_operator_input(prompt):
    valid_operators = {'+', '-', '*', '/'}
    while True:
        operator = input(prompt)
        if operator in valid_operators:
            return operator
        else:
            print("Please enter a valid operator (+, -, *, /):")

while True:
    # Get inputs from the user
    x = get_number_input("Enter first number: ")
    y = get_number_input("Enter second number: ")

    # Get the operator from the user
    operator = get_operator_input("Enter operation (+, -, *, /): ")

    # Perform the appropriate operation based on the operator
    if operator == "+":
        result = add(x, y)
    elif operator == "-":
        result = subtract(x, y)
    elif operator == "*":
        result = multiply(x, y)
    elif operator == "/":
        result = divide(x, y)
    else:
        result = "Invalid operation"

    # Display the result to the user
    if isinstance(result, float) and result.is_integer():
        print("Result:", int(result))
    else:
        print("Result:", result)

    # Ask the user if they want to perform another calculation
    another_calculation = input("Do you want to perform another calculation? (yes/no): ")

    if another_calculation.lower() != 'yes':
        break
