l1 = [10, 20, 30]
l2 = ['a', 'b']

for v1, v2 in zip(l1, l2):
    print(v1, v2)

for v1, v2 in zip("abc", "xyz"):
    print(v1, v2)
