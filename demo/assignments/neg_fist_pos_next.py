nums = [10, -2, 30, 40, -55, -60, 100, -42]
l = []
# Negative numbers
for n in nums:
    if n < 0:
        l.append(n)

# Positive numbers
for n in nums:
    if n >= 0:
        l.append(n)

print(l)
