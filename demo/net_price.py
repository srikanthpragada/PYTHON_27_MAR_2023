# Take price and display net price after a discount of 10%

price = int(input("Enter price :"))
discount = price * 10 // 100    # 10%
net_price = price - discount


print(f"Price      {price:6}")
print(f"Discount   {discount:6}")
print(f"Net price  {net_price:6}")
