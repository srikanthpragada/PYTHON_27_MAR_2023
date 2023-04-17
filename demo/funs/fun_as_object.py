def fun():
    print("Function")


print(type(fun))
print(id(fun))
fun2 = fun

fun()
fun2()


