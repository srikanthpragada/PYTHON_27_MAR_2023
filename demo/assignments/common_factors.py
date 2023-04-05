# Common factors
num1, num2 = 33, 20

smallest = num1 if num1 < num2 else num2

found = False
for i in range(2, smallest//2 + 1):
    if num1 % i == 0 and num2 % i == 0:
        print(i)
        found = True

if not found:
    print("No common factors")





