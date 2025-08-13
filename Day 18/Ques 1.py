# Ques : Given two sets of student roll numbers (English subscribers and French subscribers), print the total number of students subscribed to both.

# Input:
# First line: number of English subscribers (n1)
# Second line: n1 roll numbers
# Third line: number of French subscribers (n2)
# Fourth line: n2 roll numbers

n1 = int(input())
english_set = set(map(int, input().split()))

n2 = int(input())
french_set = set(map(int, input().split()))

print(len(english_set & french_set))  # intersection count
