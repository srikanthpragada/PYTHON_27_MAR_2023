def wish(msg: str, user: str):
    print(msg, user)


wish("Hi", "Bill")  # positional
wish(user="Brian", msg="Hello")  # keyword
wish(10, 20)

