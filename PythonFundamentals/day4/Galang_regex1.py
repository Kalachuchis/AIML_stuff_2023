import re

pattern = "^(([a-z|A-Z]{2,15})\.([a-z|A-Z]{2,15})@pointwest.com.ph)$"


string = input("Enter email address: ")

match = re.search(pattern, string)

if match:
    email = match.group(0)
    print(match.group())
    name = email.replace("@pointwest.com.ph", "").split(".")
    print("First Name: " + name[0].capitalize())
    print("Last Name: " + name[1].capitalize())
else:
    print(f"{string} is an INVALID Pointwest email")
