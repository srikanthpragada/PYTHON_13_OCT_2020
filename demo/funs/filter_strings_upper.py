# Select string that contain at least one uppercase letter

def has_upper(st):
    for c in st:
        if c.isupper():
            return True

    return False


names = ['Java', 'javascript', 'PYTHON', 'c#', 'SQL']

for n in filter(has_upper, names):
    print(n)

for n in filter(lambda s: len(s) > 5, names):
    print(n)