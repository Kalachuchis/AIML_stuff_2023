# Program that asks the age and determines whether infant, teenager or adult


user_input = ""
# Asks user for the age
while not user_input.isnumeric(): # repeats asking for input until user inputs numberic value
    user_input = input("Please enter your age: ")


age = int(user_input)


if 0 <= age and age <= 2:
    print("You are an infant")
elif 2 < age and age < 13:
    print("You are a child")
elif 12 < age and age < 18:
    print("You are a teenager")
elif 18 < age:
    print("You are an adult")
else:
    print("what are you?")
