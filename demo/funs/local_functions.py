g = 100


def f1():
    n1 = 1
    global g
    g = 10

    def f2():
        n2 = 10
        nonlocal n1
        n1 = 2
        print(g, n1, n2)

    f2()
    print(n1)


f1()
