n = int(input("Enter number of students: "))

students = []

for i in range(n):
    print("\nEnter details of student", i + 1)

    name = input("Name: ")
    aggregate = float(input("Aggregate marks: "))

    s1 = float(input("Subject 1 marks: "))
    s2 = float(input("Subject 2 marks: "))
    s3 = float(input("Subject 3 marks: "))

    attendance = float(input("Attendance: "))
    income = float(input("Family income: "))

    if (aggregate >= 75 and
        s1 >= 60 and s2 >= 60 and s3 >= 60 and
        attendance >= 75 and income <= 250000):

        students.append((name, aggregate,
                         attendance, income))

    else:
        print(name, "is not eligible")

# Ranking eligible students
students.sort(key=lambda x: (-x[1], -x[2], x[3]))

print("\n--- Scholarship Ranking ---")

if len(students) == 0:
    print("No eligible students")

else:
    for rank, student in enumerate(students, 1):
        print(rank, student[0],
              "Marks:", student[1],
              "Attendance:", student[2],
              "Income:", student[3])

