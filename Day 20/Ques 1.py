# Question: Given the size of each family group k and an unordered room number list where all family rooms repeat k times except the Captain's room (appears once), find the Captain's room number.


k = int(input())
rooms = list(map(int, input().split()))
room_set = set(rooms)
print(((sum(room_set) * k) - sum(rooms)) // (k - 1))