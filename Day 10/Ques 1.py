# Problem: Print the formatted values of numbers from 1 to 'number'
# Output should show Decimal, Octal, Hexadecimal (uppercase), and Binary
# All values should be right-aligned based on the width of the binary of 'number'

def print_formatted(number):
    width = len(bin(number)[2:])  # Width is length of binary representation
    for i in range(1, number + 1):
        dec = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexa = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        print(dec, octal, hexa, binary)

# Example usage
if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print_formatted(n)
