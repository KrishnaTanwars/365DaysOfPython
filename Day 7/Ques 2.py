# 🔸 Q2: Count Substring Occurrences
# Task: Count how many times a substring occurs in a string, including overlapping occurrences.
# Input: string, substring
# Output: Number of occurrences

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input("Enter main string: ").strip()
    sub_string = input("Enter substring: ").strip()
    
    count = count_substring(string, sub_string)
    print("Total occurrences:", count)
