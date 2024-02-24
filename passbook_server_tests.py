# Import functions to be tested
import time
from passbook_tracker import check_balance, list_transactions
from deposit_client_api import connect_client as connect_deposit_server, disconnect_client as disconnect_deposit_server, deposit
from tools import generateUniqueName
from withdraw_client_api import connect_client as connect_withdrawal_server, disconnect_client as disconnect_withdrawal_server, withdraw

def test_check_balance():
    name = generateUniqueName()
    deposit(name, 50)
    withdraw(name, 50)
    deposit(name, 50)
    actual_value = check_balance(name)
    expected_value = 50
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"

def test_list_transactions():
    name = generateUniqueName()
    deposit(name, 100)
    withdraw(name, 50)
    expected_transactions = [('deposit', 100), ('withdrawal', 50)]
    actual_value = list_transactions(name)
    expected_value = expected_transactions
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"

def run_tests():
    test_check_balance()
    test_list_transactions()
    print("All tests passed!")

if __name__ == "__main__":
    connect_deposit_server()
    connect_withdrawal_server()
    run_tests()
    disconnect_deposit_server()
    disconnect_withdrawal_server()
