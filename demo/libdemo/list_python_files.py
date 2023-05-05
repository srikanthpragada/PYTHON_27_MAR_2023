import os

allfiles = os.walk(r"d:\classroom\mar27p\demo")

count = 0
for (dirname, dirs, files) in allfiles:
    for file in files:
        if file.endswith(".py"):
            print(dirname + "\\" + file)
            count += 1

print(count)
