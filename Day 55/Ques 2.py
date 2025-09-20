# Problem: Given an integer n, print the decimal, octal, hexadecimal (capitalized), and binary values for each integer from 1 to n. Each value should be space-padded to match the width of the binary value of n and separated by a single space.

def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        deci = str(i)
        octal = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print(deci.rjust(width), octal.rjust(width), hexa.rjust(width), binary.rjust(width))
