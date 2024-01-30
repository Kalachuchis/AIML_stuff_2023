string = input("Please input your name: ").strip()

print("".join([i[0].upper() for i in string.split(" ")]))
