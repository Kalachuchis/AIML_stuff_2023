string = input("Input text: ").strip()

dirty_pair = [i for i in string.split(",")]

clean_pairs = []

max_key = 0
max_val = 0

try:
    for index, i in enumerate(dirty_pair):
        # gets the words/attribute for the pair
        key = " ".join([i for i in i.strip().split(" ") if i.isalpha()]).strip()

        # gets the number value for the pair
        value = [i for i in i.strip().split(" ") if i.isnumeric()][0]

        # finds the max length for key and value
        if len(key) > max_key:
            max_key = len(key)
        if len(value) > max_val:
            max_val = len(value)
        if len(value) + len(key) > 50:
            raise ValueError("Length exceeded 50 characters")

        print(len(value) + len(key))
        clean_pairs.append((key, value))

    print("")
    print("Ugly output")
    print("-----------")
    for i in clean_pairs:
        print(i[0], i[1])

    print("")
    print("Beautified Output")
    print("-----------------")
    for i in clean_pairs:
        len_key = len(i[0])
        len_val = len(i[1])
        space_key = " " * (max_key - len_key)
        space_val = " " * (max_val - len_val)

        val_out = f"{i[0]}{space_key}: {space_val}{i[1]}"
        print(val_out)
except Exception as e:
    print(e)
