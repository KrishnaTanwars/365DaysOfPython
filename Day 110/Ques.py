#Ques : Given a row of cube lengths, choose cubes from either end to stack them so each upper cube is smaller or equal in size.
# Print "Yes" if stacking is possible, otherwise print "No".

from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    blocks = deque(map(int, input().split()))
    possible = True
    last = float('inf')

    while blocks:
        if blocks[0] >= blocks[-1]:
            choice = blocks.popleft()
        else:
            choice = blocks.pop()

        if choice > last:
            possible = False
            break
        last = choice

    print("Yes" if possible else "No")