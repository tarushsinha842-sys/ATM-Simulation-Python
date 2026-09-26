import json
import os
import datetime

name=input("Enter your account name: ")

#PIN Creation 
while True:
    pin=input("Set a 4-digit PIN: ")
    if pin.isdigit() and len(pin) ==4:
        break 
    else:
        print("Invalid PIN. PIN must be  exactly 4 digit. \n")

# Login system 

attempts=3
while attempts >0:
    entered_pin=input(" ENTER PIN TO LOGIN: ")

    if entered_pin==pin:
        print("\nLogin Successful !")
        break
    else:
        attempts -=1
        if attempts>0:
            print(f"Incorrect PIN. Attempts left: {attempts} ")
        else:
            print("Account Locked ! Too many incorrect attempts ")
            exit()

# ACCOUNT DATA
if os.path.exists("account_data.json"):
    with open("account_data.json", "r") as f:
        saved_data=json.load(f)
        BALANCE=saved_data["balance"]
        HISTORY=saved_data["history"]
        print(f"\nWelcome back, {saved_data['name']}! Your saved data has been loaded.")
else:
    BALANCE=50000000.0
    HISTORY=[3000000]

# MAIN MENU 
while True:
    print("\n"+"="*29)
    print("    ATM  SIMULATION")
    print("="*29)
    print("1. DEPOSIT")
    print("2. WITHDRAW")
    print("3. BALANCE")
    print("4. HISTORY")
    print("5. EXIT")
    choice=input("choose an option: ")

    #DIPOSIT
    if choice=="1":
        amount=input("ENTER THE AMOUNT YOU WANT TO DEPOSIT:")
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                BALANCE+=amount
                now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                HISTORY.append(f"deposited {amount} on {now} | balance: {BALANCE}")

                print(f"{amount} DEPOSITED SUCCESSFULLY!")
                print(f"NEW BALANCE: {BALANCE}")

            else:
                print("AMOUNT MUST BE GREATER THAN ZERO.")
        else:
            print("invalid amount!")


    elif choice =="2":
        amount=input("ENTER THE AMOUNT YOU WANT TO WITHDRAW: ")

        if amount.isdigit():
            amount=int(amount)

            if amount <= 0:
                print("AMOUNT MUST BE GREATER THAN ZERO ")

            elif amount>BALANCE:
                print("INSUFFICIENT BANK BALANCE")
            else:
                BALANCE-=amount 
                now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                HISTORY.append(f"Withdraw {amount} on {now} | balance: {BALANCE}")

                print(f"{amount} WITHDRAW SUCCESSFULLY!")
                print(f"NEW BALANCE : {BALANCE}")

        else:
            print("INVALID AMOUNT")  

    elif choice =="3":

        print("\n---- ACCOUNT DETAIL ----")
        print("Account Holder:", name)
        print("BALANCE         :", BALANCE)

    elif choice =="4":

        print("\n---- TRANSACTION HISTORY ----")
        print("Account Holder:",name)
        print("HISTORY         :", HISTORY)

    elif choice =="5":

        data={"name": name, "balance": BALANCE, "history": HISTORY}
        with open("account_data.json", "w") as f:
            json.dump(data, f, indent=4)

        print("\n THANK YOU FOR BANKING WITH US! ")
        print(" HAVE A GREAT DAY! ")
        break

    else:
        print("INVALID CHOICE! PLS SELECT A VALID OPTION ")