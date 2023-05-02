def numbers():
    for i in range(3):
        yield i


n = numbers()  # generator
print(type(n))
print(next(n))
print(next(n))
