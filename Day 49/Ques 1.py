# Ques : Validate a UID based on specific rules: must contain at least 2 uppercase English alphabet characters, at least 3 digits, only alphanumeric characters, no character repetition, and must be exactly 10 characters long.

import re
for _ in range(int(input())):
    uid = input().strip()
    if (len(uid) == 10 and uid.isalnum() and len(set(uid)) == 10 and len(re.findall(r'[A-Z]', uid)) >= 2 and len(re.findall(r'\d', uid)) >= 3):
        print("Valid")
    else:
        print("Invalid")