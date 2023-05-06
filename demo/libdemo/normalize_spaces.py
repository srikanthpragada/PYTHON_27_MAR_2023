import re

with open("story.txt", "rt") as f:
    contents = f.read()

# replace one or more spaces with one space
new_contents = re.sub(' +', ' ', contents)

# replace one or more newlines with one newline
new_contents = re.sub("\n+", '\n', new_contents)

#print(new_contents)

# write back to original file
with open("story.txt", "wt") as f:
    f.write(new_contents)


