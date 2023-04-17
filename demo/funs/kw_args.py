def fun(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


def fun2(*args, **kwargs):
    pass


fun(a=10, b=20, msg="Hello")
fun2(10, 20, 30, a=10, b=20)
