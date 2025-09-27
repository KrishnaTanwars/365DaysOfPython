# Question: Generate a mat-like pattern using string formatting methods like .ljust(), .center(), and .rjust().

import sys

def solve_hackerrank_problem():
    n, m = map(int, sys.stdin.readline().split())

    # Top half
    for i in range(1, n, 2):
        print((".|." * i).center(m, "-"))

    # Middle part
    print("WELCOME".center(m, "-"))

    # Bottom half
    for i in range(n - 2, -1, -2):
        print((".|." * i).center(m, "-"))

if __name__ == "__main__":
    solve_hackerrank_problem()