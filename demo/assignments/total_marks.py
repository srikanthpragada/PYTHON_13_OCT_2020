
st = "90,89,67,56,90,88,91"

total = 0
for m in st.split(","):
    total += int(m)

print(total)

# print(sum(map(int, st.split(","))))
