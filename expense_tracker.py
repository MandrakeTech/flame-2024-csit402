# an app that shows a console base menu 
# with options for deposit, withdraw and list transtactions

from dataclasses import dataclass

@dataclass
class UserData:
    name: str
    transactions: list
    balance: int

# create a dictionary that contains transactions and balance against each user name
bankData: dict[str, UserData] = {}

def getUserData(name) -> UserData:
    if name not in bankData:
        bankData[name] = UserData(name, [], 0)
    return bankData[name]

def deposit(name, amount):
    userData = getUserData(name)
    userData.balance += amount
    userData.transactions.append(('deposit', amount))

    return userData.balance

def withdraw(name, amount):
    userData = getUserData(name)

    if userData.balance >= amount:
        userData.balance -= amount
        userData.transactions.append(('withdrawal', amount))
        return userData.balance
    else:
        return "Insufficient funds"

def check_balance(name):
    return getUserData(name).balance

def list_transactions(name):
    return getUserData(name).transactions

