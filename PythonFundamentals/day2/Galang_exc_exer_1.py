string = input("Input: ")


try:
    index = int(input("Index: "))
    string_list = [int(i) for i in string.split(",")]

    print(string_list[index - 1])
except ValueError:
    print("ValueError: List should contain numbers only")
except IndexError:
    print(
        f"Item at index {index} is not found. The length of collection is just {len(string_list)}"
    )
