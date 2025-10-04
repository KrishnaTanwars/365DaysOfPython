# Ques: Happiness Calculation (Python)
# Problem	You have an array of n integers and two disjoint sets, A and B, each containing m integers. For each integer i in the array: if i∈A, you add +1 to your happiness; if i∈B, you add −1 to your happiness. Otherwise, your happiness does not change. Your initial happiness is 0. Output your final happiness.


n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0
for x in arr:
    if x in A:
        happiness += 1
    elif x in B:
        happiness -= 1

print(happiness)
