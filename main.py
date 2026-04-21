print("Folio-Sync Initialised")
"""Classes that will be needed: 
User:           (when multiple users are there)
Asset:          (along with child classes such as Stock,ETF,MutualFund etc)
Portfolio:      (To act as vault to store and show the assets and net worth)
"""

class User:
    """User class will be used to give user operations like profile and all once the fundamental logic is developed.
    This class will be functional in later time."""
    pass

class Asset:
    """Asset is the parent class for all different types of Child instrument classes, 
    it stores the basic info like asset_name and capital invested."""
    
    def __init__(self,asset_name,investment):
        self.asset_name = asset_name
        self.investment = investment
        
class Stock(Asset):
    pass

def prompt_stock():
    """Asks the User for detail input of the Stock to be added in Portfolio."""
    ticker = input("Enter TICKER: ").upper()
    quantity = get_number_input("Enter Quantity: ")
    price = get_number_input("Enter Price: ")

class Portfolio:
    pass


def get_number_input(prompt:str,low=0):
    while True:
        try:
            number = (input(prompt))
            if not number.strip():
                print("Error: Input cannot be empty.")
                continue
            number = float(number)  
            if number<low:
                print(f"Error: The number should be greather than {low}.")
                continue
            return number
        
        except ValueError:
            print("Error: Please enter a valid number.")


def main():
    vault = Portfolio()
    
    while True:
        print("1. Log a new Investment/Trade")
        print("2. View my Portfolio")
        print("3. Show overall Profit or Loss")
        print("4. Exit")

        choice = get_number_input("\nWhat would you like to do? (1/2/3/4): ")
        if choice == 1:
            print("Asset Types:")
            print("1. Stocks")
            print("2. ETFs")
            print("3. Mutual Fund")
            print("4. Cryptocurrency")
            print("5. Fixed Deposit (FD)")
            print("6. Recurring Deposit (RD)")
            print("7. Bonds/SGBs")
            print("8. Cash Balance")

            asset_type = get_number_input("Select an Asset Type (1 - 8): ")
            if (asset_type) == 1:
                prompt_stock()
        if choice == 4:
            print("Folio_Sync Closed!")
            break
                
                
                
                
                
if __name__ == "__main__":
    main()