# Ques : Determine if a row of cubes can be stacked following a non-increasing size rule (new cube≤top cube), by only picking the leftmost or rightmost cube at each step.

from collections import deque

def solve():
    """
    Reads a single test case and determines if the blocks can be stacked 
    using a greedy approach.
    """
    try:
        # Read n, the number of cubes
        n = int(input())
    except:
        return 

    # Read side lengths and convert to a deque
    blocks = deque(map(int, input().split()))
    
    possible = True
    last = float('inf') 

    while blocks:
        can_choose_left = blocks[0] <= last
        can_choose_right = blocks[-1] <= last
        
        if can_choose_left and can_choose_right:
     
            if blocks[0] >= blocks[-1]:
                choice = blocks.popleft()
            else:
                choice = blocks.pop()
        
        elif can_choose_left:
            choice = blocks.popleft()
        
        elif can_choose_right:
            choice = blocks.pop()
        
        else:
            possible = False
            break

        last = choice 

    print("Yes" if possible else "No")

try:
    t = int(input())
    for _ in range(t):
        solve()
except:
    pass