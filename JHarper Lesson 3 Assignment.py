while True:
    try:
        investment_amount = int(input("Enter the investment amount (between 1 and 50,000): "))
        if 0 < investment_amount < 50000:
            break
        else:
            print("Your investment amount must be between 1 and 50000. Please try again.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    try:
        interest_rate = int(input("Enter the yearly interest rate (between 1 and 15): "))
        if 0 < interest_rate < 15:
            break
        else:
            print("Your interest rate must be between 1 and 15. Please try again.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    try:
        years = int(input("Enter the investment duration in years (greater than 0): "))
        if years > 0:
            break
        else:
            print("Your investment duration must be greater than 0. Please try again.")
    except ValueError:
        print("Please enter a valid number.")

months = years * 12
monthly_interest_rate = (interest_rate / 12) / 100

total_value = investment_amount

for month in range(1, months + 1):
    interest = total_value * monthly_interest_rate
    total_value += round(interest, 2)
    if month % 12 == 0:
        current_year = month // 12
        print(f"Year {current_year}: ${total_value:.2f}")

print("\n--- Final Investment Details ---")
print(f"Investment duration: {years} years.")
print(f"Yearly Interest Rate: {interest_rate}%")
print(f"Initial Investment: ${investment_amount}")
print(f"Total Value after {years} years: ${round(total_value, 2):.2f}")
print("Completed by, Jacob Harper")
