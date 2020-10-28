data = ["1,60", "3,70", "1,76", "2,50", "2,90", "1,70"]

students = {}

for d in data:
    rollno, marks = d.split(",")
    if rollno in students:
        students[rollno].append(marks)  # add marks to existing student
    else:
        students[rollno] = [marks]   # add new student with marks as list

for rollno,marks in sorted(students.items()):
    print(rollno, ",".join(marks))

