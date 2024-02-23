# Import functions to be tested
from deposit_client_api import deposit
from passbook_client_api import connect_client, disconnect_client, check_balance, list_transactions, check_balance
from tools import generateUniqueName
from withdraw_client_api import withdraw

def test_deposit():
    name = generateUniqueName()
    deposit(name, 100)
    actual_value = check_balance(name)
    expected_value = 100
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"
    actual_value2 = list_transactions(name)
    expected_value2 = [('deposit', 100)]
    assert actual_value2 == expected_value2, f"Expected: {expected_value2}, Actual: {actual_value2}"

def test_multi_user_deposit():
    name1 = generateUniqueName()
    deposit(name1, 100)
    actual_value = check_balance(name1)
    expected_value = 100
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"
    actual_value = list_transactions(name1)
    expected_value = [('deposit', 100)]
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"
    name2 = generateUniqueName()
    deposit(name2, 100)
    actual_value = check_balance(name2)
    expected_value = 100
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"
    actual_value = list_transactions(name2)
    expected_value = [('deposit', 100)]
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"
    # check user1 again
    actual_value = check_balance(name1)
    expected_value = 100
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"
    actual_value = list_transactions(name1)
    expected_value = [('deposit', 100)]
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"

def test_withdraw_sufficient_funds():
    name = generateUniqueName()
    deposit(name, 100)
    withdraw(name, 50)
    actual_value = check_balance(name)
    expected_value = 50
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"
    actual_value = list_transactions(name)
    expected_value = [('deposit', 100), ('withdrawal', 50)]
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"

def test_withdraw_insufficient_funds():
    name = generateUniqueName()
    deposit(name, 50)
    withdraw(name, 100)
    actual_value = check_balance(name)
    expected_value = 50  # Balance should remain unchanged
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"
    actual_value = list_transactions(name)
    expected_value = [('deposit', 50)]
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"

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
    connect_client()
    test_deposit()
    test_multi_user_deposit()
    test_withdraw_sufficient_funds()
    test_withdraw_insufficient_funds()
    test_check_balance()
    # test_list_transactions()
    disconnect_client()
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
