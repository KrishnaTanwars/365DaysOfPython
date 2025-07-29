# Question: Print each item name and total price in order of first occurrence. Items may repeat.

from collections import OrderedDict

n = int(input())
items = OrderedDict()

for _ in range(n):
    *item_name, price = input().split()
    name = ' '.join(item_name)
    price = int(price)
    items[name] = items.get(name, 0) + price

for item, total in items.items():
    print(item, total)