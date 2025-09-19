# Question: Given an immutable string, how would you change a character at a specific position?

def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]
