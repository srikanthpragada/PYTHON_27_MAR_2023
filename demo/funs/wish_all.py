def wish(*names, msg="Hello"):
    for n in names:
        print(msg, n)


wish("Bill", "Larry", "Andy")
wish("Bill", "Larry", msg="Hi")
