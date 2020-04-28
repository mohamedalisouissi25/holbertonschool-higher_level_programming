#!/usr/bin/python3

for num in range(0, 8):

    for num2 in range(num + 1, 10):
        print("{:d}{:d}".format(num, num2), end=', ')

print("{:d}{:d}".format(num + 1, num2))
