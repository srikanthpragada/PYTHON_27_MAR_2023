l1 = [1, 2, 3, 4]
l2 = [10, 20, 30]

for idx, v1 in enumerate(l1):
    if idx < len(l2):
        v2 = l2[idx]
    else:
        v2 = "Unknown"

    print(f"{v1} - {v2}")
