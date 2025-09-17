# Question: Debug the given function print_from_stream using the default value of one of its arguments. The function should print the first n values returned by the get_next() method of a stream object. If the stream argument is not provided, it should use an instance of the EvenStream class.

def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())