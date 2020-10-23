st = "How do you do"
w = "did"

pos = -1
while True:
    pos = st.find(w, pos + 1)
    if pos == -1:
        break

    print(pos)
