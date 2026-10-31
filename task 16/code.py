
# Multi-Day Water Tank Simulation

capacity = float(input("Enter tank capacity in litres: "))

water = float(input("Enter initial water level: "))

threshold = float(input("Enter target water level: "))

days = int(input("Enter number of days: "))

# Validate input
if (capacity <= 0 or water < 0 or water > capacity
        or threshold < 0 or threshold > capacity or days <= 0):

    print("Invalid input!")

else:

    overflow_total = 0
    shortage_total = 0
    first_threshold = None

    print("\n--- WATER TANK REPORT ---")

    for day in range(1, days + 1):

        print("\nDay", day)

        inflow = float(input("Enter water inflow: "))
        outflow = float(input("Enter water outflow: "))

        if inflow < 0 or outflow < 0:
            print("Invalid inflow or outflow!")
            continue

        # Calculate water level
        new_water = water + inflow - outflow

        # Detect overflow
        if new_water > capacity:

            overflow = new_water - capacity
            overflow_total += overflow

            new_water = capacity

            print("Overflow:", overflow, "litres")

        else:
            print("Overflow: 0 litres")

        # Detect shortage
        if new_water < 0:

            shortage = abs(new_water)
            shortage_total += shortage

            new_water = 0

            print("Water Shortage:", shortage, "litres")

        else:
            print("Water Shortage: 0 litres")

        water = new_water

        print("Current Water Level:", water, "litres")

        # Check threshold
        if first_threshold is None and water >= threshold:
            first_threshold = day

            print("Target Threshold Reached!")

    # Final Report
    print("\n--- FINAL WATER TANK SUMMARY ---")

    print("Final Water Level:", water, "litres")
    print("Total Overflow:", overflow_total, "litres")
    print("Total Shortage:", shortage_total, "litres")

    if first_threshold is not None:
        print("First Threshold Reached on Day:", first_threshold)
    else:
        print("Threshold Not Reached")

