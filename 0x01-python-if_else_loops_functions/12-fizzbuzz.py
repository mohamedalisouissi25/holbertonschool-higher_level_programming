#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 100 + 1):
        if num % 3 == 0:
            print("Fizz", end='')
        if num % 5 == 0:
            print("Buzz", end='')
        if num % 3 and num % 5:
            print("{:d}".format(num), end='')
        print(end=' ')
