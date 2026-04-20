print("Folio-Sync Initialised")
"""Classes that will be needed: 
User
Trade
Portfolio
"""

class Trade:
    """Will have a functions like buy/sell then attributes like quantityy,price,name or ticker , date of adding , nav date and type of instrument"""
    def __init__(self):
        pass
class User:
    pass

class Portfolio:
    pass


def get_number_input():
    pass


def main():
    vault = Portfolio()
    
    while True:
        print("1. Log a new Trade/Investment")
        print("2. View my Portfolio")
        print("3. Show overall Profit or Loss")
        print("4. Exit")

        try:
            choice = int(input("What would you like to do?"))
            if choice < 1 or choice > 4:                        #In futrue we will increase options then we will make range as automatic
                print("Error: Enter an option in the range")
                continue
        except TypeError or ValueError:
            print("Error: Enter a valid option number.")
            
            if choice == 1:
                ticker = input("TICKER: ").upper()
                quantity = float(input("Quantity: "))
                
                
                


