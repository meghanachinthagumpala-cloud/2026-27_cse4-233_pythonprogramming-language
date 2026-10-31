
# Attendance Recovery Computation System

import math

# Student details
name = input("Enter student name: ")

total = int(input("Enter total classes conducted: "))
attended = int(input("Enter classes attended: "))

required = float(input("Enter required attendance percentage: "))

# Validate inputs
if (total <= 0 or attended < 0 or attended > total
        or required <= 0 or required > 100):

    print("Invalid input!")

else:

    # Calculate current attendance
    current = (attended / total) * 100

    print("\n--- ATTENDANCE REPORT ---")
    print("Student Name:", name)
    print("Total Classes:", total)
    print("Classes Attended:", attended)
    print("Current Attendance:", round(current, 2), "%")

    if current >= required:
        print("Status: Eligible")
        print("No recovery classes required.")

    else:
        # Calculate minimum additional classes
        target = required / 100

        needed = math.ceil(
            (target * total - attended) / (1 - target)
        )

        print("Status: Not Eligible")
        print("Minimum Consecutive Classes Required:", needed)

    # Future attendance scenarios
    print("\n--- FUTURE ATTENDANCE SCENARIOS ---")

    scenarios = [5, 10, 15, 20]

    for future in scenarios:

        future_attended = attended + future
        future_total = total + future

        percentage = (
            future_attended / future_total
        ) * 100

        print("After", future, "classes:",
              round(percentage, 2), "%")


