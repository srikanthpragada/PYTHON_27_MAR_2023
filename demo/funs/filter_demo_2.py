data = ["abc", "pqr", "a123", "x33", "def"]


def hasdigit(s):
    for c in s:
        if c.isdigit():
            return True

    return False


for n in filter(hasdigit, data):
    print(n)
