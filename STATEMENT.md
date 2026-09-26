# Project Statement

## Project Title

**ATM Simulation using Python**

## Problem Statement

The purpose of this project is to create a simple ATM simulation program using Python.

The program provides a basic banking-style interface where a user can create a 4-digit PIN, log in to an account, and perform common ATM operations. The program also stores account information and transaction history so that the saved data can be loaded when the program is run again.

## Objectives

The main objectives of this project are:

1. To create a simple PIN-based login system.
2. To provide basic ATM operations through a menu-driven interface.
3. To allow deposits and withdrawals.
4. To display the current account balance.
5. To maintain transaction history.
6. To save account information using a JSON file.
7. To practice Python programming concepts such as loops, conditions, lists, dictionaries, functions, file handling, and modules.

## Scope

The project covers the following operations:

- Account name input
- PIN creation and validation
- Login authentication
- Three login attempts
- Deposit
- Withdrawal
- Balance checking
- Transaction history
- Saving and loading account data

The project is intended for educational purposes and demonstrates the basic logic behind an ATM-style application.

## Working Principle

The program first asks the user for an account name and a 4-digit PIN.

After the PIN is created, the user is asked to log in. The program allows three attempts to enter the correct PIN. If the user enters the correct PIN, the main ATM menu is displayed.

The user can then select an operation:

- Deposit money
- Withdraw money
- Check balance
- View transaction history
- Exit the program

When the user exits, the current account information is stored in a JSON file. When the program is run again, the saved information can be loaded from that file.

## Technologies

The project is developed using **Python** and uses:

- `json` for storing account information
- `os` for checking whether the account data file exists
- `datetime` for recording transaction date and time

## Expected Outcome

The expected outcome is a working command-line ATM simulation that allows the user to authenticate and perform basic account operations while maintaining saved account information and transaction history.

## Educational Purpose

This project is designed to strengthen fundamental Python programming skills through a practical application. It demonstrates how multiple programming concepts can be combined to create a functional command-line application.

## Limitations

This project is a simulation and is not intended for real financial transactions. It does not provide real banking services or connect to any real bank account.

## Conclusion

The ATM Simulation demonstrates how Python can be used to build a simple menu-driven application with authentication, transaction processing, and file-based data storage. It provides a foundation for learning more advanced concepts such as object-oriented programming, databases, graphical interfaces, and secure authentication.
