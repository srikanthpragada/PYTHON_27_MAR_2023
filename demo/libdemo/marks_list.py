f = None
try:
    f = open("marks.tx", "rt")
    for line in f.readlines():
        parts = line.strip().split(",")
        if len(parts) < 2:
            continue

        name = parts[0]
        marks = [int(v) for v in parts[1:]]
        total = sum(marks)
        avg = total / len(marks)
        print(f"{name:20} {total:3} {avg:5.2f}")

except Exception as ex:
    print("Sorry! : Error ->" + str(ex))
finally:
    if f is not None:
        f.close()
        print("File closed!")
