# Ques : You are given cubes in a row; you may pick only from left or right and must stack cubes so each new cube ≤ previous cube.
# For each test case, print Yes if such stacking is possible, else No.

from collections import deque

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        blocks = deque(map(int, input().split()))
        
        last = float('inf')     # the top of the stack
        
        possible = True
        while blocks:
            # pick the larger cube from either end
            if blocks[0] >= blocks[-1]:
                pick = blocks.popleft()
            else:
                pick = blocks.pop()
            
            if pick > last:     # violates condition
                possible = False
                break
            
            last = pick
        
        print("Yes" if possible else "No")
