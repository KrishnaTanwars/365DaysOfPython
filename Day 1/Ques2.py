# 🏅 Problem: Find the Runner-Up Score
# You're given a list of scores. Find the second highest (runner-up) score.

# 📌 Input Format
# First line: Integer n (number of scores)

# Second line: n space-separated integers (the scores)

if __name__ == "__main__":
    n = int(input())
    arr = map(int,input().split())
    arr = list(arr)
    unique_scores = list(set(arr))
    unique_scores.sort(reverse=True)
    print(unique_scores[1])