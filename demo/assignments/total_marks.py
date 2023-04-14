data = ["1,80", "2,50", "1,72", "3,44", "3,60", "2,90"]

students = {}
for entry in data:
    rollno, marks = entry.split(",")
    total = students.get(rollno, 0) + int(marks)
    students[rollno] = total
    # print(students)

for rollno, total in sorted(students.items()):
    print(f"{rollno:5} {total:3}")
