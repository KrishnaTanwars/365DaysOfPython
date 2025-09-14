Ques : Use a decorator to standardize a list of mobile numbers to the format +91 xxxxx xxxxx.

def wrapper(f):
    def fun(l):
        formatted = ['+91 {} {}'.format(num[-10:-5], num[-5:]) for num in l]
        f(formatted)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)