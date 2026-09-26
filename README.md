# ATM Simulation

A simple **ATM Simulation project in Python** created as a beginner-friendly programming project.

The program allows a user to create a 4-digit PIN, log in to the account, and perform basic ATM operations such as depositing money, withdrawing money, checking the balance, and viewing transaction history.

## Features

- Account name input
- 4-digit PIN creation
- PIN validation
- Login system with 3 attempts
- Account lock after incorrect login attempts
- Account data saved in `account_data.json`
- Existing account data loaded when available
- Deposit money
- Withdraw money
- Check account balance
- View transaction history
- Exit and save account information

## Technologies Used

- Python 3
- `json`
- `os`
- `datetime`

These modules are used for data storage, file checking, and transaction timestamps.

## How to Run

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code or a terminal.
4. Run:

```bash
python atm_project_single_file.py
```

If your system uses the Python launcher, you can also use:

```bash
py atm_project_single_file.py
```

## How It Works

### 1. Account Setup

The program asks the user to enter an account name and create a 4-digit PIN.

### 2. Login

The user enters the PIN to log in.

There are three login attempts. If all attempts are incorrect, the account is locked and the program exits.

### 3. Account Data

The program checks whether `account_data.json` exists.

- If it exists, the saved balance and transaction history are loaded.
- If it does not exist, the program starts with the initial values defined in the code.

### 4. ATM Menu

After login, the user gets five options:

```text
1. DEPOSIT
2. WITHDRAW
3. BALANCE
4. HISTORY
5. EXIT
```

### 5. Deposit

The user enters an amount to deposit. A successful deposit updates the balance and adds the transaction to the history.

### 6. Withdraw

The user enters an amount to withdraw.

The program checks that:

- The amount is greater than zero.
- The amount does not exceed the available balance.

### 7. Balance

The current account holder name and balance are displayed.

### 8. Transaction History

The account holder name and stored transaction history are displayed.

### 9. Exit

When the user selects Exit, the account name, balance, and transaction history are saved to:

```text
account_data.json
```

## Project Structure

```text
ATM-Simulation/
│
├── atm_project_single_file.py
├── account_data.json
├── README.md
└── STATEMENT.md
```

`account_data.json` is created/updated by the program when the user exits through the ATM menu.

## Important Note

This is an **educational ATM simulation**, not a real banking application. It does not connect to a real bank, payment system, or financial account.

## Learning Objectives

This project demonstrates practical use of:

- Variables
- `input()` and `print()`
- `if/elif/else`
- `while` loops
- Functions and program structure
- Lists and dictionaries
- JSON file handling
- File existence checking
- Date and time handling
- Basic input validation
- Simple authentication logic

## Future Improvements

Possible future improvements include:

- Multiple user accounts
- Better PIN security
- Transfer functionality
- More detailed transaction records
- Separate classes for accounts and transactions
- A graphical user interface
- Database-based storage

## Author

Created as a Python programming project.
## Repository link
https://github.com/tarushsinha842-sys/ATM-Simulation-Python
