def func1(name, age):
    """accepts two arguements and formats"""
    return f"Your name is {name} and your are {age} years"


def func2(*args):
    """accepts multiple arguments and concatenate into a string"""
    return ", ".join(str(i) for i in args)


def func3(a, b=None):
    """optional argument b"""
    b = a if b is not None else b
    return ((a + b), (a * b))


print(func1("Iggy", 26))

print(func2(420, 69, "blaze it"))

print(func3(21, 2))
# no b
print(func3(21))
