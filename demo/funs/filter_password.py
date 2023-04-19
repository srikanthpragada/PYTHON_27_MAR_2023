def isvalidpassword(pwd):
    upper = digit = special = False
    for c in pwd:
        if c.isupper():
            upper = True
        elif c.isdigit():
            digit = True
        elif c in "@#_*":
            special = True

    return upper and digit and special


pwds = ['abc123', 'Axy#21', "Xyddd9_", "Adfd7"]

for p in filter(isvalidpassword, pwds):
    print(p)
    