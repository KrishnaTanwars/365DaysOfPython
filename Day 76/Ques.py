# Question: Given a spreadsheet containing a list of N athletes and their M attributes, sort the data based on the Kth  attribute (0-indexed). If two athletes have the same value for the Kth  attribute, maintain the order they appeared in the input.

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().split())))

    k = int(input())

    arr.sort(key=lambda x: x[k])

    for row in arr:
        print(*row)