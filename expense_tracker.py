# an app that shows a console base menu 
# with options for deposit, withdraw and list transtactions

transactions = []
balance = 0

def reset_data():
    global transactions
    global balance
    transactions = []
    balance = 0

def deposit(amount):
    global balance
    balance += amount
    transactions.append(('deposit', amount))
    return balance

def withdraw(amount):
    global balance
    if balance >= amount:
        balance -= amount
        transactions.append(('withdrawal', amount))
        return balance
    else:
        return "Insufficient funds"

def check_balance():
    return balance

def list_transactions():
    return transactions

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
            amount = float(input("Enter deposit amount: "))
            deposit(amount)
            print("Deposited", amount)

        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))
            withdraw(amount)
            print("Withdrawn", amount)

        elif choice == '3':
            print("Current Balance:", check_balance())

        elif choice == '4':
            print("Transaction History:")
            list_transactions()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


