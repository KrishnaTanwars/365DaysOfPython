# Ques : Count points by calculating contributions of each starting letter (vowel for Kevin, consonant for Stuart) using: `points = len(S) - i` for index `i`. Compare totals to declare the winner or draw.

def minion_game(string):
    vowels = 'AEIOU'
    kevin = 0
    stuart = 0
    n = len(string)
    for i in range(n):
        if string[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
