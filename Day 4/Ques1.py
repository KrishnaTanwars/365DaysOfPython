# Q: Given a string of space-separated words, convert it into a hyphen-separated string.
# Example: Input: "this is a string" → Output: "this-is-a-string"

def split_and_join(line):
    return "-".join(line.split())

if __name__ == '__main__':
    line = input("Enter a space-separated string: ")
    result = split_and_join(line)
    print("Output:", result)
