import re

string = input("Enter a string: ").strip()


def helper(match):
    match = match.group()
    return f"{match}G{match}" if match.isupper() else f"{match}g{match}"


format_string = re.sub(r"[AEIOUaeiou]", helper, string)


print(format_string)
