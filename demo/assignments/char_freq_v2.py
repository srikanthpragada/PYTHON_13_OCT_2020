
st = "How do you do"

freq = {}

for c in st:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

print(freq)
