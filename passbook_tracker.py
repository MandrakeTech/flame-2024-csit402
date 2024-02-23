# an app that shows a console base menu 
# with options for deposit, withdraw and list transtactions

from dataclasses import dataclass
from deposit_client_api import check_balance as check_deposit_balance, list_transactions as list_deposit_transactions
from withdraw_client_api import check_balance as check_withdrawal_balance, list_transactions as list_withdraw_transactions

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

def check_balance(name: str):
    deposit_balance = check_deposit_balance(name)
    if isinstance(deposit_balance, int):
        withdrawal_balance = check_withdrawal_balance(name)
        if isinstance(withdrawal_balance, int):
            return deposit_balance - withdrawal_balance
    return "error while retreiving balance"

def list_transactions(name: str):
    deposit_transactions = list_deposit_transactions(name)
    if isinstance(deposit_transactions, list):
        withdrawal_transactions = list_withdraw_transactions(name)
        if isinstance(withdrawal_transactions, list):
            return deposit_transactions + withdrawal_transactions
    return "error while retreiving transactions"


