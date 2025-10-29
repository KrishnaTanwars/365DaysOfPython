# Ques : Given a list of integers, find the average of all distinct elements rounded to 3 decimal places. 
# Input: n and n integers → Output: average of unique elements (e.g., 169.375).

def average(array):
    return round(sum(set(array)) / len(set(array)), 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
