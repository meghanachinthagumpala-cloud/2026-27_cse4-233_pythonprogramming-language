
# Retail Billing with Multiple Discount Rules

products = []

n = int(input("Enter number of products: "))

subtotal = 0
total_tax = 0

for i in range(n):

    print("\nEnter Product", i + 1, "Details")

    name = input("Enter product name: ")
    category = input("Enter category (electronics/clothing/grocery): ").lower()

    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    # Validate inputs
    if price < 0 or quantity <= 0:
        print("Invalid price or quantity!")
        exit()

    amount = price * quantity

    # Category-specific tax
    if category == "electronics":
        tax_rate = 18

    elif category == "clothing":
        tax_rate = 5

    elif category == "grocery":
        tax_rate = 0

    else:
        print("Invalid category!")
        exit()

    tax = amount * tax_rate / 100

    subtotal += amount
    total_tax += tax

    products.append({
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "amount": amount,
        "tax": tax
    })

# Threshold discount
discount = 0

if subtotal > 5000:
    discount = subtotal * 0.10

# Maximum concession limit
discount = min(discount, 1000)

# Final bill
final_amount = subtotal + total_tax - discount

# Display invoice
print("\n========== RETAIL INVOICE ==========")

for p in products:
    print("\nProduct:", p["name"])
    print("Category:", p["category"])
    print("Price:", p["price"])
    print("Quantity:", p["quantity"])
    print("Amount:", round(p["amount"], 2))
    print("Tax:", round(p["tax"], 2))

print("\nSubtotal:", round(subtotal, 2))
print("Total Tax:", round(total_tax, 2))
print("Discount:", round(discount, 2))
print("Final Payable Amount:", round(final_amount, 2))

print("===================================")

