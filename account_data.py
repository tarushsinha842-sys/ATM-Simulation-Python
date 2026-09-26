"""Load account information from account_data.json."""

import json
import os


def load_account():
    if os.path.exists("account_data.json"):
        with open("account_data.json", "r") as f:
            saved_data = json.load(f)
            balance = saved_data["balance"]
            history = saved_data["history"]
            print(
                f"\nWelcome back, {saved_data['name']}! "
                "Your saved data has been loaded."
            )
    else:
        balance = 50000000.0
        history = [3000000]

    return balance, history
