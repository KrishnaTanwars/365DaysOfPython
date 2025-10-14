# Ques: Given a spreadsheet of N athletes and their M attributes, you are required to sort the data based on the Kth  attribute (0-indexed) and print the resulting table. If two attributes are the same, print the row that appeared first in the input.

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = [list(map(int, input().split())) for _ in range(n)]
    k = int(input())
    arr.sort(key=lambda x: x[k])
    for row in arr:
        print(*row)