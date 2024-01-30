string = input("Please input a string: ").strip()

print("".join([i for i in string if (i.isspace() or i.isalpha() or i.isnumeric())]).lower())
