try:
    f = open("names.txt", "rt")
    for line in f.readlines():
        print(line.strip())

    f.close()
except Exception as ex:
    print("Sorry! : Error ->" + str(ex))

