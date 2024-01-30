import re

string = input("Enter a string: ").strip()
# pattern_deep = r"^((((\d|\d\d|1\d\d|2[1-4]\d|25[0-5])|(\d|\d\d|1\d\d|2[1-4]\d|25[0-5])\/(\d|\d\d|1\d\d|2[1-4]\d|25[0-5]))\.?){3}((\d|\d\d|1\d\d|2[1-4]\d|25[0-5])|(\d|\d\d|1\d\d|2[1-4]\d|25[0-5])\/(\d|\d\d|1\d\d|2[1-4]\d|25[0-5])))$"

# regex pattern sample 192.138.2.2/32
pattern_deep = r"^(((\d|\d\d|1\d\d|2[1-4]\d|25[0-5])\.?){3}(\d|\d\d|1\d\d|2[1-4]\d|25[0-5])(\/(\d|[1-2]\d|3[0-2]))?)$"
pattern_shallow = r"^((\d+)\.){3}(\d+)(\/\d+)?$"


def nearest_value(shallow_match):
    address = shallow_match.split("/")

    nearest_address = re.sub(r"\d+", helper, address[0])

    # returns 32 if cidr is greater than 32 no use case for less than 0 since it is not possible to get from regex
    cidr = 32 if int(address[1]) > 32 else str(int(address[1]))

    print(f"Nearest valid value = {nearest_address}/{cidr}")


def helper(match):

    # ip address can only go to 255
    if int(match.group()) > 255:
        return str(255)
    else:
        return str(int(match.group()))


def verify_address(shallow_match):
    match = re.search(pattern_deep, shallow_match)

    if match:
        print(f"{match.group()} is a VALID IPv4 CIDR Block")
    else:
        nearest_value(shallow_match)


shallow_match = re.search(pattern_shallow, string)

if shallow_match:
    print(shallow_match.group())
    verify_address(shallow_match.group())
else:
    print(f"{string} contains INVALID character")
