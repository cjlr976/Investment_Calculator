'''Chloe Robinson and Camila Fienco
COT 4400 Analysis of Algorithms
22 February 2026
'''

'''
Purpose: Recursively calculates final investment value
Base case: 
    If years == 0, return initial principle
Recursive case:
    V(n) = (V(n-1) + contribution) * (1 + rate)
'''
def investment(principle, rate, contrib_a, years):
    # Valid input
    if years < 0:
        raise ValueError("Years cannot be negative.")

    # Base case
    if years == 0:
        return principle
    
    # Recursive case
    prev_val = investment(principle, rate, contrib_a, years - 1)
    cur_val = (prev_val + contrib_a) * (1 + rate)
    return cur_val


# Purpose: Calculate return on investment as a percentage
def roi(total_invested, final_val):
    if total_invested == 0:
        raise ValueError("Total invested cannot be zero.")
    
    gain = final_val - total_invested
    return (gain / total_invested) * 100


# Purpose: Calculates total profit
def profit(total_invested, final_val):
    return final_val - total_invested


def main():
    principle = float(input("Initial Investment: "))
    annual_rate = float(input("Annual Rate (decimal): "))
    annual_contrib = float(input("Annual Contributions: "))
    total_years = int(input("Number of Years: "))

    # Recursive final value
    final_amount = investment(principle, annual_rate, annual_contrib, total_years)

    # Total invested = principal + contributions
    total_invested = principle + (annual_contrib * total_years)

    # Profit and ROI
    total_profit = profit(total_invested, final_amount)
    roi_percent = roi(total_invested, final_amount)

    #Write to output file
    with open("roi_output.txt", "w") as f:
        f.write(f"Final Amount: ${final_amount:.2f}\n")
        f.write(f"Total Invested: ${total_invested:.2f}\n")
        f.write(f"Final Profit: ${total_profit:.2f}\n")
        f.write(f"ROI Percentage: {roi_percent:.2f}%\n")

if __name__ == "__main__":
    main()