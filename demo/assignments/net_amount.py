
price = int(input("Enter price :"))
qty = int(input("Enter qty :"))

if qty > 3:
    disrate = 30
elif qty > 2:
    disrate = 20
else:
    disrate = 10

amount = qty * price
discount = amount * disrate / 100
net_amount = amount - discount

if net_amount > 10000:
    net_amount = net_amount * 90 / 100

print(net_amount)


