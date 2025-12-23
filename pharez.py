def calculate_tax():
    print("Filing Statuses:")
    print("0 - Single")
    print("1 - Married Filing Jointly or Qualifying Widow(er)")
    print("2 - Married Filing Separately")
    print("3 - Head of Household")
    
    # Prompt user for input
    try:
        status = int(input("Enter the filing status (0, 1, 2, or 3): "))
        income = float(input("Enter the taxable income: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    # Tax brackets for 2009 
    brackets = [
        [8350, 33950, 82250, 171550, 372950],   
        [16700, 67900, 137050, 208850, 372950], 
        [8350, 33950, 68525, 104425, 186475],   
        [11950, 45500, 117450, 190200, 372950]  
    ]
    
    rates = [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]

    if status < 0 or status > 3:
        print("Error: Invalid status selected.")
        return

    # Select the brackets for the specific filing status
    current_brackets = brackets[status]
    tax = 0.0
    
    # Logic to calculate progressive tax
    if income <= current_brackets[0]:
        tax = income * rates[0]
    else:
        # Tax for the first bracket
        tax = current_brackets[0] * rates[0]
        
        # Calculate for middle brackets
        for i in range(1, len(current_brackets)):
            if income > current_brackets[i]:
                tax += (current_brackets[i] - current_brackets[i-1]) * rates[i]
            else:
                tax += (income - current_brackets[i-1]) * rates[i]
                break
        else:
            # If income is higher than the last bracket threshold (35% bracket)
            tax += (income - current_brackets[-1]) * rates[-1]

    print(f"Tax is ${tax:,.2f}")

# Run the function
if __name__ == "__main__":
    calculate_tax()
