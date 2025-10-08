class EvenStream(object):
    def __init__(self):
        self.current = 0
    def get_next(self):
        result = self.current
        self.current += 2
        return result

class OddStream(object):
    def __init__(self):
        self.current = 1
    def get_next(self):
        result = self.current
        self.current += 2
        return result

def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream() 
    for _ in range(n):
        print(stream.get_next())

queries = int(input())
for _ in range(queries):
    stream_name, n_str = input().split()
    n = int(n_str)
    
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())