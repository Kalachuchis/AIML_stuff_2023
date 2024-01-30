import math


def is_prime(num):
    if num < 2:
        return False
    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            return False
    return True


number = input("Please enter a number: ")
print("Will now print all prime numbers until " + number)

for i in range(0, int(number)):
    if is_prime(i):
        print(i)
