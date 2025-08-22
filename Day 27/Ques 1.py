# Question: Given a row of cubes, you can only pick a cube from the left or right end to stack them vertically. A cube can be placed on top of another only if its side length is less than or equal to the one below it. Determine if it's possible to stack all the cubes.

from collections import deque

T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    cubes = deque(map(int, input().split()))
    top = float('inf')
    possible = True

    while cubes:
        if cubes[0] >= cubes[-1]:
            pick = cubes.popleft()
        else:
            pick = cubes.pop()

        if pick > top:
            possible = False
            break
        top = pick

    print("Yes" if possible else "No")
