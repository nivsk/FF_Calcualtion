import random
import matplotlib.pyplot as plt

def format_number(number):
    return '${:,.2f}'.format(number)

def calculate_taxes(income):
    if 0 <= income <= 11000:
        tax_amount = 0
    elif 11001 <= income <= 44725:
        tax_amount = (income - 11000) * 0.10
    elif 44726 <= income <= 95375:
        tax_amount = 3372.50 + (income - 44725) * 0.12
    elif 95376 <= income <= 182100:
        tax_amount = 9635 + (income - 95375) * 0.22
    elif 182101 <= income <= 231250:
        tax_amount = 27245 + (income - 182100) * 0.24
    elif 231251 <= income <= 578125:
        tax_amount = 47569 + (income - 231250) * 0.32
    else:
        tax_amount = 150689.50 + (income - 578125) * 0.37
    
    return tax_amount

def main():
    annual_salary = float(input("Enter your annual salary: "))
    monthly_rent = float(input("Enter your monthly rent: "))
    necessary_expenses = float(input("Enter monthly necessary expenses (food, water, etc.): "))
    insurance = float(input("Enter monthly insurance expense: "))
    
    discretionary_expenses = input("How much do you spend on non-necessary things? (Q for 5-20%, W for 15-30%, E for 25-40%): ")
    if discretionary_expenses == "q" or discretionary_expenses == "Q":
        discretionary_percentage = random.uniform(0.05, 0.20)
    else:
        discretionary_percentage = random.uniform(0.15, 0.40)

    time_periods = list(range(12, 241, 12))

    savings_data = []

    for months in time_periods:
        total_expenses = 0
        total_income = 0

        for month in range(1, months + 1):
            tax_rate = calculate_taxes(annual_salary) / 12
            net_income = annual_salary / 12 - tax_rate
            total_income += net_income

            monthly_expenses = monthly_rent + necessary_expenses + insurance
            monthly_expenses += net_income * discretionary_percentage
            total_expenses += monthly_expenses

            if month % 12 == 0:
                inflation_rate = random.uniform(0.02, 0.05)
                deflation_chance = random.uniform(0, 1)
                if deflation_chance < 0.05:
                    inflation_rate = -random.uniform(0.01, 0.05)

                annual_salary *= (1 + inflation_rate)

                # Separate inflation and deflation calculations for expenses
                inflation_rate_expenses = random.uniform(0.02, 0.05)
                deflation_chance_expenses = random.uniform(0, 1)
                if deflation_chance_expenses < 0.05:
                    inflation_rate_expenses = -random.uniform(0.01, 0.05)

                monthly_rent *= (1 + inflation_rate_expenses)
                necessary_expenses *= (1 + inflation_rate_expenses)
                insurance *= (1 + inflation_rate_expenses)

                if months <= 120:  # Avoid crisis after the 10th year
                    crisis_chance = random.uniform(0, 1)
                    if crisis_chance < 0.2:
                        annual_salary *= (1 - random.uniform(0.2, 0.4))

        savings = total_income * months / 12 - total_expenses
        savings_data.append(savings)

        if months == 12:
            time_period_label = "1 Month"
        elif months == 72:
            time_period_label = "6 Months"
        else:
            time_period_label = f"{months // 12} Years"

        print(f"{time_period_label} Summary:")
        print(f"Total Income: {format_number(total_income * months / 12)}")
        print(f"Total Expenses: {format_number(total_expenses)}")
        print(f"Total Savings: {format_number(savings)}\n")

    plt.plot([x // 12 for x in time_periods], savings_data, marker='o')
    plt.xlabel('Time Period (Years)')
    plt.ylabel('Total Savings')
    plt.title('Total Savings Over Time')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
