data = "90,88,34,,45,56"

marks = filter(str.isdigit, data.split(","))
total = sum(map(int, marks))
print(total)

total = sum([int(m) for m in data.split(",") if m.isdigit()])
print(total)
