"""🧮 Problem 1: Hash a Tuple
📌 Description:
Given an integer n, and n space-separated integers, create a tuple of those integers. Then compute and print the hash value of the tuple.

Note: This version is for Python 2, as required by HackerRank to produce a consistent hash output."""


if __name__ == '__main__':
    n = input()
    integer_list = map(int, raw_input().split())
    print hash(tuple(integer_list))