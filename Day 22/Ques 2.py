# Question: Kevin and Stuart play a game with a string. Both players have to make all possible substrings from the given string.

# Stuart gets points for substrings starting with consonants.

# Kevin gets points for substrings starting with vowels (A, E, I, O, U).

# A player gets +1 point for each occurrence of the substring. Your task is to determine the winner and their score.


def minion_game(string):
    vowels = "AEIOU"
    kevin_score = 0
    stuart_score = 0
    n = len(string)
    for i in range(n):
        if string[i] in vowels:
            kevin_score += n - i
        else:
            stuart_score += n - i

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
