nums = [1, 10, -4, -5, 9, -66]


def ispositive(n):
    return n > 0


for n in filter(ispositive, nums):
    print(n)

for c in filter(str.isupper, "AbDef"):
    print(c)
