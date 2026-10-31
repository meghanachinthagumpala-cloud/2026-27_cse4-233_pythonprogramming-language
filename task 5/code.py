
# Multi-Plan Telecommunications Cost Optimization

data_usage = float(input("Enter data usage in GB: "))
call_usage = float(input("Enter call usage in minutes: "))
required_validity = int(input("Enter required validity days: "))
budget = float(input("Enter your budget: "))

n = int(input("Enter number of mobile plans: "))

plans = []

for i in range(n):

    print("\nEnter Plan", i + 1, "Details")

    name = input("Enter plan name: ")
    price = float(input("Enter plan price: "))
    data_limit = float(input("Enter data limit in GB: "))
    call_limit = float(input("Enter call limit in minutes: "))
    validity = int(input("Enter validity days: "))

    extra_data_rate = float(
        input("Enter extra data charge per GB: ")
    )

    extra_call_rate = float(
        input("Enter extra call charge per minute: ")
    )

    # Validate plan details
    if (price < 0 or data_limit < 0 or call_limit < 0
        or validity < 0 or extra_data_rate < 0
        or extra_call_rate < 0):
        print("Invalid plan details!")
        continue

    # Check validity
    if validity < required_validity:
        print("Plan not eligible: Insufficient validity")
        continue

    # Calculate excess usage
    extra_data = max(0, data_usage - data_limit)
    extra_calls = max(0, call_usage - call_limit)

    data_charge = extra_data * extra_data_rate
    call_charge = extra_calls * extra_call_rate

    total_cost = price + data_charge + call_charge

    # Check budget
    if total_cost <= budget:

        plans.append({
            "name": name,
            "price": price,
            "extra_data": extra_data,
            "extra_calls": extra_calls,
            "total": total_cost
        })

# Find economical plan
print("\n--- MOBILE PLAN COMPARISON ---")

if plans:

    plans.sort(key=lambda x: x["total"])

    for plan in plans:
        print("\nPlan Name:", plan["name"])
        print("Base Price:", plan["price"])
        print("Extra Data:", plan["extra_data"], "GB")
        print("Extra Calls:", plan["extra_calls"], "minutes")
        print("Total Cost: Rs.", round(plan["total"], 2))

    best = plans[0]

    print("\n--- MOST ECONOMICAL PLAN ---")
    print("Plan Name:", best["name"])
    print("Total Cost: Rs.", round(best["total"], 2))

else:
    print("No eligible mobile plans found.")

