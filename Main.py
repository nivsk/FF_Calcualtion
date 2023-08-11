def calculate_balance(principal, days, interest_rate):
    balance = principal
    for day in range(days):
        interest = balance * (interest_rate / 100)
        balance += interest
    return balance

def format_balance(balance):
    return f"{balance:,.2f}"

principal = float(input("Enter initial amount: "))
interest_rate = float(input("Enter Daily interest: "))  # Daily interest rate
custom_day = int(input("Enter Custom Day: "))
rounded = round(custom_day / 360)

days_list = [30, 60, 90, custom_day]
for days in days_list:
    balance_after_days = calculate_balance(principal, days, interest_rate)
    formatted_balance = format_balance(balance_after_days)
    print(f"Balance after {days} days: {formatted_balance}")
print("Custom days into years(rounded): "+ str(rounded) + " Years")

