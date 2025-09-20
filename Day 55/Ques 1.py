# Problem: Given a string of space-separated words, split it on a space delimiter and then join the words using a hyphen.

def split_and_join(line):
    words = line.split(" ")
    return "-".join(words)