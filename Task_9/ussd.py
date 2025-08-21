# This is a simulation of a ussd service
# Thought process
# 1. The ussd is going to handle balance checking, buying airtime and registration
# 2. user will need to register before using the service: The user dictionary will look like this {"name": "user name", "password": "1234"}
# 3. user will need to dial *419# to get started

ussd_code = "*419#"

enter_code = input("Dial *419# to get started: ")

amount = 0


while enter_code != ussd_code:
    print("You entered a wrong code")
    enter_code = input("Dial *419# to get started: ")

user_data = {}

print("You will need to register first\n")

user_data["name"] = input("Enter your name: ")
user_data["password"] = input("Set your password: ")
user_data["account_balance"] = 5000
confirm_password = input("Confirm your password: ")

while confirm_password != user_data["password"]:
    confirm_password = input("Password does not match, please try again: ")
    

print(f"you have been given {user_data['account_balance']} Naira as welcome balance.\n")


    
print("Select a service: \n1. Check Balance\n2. Buy Airtime\n3. Exit\n")

user_input = input("Enter 1,2 or 3: ")

print('\n')

while user_input != '3':
    if user_input == '1':
        password = input("Enter your password: ")
        while password != user_data["password"]:
            password = input("Wrong password, try again: ")

        print(f"Your balance is {user_data['account_balance']}\n")
        print("Select a service: \n1. Check Balance\n2. Buy Airtime\n3. Exit\n")
        user_input = input("Enter 1,2 or 3: ")
    elif user_input == '2':
        password = input("Enter your password: ")
        while password != user_data["password"]:
            password = input("Wrong password, try again: ")

        phone_number = input("Emter the phone number: ")
        try:
            amount = int(input("Enter amount: "))
        except ValueError:
            print("The value you entered is invalid try again\n")
        print('\n')
        if amount != 0:
            while amount > user_data["account_balance"]:
                print("Sorry you do not have enough fund for this transaction: ")
                amount = int(input("Enter amount: "))
            user_data["account_balance"] -= amount
            print(f"{amount} Naira airtime has been added to {phone_number} and your balance is {user_data["account_balance"]}\n")
            
        print("Select a service: \n1. Check Balance\n2. Buy Airtime\n3. Exit\n")
        user_input = input("Enter 1,2 or 3: ")

print(f"Thank you for using our service {user_data["name"]}")