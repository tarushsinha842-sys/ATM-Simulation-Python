import json 
import datetime
import os


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
exec(open("account_data.py").read())

# MAIN MENU
exec(open("atm_menu.py").read())
