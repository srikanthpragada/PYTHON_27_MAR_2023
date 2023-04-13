names = ["java", "javascript", 'java', 'ruby', 'typescript']
chars = set()
for n in names:
    chars = chars | set(n)
    # print(chars)

print(chars)
