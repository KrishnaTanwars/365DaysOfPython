# Ques : Print a palindromic number triangle of size n using exactly one print statement inside the loop and no strings.

for i in range(1, int(input())+1):
    print(i*(10**i//9) - (i//10)*(10**(i//10+1)//9))
