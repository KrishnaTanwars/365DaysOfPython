# Ques : Given a list of plant heights, find the average height considering only distinct values. Print the result rounded to 3 decimal places.

def average(array):
    return round(sum(set(array)) / len(set(array)), 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)