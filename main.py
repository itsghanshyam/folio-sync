from datetime import datetime
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
    
    def __init__(self,asset_name,investment,purchase_date):
        self.asset_name = asset_name
        self.investment = investment
        self.purchase_date = purchase_date

class Stock(Asset):
    def __init__(self,ticker,quantity,price,purchase_date):
        self.ticker = ticker
        self.quantity = quantity
        self.price = price
        super().__init__(ticker,quantity*price,purchase_date)
        
class ETF(Asset):
    def __init__(self,ticker,quantity,price,purchase_date):
        self.ticker = ticker
        self.quantity = quantity
        self.price = price
        super().__init__(ticker,quantity*price,purchase_date)

class MutualFund(Asset):
    def __init__(self,scheme_name,nav_date,nav,investment,units):
        self.scheme_name = scheme_name
        self.nav = nav
        self.units = units
        super().__init__(scheme_name,investment,nav_date)
        
class Crypto(Asset):
    def __init__(self,ticker,quantity,price,purchase_date):
        self.ticker = ticker
        self.quantity = quantity
        self.price = price
        super().__init__(ticker,quantity*price,purchase_date)

class FD(Asset):
    def __init__(self,name,bank_name,investment,interest_rate,investment_date,tenure_days):
        self.name = name
        self.bank_name = bank_name
        self.interest_rate = interest_rate
        self.tenure_days = tenure_days # TODO: Upgrade to accurate calendar shift logic
        super().__init__(f"{name} ({bank_name})",investment,investment_date)
         
class RD(Asset):
    pass

class Portfolio:
    """The Portfolio Class holds the different Asset objects the User has invested in and does the operation on them like 
    viewing the portfolio"""
    def __init__(self):
        self.portfolio = []
    def add_to_folio(self,item):
        self.portfolio.append(item)
    def view_portfolio(self):
        result = "\n"
        for asset in self.portfolio:
            result += (f"Asset: {asset.asset_name}  | Total Investment: \n")
        return result
    
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
            
def get_date_input(prompt: str):
    while True:
        date = input(prompt).strip()
        try:
            if not date:
                print("Date cannot be empty.")
                continue
            date = datetime.strptime(date,"%d-%m-%Y").date()
            return date
        except ValueError:
            print("Error: Invalid date format, Please Enter in DD-MM-YYYY format.")
        
def get_bank_input(prompt: str,banks):
    print("Available Banks: ")
    for index,bank_name in enumerate(banks,1):
        print(f"{index}. {bank_name}")
    choice = get_number_input(prompt)
    if choice == 1:
        return banks[0].strip().upper()
    elif choice == 2:
        return banks[1].strip().upper()
    elif choice == 3:
        return banks[2].strip().upper()
    elif choice == 4:
        return banks[3].strip().upper()
    elif choice == 5:
        return banks[4].strip().upper()
    else:
        choice = input("Enter Bank Name: ").strip().upper()
        return choice
    
def get_duration_days(prompt):
    print(prompt)
    years = get_number_input("Enter Tenure (Years): ")
    months = get_number_input("Enter Tenure (Months): ")
    days = get_number_input("Enter Tenure (Days): ")
    tenure_days = (years*365) + (months*30) + days # TODO: Upgrade to accurate calendar shift logic
    return tenure_days 

def prompt_stock():
    """Prompts the User for detail input of the Stock to be added in Portfolio."""
    ticker = input("Enter TICKER: ").upper()
    quantity = get_number_input("Enter Quantity: ")
    price = get_number_input("Enter Price: ")
    purchase_date = get_date_input("Purchasing Date (DD-MM-YYYY): ")
    return Stock(ticker,quantity,price,purchase_date)
    
def prompt_etf():
    """Prompts the User for detail input of the ETF (Exchange Traded Fund) to be added in Portfolio."""
    ticker = input("Enter TICKER: ").upper().strip()
    quantity = get_number_input("Enter Quantity: ")
    price = get_number_input("Enter Price: ")
    purchase_date = get_date_input("Purchasing Date (DD-MM-YYYY): ")
    return ETF(ticker,quantity,price,purchase_date)

