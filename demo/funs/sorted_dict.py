marks = {101: 80, 103: 90, 102: 40, 105: 66, 106: 30}

for r, m in sorted(marks.items(), key=lambda t: t[1]):
    print(r, m)
