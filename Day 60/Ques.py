# Question : In Python, a string of text can be aligned left, right and center... You are given a partial code that is used for generating the HackerRank Logo of variable thickness. Your task is to replace the blank [_____] with .ljust, .rjust or .center.

thickness = int(input())
c = 'H'

for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

for i in range(thickness):
    print((c*(thickness-i-1)).rjust(thickness*2)+(c*(thickness-i-1)).rjust(thickness*6))