def prompt_mf():
    """Prompts the User for detail input of the Mutual Fund to be added in Portfolio."""
    scheme_name = input("Enter Scheme Name: ").strip().upper()
    nav_date = get_date_input("NAV Date (DD-MM-YYYY): ")
    nav = get_number_input("Purchase NAV: ")
    while True:
        print("How would you like to Enter your holdings?\n")
        print("1. Enter Total Purchase Amount")
        print("2. Enter Number of Units bought\n")
        choice = get_number_input("Choose an option: ")
        if choice == 1:
            investment = get_number_input("Purchase Amount: ")
            units = (investment/nav)
            break
        elif choice == 2:
            units = get_number_input("Number of Units: ")
            investment = (units*nav)
            break
        else:
            print("Choose a valid option: ")
    return MutualFund(scheme_name,nav_date,nav,investment,units)

def prompt_crypto():
    """Prompts the User for detail input of the Cryptocurrency to be added in Portfolio."""
    ticker = input("Enter coin TICKER: ").upper()
    quantity = get_number_input("Enter Quantity: ")
    price = get_number_input("Enter Price: ")
    purchase_date = get_date_input("Purchasing Date (DD-MM-YYYY): ")
    return Crypto(ticker,quantity,price,purchase_date)

def prompt_fd():
    """Prompts the User for detail input of the Fixed Deposit to be added in Portfolio."""
    banks = ["SBI Bank","HDFC Bank","ICICI Bank","Axis Bank","Post Office","Other"]
    name = input("Name for FD: ").upper()
    bank_name = get_bank_input("Choose the Bank for FD:",banks)
    investment = get_number_input("Investment Amount: ")
    interest_rate = get_number_input("Intereset Rate: ")
    investment_date = get_date_input("Date of Investment (DD-MM-YYYY): ") # TODO: Need to add tenure
    tenure_days = get_duration_days("Tenure for Fixed Deposit (FD)")
    return FD(name,bank_name,investment,interest_rate,investment_date,tenure_days)
    

def prompt_rd():
    """Prompts the User for detail input of the Recurring Deposit to be added in Portfolio."""
    pass

def prompt_bond():
    """Prompts the User for detail input of the Bond/SGB to be added in Portfolio."""
    pass

def prompt_cash():
    """Prompts the User for detail input of the Cash Balance to be added in Portfolio."""
    pass


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
            
            if (asset_type) == 1:           #TODO: Add a confirmation message before adding.
                new_stock = prompt_stock()      #TODO: Add an option to cancel adding the asset and go back.
                vault.add_to_folio(new_stock)
                print(f"The stock {new_stock.asset_name} is added to the portfolio.")
                
            elif (asset_type) == 2:
                new_etf = prompt_etf()
                vault.add_to_folio(new_etf)
                print(f"The ETF {new_etf.asset_name} is added to the portfolio.")
                
            elif (asset_type) == 3:
                new_mf = prompt_mf()
                vault.add_to_folio(new_mf)
                print(f"The Mutual Fund Scheme {new_mf.asset_name} is added to the portfolio.")
                
            elif (asset_type) == 4:
                new_crypto = prompt_crypto()
                vault.add_to_folio(new_crypto)
                print(f"The Crypto Coin {new_crypto.asset_name} is added to the portfolio.")
            
            elif (asset_type) == 5:
                new_fd = prompt_fd()
                vault.add_to_folio(new_fd)
                print(f"The Fixed deposit {new_fd.asset_name} is added to the portfolio.")
                
            elif (asset_type) == 6:
                prompt_rd()
            elif (asset_type) == 7:
                prompt_bond()
            elif (asset_type) == 8:
                prompt_cash()
            else:
                print("Error: Select Valid option.")
                continue
        elif choice == 2:
            print(vault.view_portfolio())
        elif choice == 4:
            print("Folio_Sync Closed!")
            break
        else:
            print("Error: Select Valid option.")
            continue
            
                       
if __name__ == "__main__":
    main()