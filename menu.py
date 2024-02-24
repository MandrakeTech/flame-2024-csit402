

from deposit_client_api import deposit
from passbook_client_api import check_balance, list_transactions
from withdraw_client_api import withdraw


def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. List Transactions")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter account holder name: ")
            amount = int(input("Enter deposit amount: "))
            deposit(name, amount)
            print("Deposited", amount)

        elif choice == '2':
            name = input("Enter account holder name: ")
            amount = int(input("Enter withdrawal amount: "))
            balance = withdraw(name, amount)
            if balance != "Insufficient funds":
              print("Withdrawn", amount)

        elif choice == '3':
            name = input("Enter account holder name: ")
            print("Current Balance:", check_balance(name))

        elif choice == '4':
            name = input("Enter account holder name: ")
            transactions = list_transactions(name)
            print(f"Transaction History:{transactions}")
            
        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


