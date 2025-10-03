# Sorting a String (HackerRank)
# Ques : Sort string S with alphanumeric characters in this order: Lowercase → Uppercase → Odd Digits → Even Digits.

s = input()
print(''.join(sorted(s, key=lambda c: (c.isdigit() - c.islower(), c.isdigit(), int(c) % 2 == 0, c))))