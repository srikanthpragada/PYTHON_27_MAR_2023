# Take 5 numbers and display total
total = 0
while True:     # infinite loop
    num = int(input("Enter number [0 to stop] :"))
    if num == 0:
        break

    total += num

print(total)
