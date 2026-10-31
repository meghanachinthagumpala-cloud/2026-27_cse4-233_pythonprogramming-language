
# ATM Transaction Sequence Simulation

balance = float(input("Enter initial balance: "))

if balance < 0:
    print("Invalid initial balance!")
    exit()

n = int(input("Enter number of transactions: "))

if n < 0:
    print("Invalid number of transactions!")
    exit()

total_deposits = 0
total_withdrawals = 0
rejected = 0

MAX_WITHDRAWAL = 10000

for i in range(n):

    print("\nTransaction", i + 1)

    transaction = input(
        "Enter transaction type (deposit/withdraw): "
    ).lower()

    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Rejected: Invalid amount")
        rejected += 1

    elif transaction == "deposit":

        balance += amount
        total_deposits += amount

        print("Deposit Successful")

    elif transaction == "withdraw":

        if amount > MAX_WITHDRAWAL:
            print("Rejected: Withdrawal limit exceeded")
            rejected += 1

        elif amount > balance:
            print("Rejected: Insufficient balance")
            rejected += 1

        else:
            balance -= amount
            total_withdrawals += amount

            print("Withdrawal Successful")

    else:
        print("Rejected: Invalid transaction type")
        rejected += 1

    print("Current Balance: Rs.", round(balance, 2))


# Transaction Summary
print("\n--- ATM TRANSACTION SUMMARY ---")

print("Initial Balance: Rs.", round(
    balance - total_deposits + total_withdrawals, 2
))

print("Total Deposits: Rs.", round(total_deposits, 2))
print("Total Withdrawals: Rs.", round(total_withdrawals, 2))
print("Rejected Transactions:", rejected)
print("Final Balance: Rs.", round(balance, 2))

print("Thank you for using ATM!")

