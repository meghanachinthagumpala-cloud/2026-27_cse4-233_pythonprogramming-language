
# Campus Event Financial Planning System

# Input details
participants = int(input("Enter number of participants: "))

venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))

catering = float(input("Enter catering cost per participant: "))
transport = float(input("Enter transport cost per participant: "))
certificate = float(input("Enter certificate cost per participant: "))

sponsorship = float(input("Enter sponsorship amount: "))

# Calculate fixed and variable costs
fixed_cost = venue + equipment

variable_cost = catering + transport + certificate

total_variable = variable_cost * participants

total_cost = fixed_cost + total_variable

# Calculate sponsorship shortfall
shortfall = max(0, total_cost - sponsorship)

# Calculate participant contribution
if participants > 0:
    contribution = shortfall / participants
else:
    contribution = 0

# Break-even registration calculation
if variable_cost > 0:
    remaining = fixed_cost - sponsorship

    if remaining <= 0:
        break_even = 0
    else:
        break_even = int(remaining / variable_cost) + 1
else:
    break_even = 0 if sponsorship >= fixed_cost else -1

# Display results
print("\n--- EVENT FINANCIAL REPORT ---")

print("Fixed Cost:", fixed_cost)
print("Variable Cost:", total_variable)
print("Total Event Cost:", total_cost)

print("Sponsorship:", sponsorship)
print("Sponsorship Shortfall:", shortfall)

print("Participant Contribution: Rs.", round(contribution, 2))

if break_even == -1:
    print("Break-even cannot be achieved through registrations.")
else:
    print("Minimum Registrations to Break Even:", break_even)

print("Current Participants:", participants)

if participants >= break_even:
    print("Event is financially feasible.")
else:
    print("More registrations are required.")

