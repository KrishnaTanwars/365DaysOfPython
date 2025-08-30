# Question: Given a number N, generate the first N Fibonacci numbers. Then, use map and a lambda function to cube each Fibonacci number and print the resulting list.


cube = lambda x: x**3 

def fibonacci(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))