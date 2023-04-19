data = ["abc1", "erepqr22", "a123", "aaaax33", "d1"]

def extract_digits(s):
    ns = ""
    for c in s:
        if c.isdigit():
            ns += c

    return ns


for n in map(extract_digits, data):
    print(n)