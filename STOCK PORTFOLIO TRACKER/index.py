# Simple Stock Tracker - Properly Indented Version

# Dictionary of stock prices
stock_prices = {
    "AAPL": 180.50,
    "TSLA": 250.75,
    "MSFT": 320.20,
    "GOOGL": 135.40,
    "AMZN": 150.60
}

def get_user_portfolio():
    portfolio = {}
    while True:
        print("\nAvailable stocks:", ", ".join(stock_prices.keys()))
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        
        if stock == 'DONE':
            break
            
        if stock not in stock_prices:
            print("Error: Invalid stock symbol. Please try again.")
            continue
            
        try:
            quantity = float(input(f"Enter quantity of {stock}: "))
            if quantity <= 0:
                print("Error: Quantity must be positive.")
                continue
            portfolio[stock] = quantity
        except ValueError:
            print("Error: Please enter a valid number.")
            
    return portfolio

def display_results(portfolio):
    if not portfolio:
        print("\nNo stocks entered. Exiting.")
        return
        
    print("\nInvestment Summary:")
    print("-" * 30)
    total = 0
    
    for stock, quantity in portfolio.items():
        value = quantity * stock_prices[stock]
        print(f"{stock}:")
        print(f"  Quantity: {quantity}")
        print(f"  Price: ${stock_prices[stock]:.2f}")
        print(f"  Value: ${value:.2f}")
        print("-" * 30)
        total += value
        
    print(f"TOTAL PORTFOLIO VALUE: ${total:.2f}")

def offer_file_save(portfolio):
    if not portfolio:
        return
        
    choice = input("\nWould you like to save these results? (y/n): ").lower()
    if choice == 'y':
        filename = input("Enter filename (without extension): ").strip()
        if not filename:
            filename = "portfolio_results"
            
        try:
            with open(f"{filename}.txt", "w") as file:
                file.write("PORTFOLIO SUMMARY\n")
                file.write("=" * 30 + "\n")
                
                total = 0
                for stock, quantity in portfolio.items():
                    value = quantity * stock_prices[stock]
                    file.write(f"{stock}:\n")
                    file.write(f"  Quantity: {quantity}\n")
                    file.write(f"  Price: ${stock_prices[stock]:.2f}\n")
                    file.write(f"  Value: ${value:.2f}\n")
                    file.write("-" * 30 + "\n")
                    total += value
                    
                file.write(f"TOTAL VALUE: ${total:.2f}\n")
                
            print(f"Results saved to {filename}.txt")
        except Exception as e:
            print(f"Error saving file: {e}")

def main():
    print("Welcome to Simple Stock Tracker")
    portfolio = get_user_portfolio()
    display_results(portfolio)
    offer_file_save(portfolio)

if __name__ == "__main__":
    main()