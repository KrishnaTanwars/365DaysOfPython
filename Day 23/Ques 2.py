# Question: Given a string `s` and an integer `k`, split `s` into `n/k` substrings. For each substring, create a new string containing its unique characters in their original order, and print each new string on a new line.

def merge_the_tools(string, k):
    """
    Splits a string into substrings of length k and prints unique characters
    from each substring in order.
    """
    for i in range(0, len(string), k):
        # Get the substring of length k
        substring = string[i : i+k]
        
        # Use a dictionary to maintain order and uniqueness
        # (dict keys in Python 3.7+ are ordered)
        unique_chars_ordered = "".join(dict.fromkeys(substring))
        
        print(unique_chars_ordered)


s = 'AABCAAADA'
k = 3
print(f"Processing string '{s}' with k={k}:")
# Expected Output:
# AB
# CA
# AD
merge_the_tools(s, k)

print("-" * 20)

s = 'AAABCADDE'
k = 3
print(f"Processing string '{s}' with k={k}:")
# Expected Output:
# A
# BCA
# DE
merge_the_tools(s, k)