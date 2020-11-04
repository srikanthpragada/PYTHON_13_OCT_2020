st = "90,i,60,50,abc,70"


# marks = st.split(",")
# total = 0
# for m in marks:
#     total += int(m)
#
# print(total)

def convert_to_int(s):
    if s.isdigit():  # Valid number
        return int(s)
    else:  # Invalid number so return 0
        return 0


print(sum(map(convert_to_int, st.split(","))))

print(sum(map(lambda v: int(v) if v.isdigit() else 0, st.split(","))))
