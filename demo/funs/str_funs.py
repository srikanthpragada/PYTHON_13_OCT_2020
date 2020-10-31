
def count_upper(st):
    count = 0
    for c in st:
        if c.isupper():
            count += 1

    return count


print(count_upper("PYthON"))
