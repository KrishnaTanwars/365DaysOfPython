# Question:  Given roll numbers of students subscribed to English and French newspapers, print the total number subscribed to only English.

n1 = int(input())
english_set = set(map(int, input().split()))
n2 = int(input())
french_set = set(map(int, input().split()))

print(len(english_set.difference(french_set)))