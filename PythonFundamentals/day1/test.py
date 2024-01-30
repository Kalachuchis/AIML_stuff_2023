count = int(input("How many times do you want to say 'Hello': "))

i = 1

while i <=count:
    if count > 10:
        print("I can't say more than 10 times")
        break
    print('Hello')
    i+=1
else: 
    print('This is else block of while!!!')

print('Job is done')
