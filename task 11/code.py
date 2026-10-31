
# Examination Result and Grace-Mark Validation

name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))

marks = []
final_marks = []

PASS_MARK = 35
MAX_MARK = 100
GRACE = 5

for i in range(n):
    mark = float(input("Enter marks for subject " + str(i + 1) + ": "))

    if mark < 0 or mark > MAX_MARK:
        print("Invalid marks! Enter marks between 0 and 100.")
        exit()

    marks.append(mark)

print("\n--- Result Processing ---")

for i in range(n):
    mark = marks[i]
    grace = 0

    if mark < PASS_MARK:
        required = PASS_MARK - mark

        if required <= GRACE:
            grace = required
            mark = mark + grace

    final_marks.append(mark)

    print("\nSubject", i + 1)
    print("Original Marks:", marks[i])
    print("Grace Marks:", grace)
    print("Final Marks:", mark)

# Calculate total and percentage
total = sum(final_marks)
percentage = total / n

# Check final result
if all(mark >= PASS_MARK for mark in final_marks):

    if percentage >= 75:
        result = "Distinction"
    elif percentage >= 60:
        result = "First Class"
    elif percentage >= 50:
        result = "Second Class"
    else:
        result = "Pass"

else:
    result = "Fail"

print("\n--- Final Examination Result ---")
print("Student Name:", name)
print("Total Marks:", total, "/", n * MAX_MARK)
print("Percentage:", round(percentage, 2), "%")
print("Final Classification:", result)

