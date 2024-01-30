import math

name = input("Enter name: ")
animal = input("Enter animal: ")
age = int(input("Enter age: "))
color = input("Enter color: ")

valid_animals = ["dog", "cat", "chicken", "pig"]

try:

    if animal not in valid_animals:
        raise TypeError("Invalid animal type")
    elif color.lower() == "black":
        raise TypeError("Pet not allowed, malas yan")

    service_charge = age / (
        math.sqrt(20 - age) * math.sqrt(30 - age) * math.sqrt(15 - age)
    )
    print(f"Service charge for {name}: {service_charge}")
except TypeError as t:
    print(t)
except ValueError:
    print("Invalid age, cannot compute service charge")
