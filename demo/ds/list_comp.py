squares = []
for n in range(1, 10):
    squares.append(n * n)

print(squares)

squares = [n * n for n in range(1, 10)]
print(squares)

codes = [ord(c) for c in "ABC 123 xyz" if c.isupper()]
print(codes)
