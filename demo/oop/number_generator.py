# Generator
def numbers():
    for n in range(1, 5):
        yield n


n = numbers()
print(n)
print(next(n), next(n))

for v in numbers():
    print(v)
