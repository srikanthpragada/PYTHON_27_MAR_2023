# Positional only args
def wish(user='Guest', msg="Hello", /):
    print(msg, user)


wish("Scott", "Hi")
wish("Steve")
