def read_file(path):
    file = open(path, "r")

    try:
        contents = file.read()
        print(contents)
        return contents
    except Exception as e:
        print(str(e))
    finally:
        file.close()
        print("uwu")

if __name__ == "__main__":
    path = "hello.txt"
    with open(path, "r") as f:
        contents = f.read()
        print(contents)
