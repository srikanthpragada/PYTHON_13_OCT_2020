st = 'Python 3.9 is latest!'

upper = lower = others = 0
for ch in st:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    else:
        others += 1

print(f"Uppercase = {upper}, Lowercase = {lower}, Others = {others}")
