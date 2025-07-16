# Problem Statement (Summary):
# Print the list of integers from 1 through n without using string methods or spaces between them.
# For example, if n = 5, output: 12345

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        print(i, end="")
