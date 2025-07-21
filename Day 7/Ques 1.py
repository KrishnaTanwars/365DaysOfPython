# 🔸 Q1: Mutate a String
# Task: Given a string, change the character at a given index to a new character.
# Input: string, position (int), character (str)
# Output: Modified string

def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input("Enter string: ")
    i, c = input("Enter position and character separated by space: ").split()
    s_new = mutate_string(s, int(i), c)
    print("Modified string:", s_new)
