fs = "java"
ss = "how are you"

found = []
for c in fs:
    if c not in found and c in ss:
        print(c)
        found.append(c)

found = ""
for c in fs:
    if c not in found and c in ss:
        print(c)
        found = found + c
