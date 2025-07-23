# Question 2:
# Given the size N x M of a door mat (where N is an odd number and M = 3*N), print a design pattern using ., |, and WELCOME in the center.

def print_door_mat(n, m):
    for i in range(1, n, 2):
        print((".|." * i).center(m, "-"))
    print("WELCOME".center(m, "-"))
    for i in range(n - 2, 0, -2):
        print((".|." * i).center(m, "-"))

if __name__ == "__main__":
    n, m = map(int, input().split())
    print_door_mat(n, m)