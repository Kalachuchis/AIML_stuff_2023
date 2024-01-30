ipAddress = input("Enter IP Address: ").strip()

dotCounter = 0

for i in ipAddress:
    if i == ".":
        dotCounter += 1

list_of_address = [i for i in ipAddress.split(".")]

try:
    if ipAddress == "0.0.0.0":
        raise Exception("Device is offline")
    if len.list_of_address != 4:
        raise Exception("Missing address")
    if list_of_address[0] == 0 and any([i != 0 for i in list_of_address[1:]]):
        raise Exception("Invalid address") 
    if dotCounter != 3:
        raise ValueError("number of dots should be exactly 3")
    for index, i in enumerate(list_of_address):
        if 0 > int(i) or int(i) > 256:
            raise TypeError("a value in you address is not within 0-255")
    print("IP Address is valid")
except Exception as e:
    print(e)
