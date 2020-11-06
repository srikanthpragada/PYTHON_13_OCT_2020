def extract_upper(st):
    upper = []
    for ch in st:
        if ch.isupper():
            upper.append(ch)

    return "".join(upper)


def has_upper(st):
    for ch in st:
        if ch.isupper():
            return True

    return False


