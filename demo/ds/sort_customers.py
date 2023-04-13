data = ["Bill,393993333", "Joe,28282222",
        "Mike,38383333","Andy,29191111"]

customers = {}
for entry in data:
   name, mobile = entry.split(",")
   customers[name] = mobile

for name, mobile in sorted(customers.items()):
    print(f"{name:20} {mobile}")


