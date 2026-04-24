from datetime import datetime
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
banks = ["SBI Bank","HDFC Bank","ICICI Bank","Axis Bank","Post Office","Other"]
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
        choice = input("Enter bank: ")
        return choice
print(get_bank_input("Choose a bank: ",banks))
    


