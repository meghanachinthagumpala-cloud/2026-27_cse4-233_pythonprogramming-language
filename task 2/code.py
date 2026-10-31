
# Progressive Electricity Billing System

bills = []

n = int(input("Enter number of months: "))

for i in range(n):
    print("\nMonth", i + 1)

    units = float(input("Enter electricity units: "))

    # Calculate slab charges
    if units <= 100:
        energy = units * 2

    elif units <= 200:
        energy = (100 * 2) + (units - 100) * 3

    elif units <= 300:
        energy = (100 * 2) + (100 * 3) + (units - 200) * 5

    else:
        energy = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

    fixed = 50

    # Calculate surcharge
    surcharge = 0
    if units > 300:
        surcharge = energy * 0.05

    # Calculate rebate
    rebate = 0
    if units < 100:
        rebate = energy * 0.05

    total = energy + fixed + surcharge - rebate

    bills.append(total)

    print("Energy Charges:", energy)
    print("Fixed Charges:", fixed)
    print("Surcharge:", surcharge)
    print("Rebate:", rebate)
    print("Total Bill: Rs.", round(total, 2))

# Compare monthly bills
print("\n--- Monthly Bill Comparison ---")

for i in range(n):
    print("Month", i + 1, ": Rs.", round(bills[i], 2))

# Identify unusual increases
print("\n--- Unusual Bill Increases ---")

found = False

for i in range(1, n):
    increase = ((bills[i] - bills[i-1]) / bills[i-1]) * 100

    if increase > 30:
        print("Month", i + 1,
              "has an unusual increase of",
              round(increase, 2), "%")
        found = True

if not found:
    print("No unusual increases found.")

