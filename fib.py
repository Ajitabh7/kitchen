#! /var/cfengine/bin/python
# simple fibonacci series
# the sum of two elements defines the next set

a, b = 0, 1
while b < 3000:
    print(b, end = ' ', flush = True)
    a, b = b, a + b

print() # line ending
