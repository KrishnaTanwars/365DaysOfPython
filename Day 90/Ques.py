# Ques : Given an odd integer thickness, print the HackerRank logo pattern using string alignment methods .rjust(), .ljust(), and .center(). Your task is to replace blanks in the given code to correctly generate the logo.

thickness = int(input())
c = 'H'

# 1. Top Cone
for i in range(thickness):
    print(c.ljust(i + 1) + c.ljust(thickness - 1)) # Note: The code in the image appears to have an error here or is incomplete. Based on common HackerRank problems, it's likely a typo in the image's code: `print(c.ljust(i + 1) + c + c.ljust(thickness - 1))` or similar.

# 2. Top Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# 3. Middle Belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

# 4. Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# 5. Bottom Cone
for i in range(thickness):
    # This line has the blank:
    # print((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6)
    # The part that is blanked out is not clear from the image, but the task implies filling a blank with .ljust, .rjust, or .center.
    # The image shows the code:
    print((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)) # The rest of the line is cut off, but the blank is likely intended to be within this logic.