# Question: Validate credit card numbers. A valid card starts with 4, 5, or 6; has 16 digits (optionally separated by hyphens in groups of 4); contains only digits 0-9; and does not have 4 or more consecutive repeated digits.


import re

def is_valid(card):
    # Check format: starts with 4,5,6; 16 digits; optional hyphens
    pattern = r'^[4-6]\d{3}(-?\d{4}){3}$'
    if not re.match(pattern, card):
        return False

    # Remove hyphens for consecutive digit check
    digits = card.replace("-", "")

    # Check for 4 or more consecutive repeated digits
    if re.search(r'(\d)\1{3,}', digits):
        return False

    return True

# Main execution block
n = int(input())
for _ in range(n):
    card = input().strip()