# Import functions to be tested
from tools import generateUniqueName
from withdraw_tracker import withdraw, check_balance, list_transactions, check_balance

def test_multi_user_withdraw():
    name1 = generateUniqueName()
    withdraw(name1, 100)
    actual_value = check_balance(name1)
    expected_value = 100
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"
    actual_value = list_transactions(name1)
    expected_value = [('withdrawal', 100)]
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"
    name2 = generateUniqueName()
    withdraw(name2, 100)
    actual_value = check_balance(name2)
    expected_value = 100
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"
    actual_value = list_transactions(name2)
    expected_value = [('withdrawal', 100)]
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"
    # check user1 again
    actual_value = check_balance(name1)
    expected_value = 100
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"
    actual_value = list_transactions(name1)
    expected_value = [('withdrawal', 100)]
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"

def test_withdraw():
    name = generateUniqueName()
    withdraw(name, 50)
    actual_value = check_balance(name)
    expected_value = 50
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"
    actual_value = list_transactions(name)
    expected_value = [('withdrawal', 50)]
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"

def test_check_balance():
    name = generateUniqueName()
    withdraw(name, 50)
    withdraw(name, 50)
    actual_value = check_balance(name)
    expected_value = 100
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"

def test_list_transactions():
    name = generateUniqueName()
    withdraw(name, 50)
    expected_transactions = [('withdrawal', 50)]
    actual_value = list_transactions(name)
    expected_value = expected_transactions
    assert actual_value == expected_value, f"Expected: {expected_value}, Actual: {actual_value}"

def run_tests():
    test_withdraw()
    test_multi_user_withdraw()
    test_check_balance()
    test_list_transactions()
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
