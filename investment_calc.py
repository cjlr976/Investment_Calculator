'''
Chloe Robinson and Camila Fienco
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

import sys

'''
Purpose: Recursively calculate final investment after n years
Parameters:
    - principle: Initial amount invested
    - rate: Annual interest rate
    - contrib_a: Annual contribution
    - years: Number of years to calculate for
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


'''
Purpose: Calculate return on investment (ROI) as a percentage
Parameters:
    - total_invested: Sum of initial principle and all contributions
    - final_val: Final amount after n years
'''
def roi(total_invested, final_val):
    if total_invested == 0:
        raise ValueError("Total invested cannot be zero.")
    
    gain = final_val - total_invested
    return (gain / total_invested) * 100


# Purpose: Calculates total profit
def profit(total_invested, final_val):
    return final_val - total_invested

#Purpose: Main function to read input, perform calculations, and write output
def main():
    lines = [line.strip() for line in sys.stdin if line.strip()]

    # Expecting exactly 4 lines of numeric input
    if len(lines) < 4:
        raise ValueError("Input file must contain 4 lines: principle, rate, contribution, years.")

    principle = float(lines[0])
    annual_rate = float(lines[1])
    annual_contrib = float(lines[2])
    total_years = int(lines[3])

    # Recursive final value
    final_amount = investment(principle, annual_rate, annual_contrib, total_years)

    # Total invested = principal + contributions
    total_invested = principle + (annual_contrib * total_years)

    # Profit and ROI
    total_profit = profit(total_invested, final_amount)
    roi_percent = roi(total_invested, final_amount)

    # Write to output file
    with open("output.txt", "w") as f:
        f.write(f"Final Amount: ${final_amount:.2f}\n")
        f.write(f"Total Invested: ${total_invested:.2f}\n")
        f.write(f"Final Profit: ${total_profit:.2f}\n")
        f.write(f"ROI Percentage: {roi_percent:.2f}%\n")


if __name__ == "__main__":
    main()