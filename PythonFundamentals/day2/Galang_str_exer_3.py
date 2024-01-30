n = int(input("Enter a number: "))
d = int(input("Enter a number: "))


# prints list of number 0 to n that are divisible by b
print([i for i in range(n + 1) if i % d == 0])
