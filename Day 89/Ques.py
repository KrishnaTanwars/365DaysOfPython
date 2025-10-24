# Ques : Given an integer n, find the smallest numerically balanced number strictly greater than n. A number is numerically balanced if each digit d appears exactly d times.

def split_and_join(line):
    return "-".join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
