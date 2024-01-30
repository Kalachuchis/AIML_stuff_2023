import re

pattern = r"\b(\+63 ?9(\d{9})|0?9(\d{9}))\b"


string = input("Enter input: ")

match = re.search(pattern, string)

if match:
    number = match.group(0)
    output = re.sub(".", "*", number)
    print(f"My phone number is {output}")
else:
    print("No valid mobile number")
