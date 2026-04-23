from datetime import datetime

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

print(get_date_input("enter date").strftime("%d-%m-%Y"))
