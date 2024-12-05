# Margin Trading Facility (MTF) Calculator

def calculate_mtf_profit_or_loss(
    purchase_value, margin_contribution, stock_change_percent, holding_period_days, interest_rate_annual
):
    # Calculate borrowed amount
    borrowed_amount = purchase_value - margin_contribution
    
    # Calculate new stock value after change
    stock_value_after_change = purchase_value * (1 + stock_change_percent / 100)
    
    # Calculate interest on borrowed amount
    interest = (borrowed_amount * interest_rate_annual * holding_period_days) / (100 * 365)
    
    # Total repayable amount to Zerodha
    total_repayable = borrowed_amount + interest
    
    # Remaining value after repaying Zerodha
    remaining_value = stock_value_after_change - total_repayable
    
    # Net profit or loss
    profit_or_loss = remaining_value - margin_contribution
    
    return {
        "Borrowed Amount": borrowed_amount,
        "Stock Value After Change": stock_value_after_change,
        "Interest Charged": interest,
        "Total Repayable to Zerodha": total_repayable,
        "Remaining Value": remaining_value,
        "Net Profit or Loss": profit_or_loss,
    }


# Take user inputs
try:
    purchase_value = float(input("Enter the total purchase value (₹): "))
    margin_contribution = float(input("Enter your contribution (₹): "))
    stock_change_percent = float(input("Enter the percentage change in stock price (%): "))
    holding_period_days = int(input("Enter the holding period (days): "))
    interest_rate_annual = float(input("Enter the annual interest rate (%): "))
    
    # Validate inputs
    if margin_contribution > purchase_value:
        print("Error: Your contribution cannot exceed the total purchase value.")
    else:
        # Calculate results
        results = calculate_mtf_profit_or_loss(
            purchase_value, margin_contribution, stock_change_percent, holding_period_days, interest_rate_annual
        )
        
        # Print results
        print("\nMargin Trading Facility (MTF) Calculation:")
        for key, value in results.items():
            print(f"{key}: ₹{value:,.2f}")

except ValueError:
    print("Error: Please enter valid numeric values.")
