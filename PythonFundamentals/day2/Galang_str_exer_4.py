string = input("Enter a string: ")
list_string = string.split(" ")

# returns number and next word
print(
    [
        (i, list_string[index + 1])  # stores i and word next to i in tuple
        for index, i in enumerate(list_string)  # enumerate to access index
        if i[0].isnumeric()
        and index < len(list_string) - 1  # checks if first character is a number and if number is the last word
    ]
)
