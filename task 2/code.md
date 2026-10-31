1. Problem Statement
To develop a Python program that calculates household electricity bills based on multiple consumption slabs, fixed charges, surcharges, and rebates. The system compares electricity bills across several months and identifies unusual increases in monthly bills.
2. Algorithm
1. Start the program.
2. Enter the number of months.
3. Enter electricity consumption units for each month.
4. Calculate energy charges using progressive slabs:
   - 0–100 units: ₹2 per unit.
   - 101–200 units: ₹3 per unit.
   - 201–300 units: ₹5 per unit.
   - Above 300 units: ₹7 per unit.
5. Add fixed charges of ₹50.
6. Calculate a 5% surcharge if consumption exceeds 300 units.
7. Apply a 5% rebate if consumption is below 100 units.
8. Calculate the final electricity bill.
9. Compare monthly bills.
10. Identify unusual increases if the bill increases by more than 30% compared with the previous month.
11. Display monthly bills and unusual increases.
12. Stop.
3. ```mermaid
   

    A([START]) --> B[/Enter Number of Months/]
    B --> C[/Enter Electricity Units/]
    C --> D{Check Consumption Slab}

    D -->|0-100| E[Calculate at Rs.2 per unit]
    D -->|101-200| F[Calculate at Rs.3 per unit]
    D -->|201-300| G[Calculate at Rs.5 per unit]
    D -->|Above 300| H[Calculate at Rs.7 per unit]

    E --> I[Add Fixed Charges]
    F --> I
    G --> I
    H --> I

    I --> J{Units Above 300?}
    J -->|Yes| K[Add 5% Surcharge]
    J -->|No| L{Units Below 100?}
    K --> L

    L -->|Yes| M[Apply 5% Rebate]
    L -->|No| N[Calculate Final Bill]
    M --> N

    N --> O[Store Monthly Bill]
    O --> P{More Months?}
    P -->|Yes| C
    P -->|No| Q[Compare Monthly Bills]

    Q --> R{Increase Above 30%?}
    R -->|Yes| S[Display Unusual Increase]
    R -->|No| T[Display Normal Increase]

    S --> U[/Display All Bills/]
    T --> U
    U --> V([STOP])

   ```
4. hus, the Progressive Electricity Billing System is successfully implemented using Python. It calculates electricity bills using multiple slabs, fixed charges, surcharges, and rebates, compares monthly bills, and identifies unusual increases.

Note: The electricity rates and billing rules used here are assumed values for this programming exercise, not official electricity tariff rates.







medium.com
