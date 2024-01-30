import re

string = input("Enter a string: ").strip()
char_to_replace = input("String to replace: ").strip()
replace_with = input("New value of string: ")


format_replace_with = re.sub(r"\d", "*", replace_with)


print(
    format_replace_with.join(string.split(char_to_replace))
    if char_to_replace and replace_with
    else string
)
