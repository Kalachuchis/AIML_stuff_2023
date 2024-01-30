n = int(input("Enter a number: "))
string = input("Enter a string: ")
list_string = string.split(" ")

# returns list of all adjecent words in groups of n
print(
    [
        list_string[index : index + n]
        for index, i in enumerate(list_string[: 1 - n if n > 1 else None]) # list only until nth to the last word
    ]
)
