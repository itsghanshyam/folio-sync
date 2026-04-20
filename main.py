print("Folio-Sync Initialised")
"""Classes that will be needed: 
User
Trade
Instrument"""

class Trade:
    """Will have a functions like buy/sell then attributes like quantityy,price,name or ticker , date of adding , nav date and type of instrument"""
    def __init__(self):#date,
        instruments = ["Stock","ETF","Mutual Fund","Crypto","Bond","FD","RD"]
        types = f"1. {instruments[0]}\n2. {instruments[1]}\n3. {instruments[2]}\n4. {instruments[3]}\n5. {instruments[4]}\n6. {instruments[5]}\n7. {instruments[6]}\n"
        instrument_type = int(input(f"Select Instrument type (only number):\n{types}"))
        self.instrument = instruments[instrument_type - 1]
        self.type_of_trade = input("Which type of trade is this (Buy B/b) or (Sell S/s)").lower()
class User:
    pass
class Instrument:
    pass
    

obj = Trade()
