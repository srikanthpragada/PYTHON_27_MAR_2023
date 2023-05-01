st = "a0"

try:
    n = int(st)
    print(100 // n)
except ValueError:
    print("Invalid Number")
except Exception as ex:
    print("Sorry! " + str(ex))
else:
    print("Done")
finally:
    print("Finally!")

print("The End")
