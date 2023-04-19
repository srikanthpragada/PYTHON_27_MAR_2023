data = ["abc", "erepqr", "a123", "aaaax33", "d"]


for n in map(len, data):
    print(n)

for n in map(str.upper, data):
    print(n)