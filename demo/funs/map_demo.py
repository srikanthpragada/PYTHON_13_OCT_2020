
st = "90,i,60,50,abc,70"

# marks = st.split(",")
# total = 0
# for m in marks:
#     total += int(m)
#
# print(total)

print(sum(map(int, st.split(","))))


