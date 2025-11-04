number = 1

for i in range(1, 1001):
    if i%15 == 0:
        print("Fizzbuzz")
    elif i%5 == 0:
        print("Buzz")
    elif i%3 == 0:
        print("Fizz")
    else:
        print(i)


#Mi Solución
'''
while number <=1000:

    if number % 15 == 0:
        print("Fizzbuzz")
    elif number %3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    number += 1
'''