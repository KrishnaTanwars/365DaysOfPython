# Problem: Create an alphabet rangoli of the given size
# Use lowercase English letters centered with hyphens

def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase

    lines = []
    for i in range(size):
        left = '-'.join(alpha[size-1:i:-1])
        center = alpha[i]
        right = '-'.join(alpha[i+1:size])
        full = left + '-' + center + ('-' + right if right else '')
        lines.append(full.center(4 * size - 3, '-'))

    # Print rangoli with mirror symmetry (top and bottom)
    print('\n'.join(lines[::-1] + lines[1:]))

# Example usage
if __name__ == '__main__':
    n = int(input("Enter size of rangoli: "))
    print_rangoli(n)
