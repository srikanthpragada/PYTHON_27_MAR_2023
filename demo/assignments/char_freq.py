
st = "how do you do"

found = []
for c in st:
    if c not in found:
        print(f"{c} - {st.count(c)}")
        found.append(c)

