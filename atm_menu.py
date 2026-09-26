"""ATM menu and transaction operations."""

import datetime
import json


def run_menu(name: str, balance: float, history: list) -> None:
    while True:
        print("\n" + "=" * 29)
        print("    ATM  SIMULATION")
        print("=" * 29)
        print("1. DEPOSIT")
        print("2. WITHDRAW")
        print("3. BALANCE")
        print("4. HISTORY")
        print("5. EXIT")
        choice = input("choose an option: ")

        # DEPOSIT
        if choice == "1":
            amount = input("ENTER THE AMOUNT YOU WANT TO DEPOSIT:")
            if amount.isdigit():
                amount = int(amount)
                if amount > 0:
                    balance += amount
                    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                    history.append(
                        f"deposited {amount} on {now} | balance: {balance}"
                    )
                    print(f"{amount} DEPOSITED SUCCESSFULLY!")
                    print(f"NEW BALANCE: {balance}")
                else:
                    print("AMOUNT MUST BE GREATER THAN ZERO.")
            else:
                print("invalid amount!")

        elif choice == "2":
            amount = input("ENTER THE AMOUNT YOU WANT TO WITHDRAW: ")
            if amount.isdigit():
                amount = int(amount)
                if amount <= 0:
                    print("AMOUNT MUST BE GREATER THAN ZERO ")
                elif amount > balance:
                    print("INSUFFICIENT BANK BALANCE")
                else:
                    balance -= amount
                    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                    history.append(
                        f"Withdraw {amount} on {now} | balance: {balance}"
                    )
                    print(f"{amount} WITHDRAW SUCCESSFULLY!")
                    print(f"NEW BALANCE : {balance}")
            else:
                print("INVALID AMOUNT")

        elif choice == "3":
            print("\n---- ACCOUNT DETAIL ----")
            print("Account Holder:", name)
            print("BALANCE         :", balance)

        elif choice == "4":
            print("\n---- TRANSACTION HISTORY ----")
            print("Account Holder:", name)
            print("HISTORY         :", history)

        elif choice == "5":
            data = {"name": name, "balance": balance, "history": history}
            with open("account_data.json", "w") as f:
                json.dump(data, f, indent=4)
            print("\n THANK YOU FOR BANKING WITH US! ")
            print(" HAVE A GREAT DAY! ")
            break

        else:
            print("INVALID CHOICE! PLS SELECT A VALID OPTION ")
