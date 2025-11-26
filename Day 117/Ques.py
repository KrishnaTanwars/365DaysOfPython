# Ques : Piling Up! (Pick cubes left/right to form stack)
from collections import deque
for _ in range(int(input())):
    dq=deque(map(int,input().split()));p=float('inf');f=1
    while dq:
        x=dq.popleft() if dq[0]>=dq[-1] else dq.pop()
        if x<=p:p=x
        else:f=0;break
    print("Yes" if f else "No")