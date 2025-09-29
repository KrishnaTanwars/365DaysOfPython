# Ques : A newly opened multinational brand wants to base its company logo on the three most common characters in the company name, S. Given a string S which is the company name in lowercase letters, find the top three most common characters in the string.

from collections import Counter

if __name__ == '__main__':
    s = input().strip()
    for ch, cnt in sorted(Counter(s).items(), key=lambda x: (-x[1], x[0]))[:3]:
        print(ch, cnt)