# Ques : You are given a list of items and their prices from supermarket sales. Print each item’s total price (quantity × price) in the order they first appear.

from collections import OrderedDict
n = int(input())
items = OrderedDict()
for _ in range(n):
    *item_name, price = input().split()
    item = " ".join(item_name)
    price = int(price)
    
    if item in items:
        items[item] += price
    else: 
        items[item] = price
    
for item, net_price in items.items():
    print(item,net_price)
