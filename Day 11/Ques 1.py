# Q1: Capitalize Full Name Properly
# Description:
# You are given a full name as input. Capitalize the first letter of each word.
# Note: Only the first character of each word should be capitalized.
# Example: Input: "alison heck" → Output: "Alison Heck"

def capitalize_full_name(name):
    return ' '.join(word.capitalize() for word in name.split())

# Input
full_name = input("Enter full name: ")

# Output
print(capitalize_full_name(full_name))
