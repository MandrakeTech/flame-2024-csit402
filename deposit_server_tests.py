# Import functions to be tested
from deposit_tracker import deposit, check_balance, list_transactions, check_balance
from tools import generateUniqueName

def test_deposit():
    name = generateUniqueName()
    deposit(name, 100)
    actual_value = check_balance(name)
    expected_value = 100
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"
    actual_value = list_transactions(name)
    expected_value = [('deposit', 100)]
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"

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

def test_check_balance():
    name = generateUniqueName()
    deposit(name, 50)
    deposit(name, 50)
    actual_value = check_balance(name)
    expected_value = 100
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"

def test_list_transactions():
    name = generateUniqueName()
    deposit(name, 100)
    deposit(name, 200)
    expected_transactions = [('deposit', 100), ('deposit', 200)]
    actual_value = list_transactions(name)
    expected_value = expected_transactions
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"

def run_tests():
    test_deposit()
    test_multi_user_deposit()
    test_check_balance()
    test_list_transactions()
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
