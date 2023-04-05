# smallest factor other than 1
# for prime numbers it must be number itself
num = 37

for i in range(2, num//2 + 1):
    if num % i == 0:
        print(i)
        break
else:
    print(num)


