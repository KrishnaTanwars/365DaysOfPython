# Question 1:
# You are given a string and a width. Your task is to wrap the string into a paragraph of the given width.


import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, width=max_width)

if __name__ == '__main__':
    string = input()
    max_width = int(input())
    result = wrap(string, max_width)
    print(result)