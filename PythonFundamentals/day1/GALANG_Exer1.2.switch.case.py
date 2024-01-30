# tuple of operations for user to choose from
operations = ("+", "-", "/", "*")


print("Welcome to a simple calculator")

# Collects 2 numbers from the user
first_number = int(input("Please enter the first number: "))
second_number = int(input("Please enter the second number: "))

# instantiate operator variable for while loop to ask for correct user input
operator = ""

while operator not in operations:
    operator = input(f"Please choose from the following {operations}: ")

match operator:
    case "+":
        print(
            f"{first_number} {operator} {second_number} = {first_number+second_number}"
        )
    case "-":
        print(
            f"{first_number} {operator} {second_number} = {first_number-second_number}"
        )
    case "/":
        print(
            f"{first_number} {operator} {second_number} = {first_number/second_number}"
        )
    case "*":
        print(
            f"{first_number} {operator} {second_number} = {first_number*second_number}"
        )
    case _:
        print("What")
