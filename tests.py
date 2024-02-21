# Import functions to be tested
from expense_tracker import deposit, withdraw, check_balance, list_transactions, check_balance

counter = 1

def generateUniqueName():
    global counter
    counter += 1
    return f"user_{counter}"

def test_deposit():
    name = generateUniqueName()
    deposit(name, 100)
    assert check_balance(name) == 100
    assert list_transactions(name) == [('deposit', 100)]

def test_withdraw_sufficient_funds():
    name = generateUniqueName()
    deposit(name, 100)
    withdraw(name, 50)
    assert check_balance(name) == 50
    assert list_transactions(name) == [('deposit', 100), ('withdrawal', 50)]

def test_withdraw_insufficient_funds():
    name = generateUniqueName()
    deposit(name, 50)
    withdraw(name, 100)
    assert check_balance(name) == 50  # Balance should remain unchanged
    assert list_transactions(name) == [('deposit', 50)]

def test_check_balance():
    name = generateUniqueName()
    deposit(name, 50)
    withdraw(name, 50)
    deposit(name, 50)
    assert check_balance(name) == 50

def test_list_transactions():
    name = generateUniqueName()
    deposit(name, 100)
    withdraw(name, 50)
    expected_transactions = [('deposit', 100), ('withdrawal', 50)]
    assert list_transactions(name) == expected_transactions

def run_tests():
    test_deposit()
    test_withdraw_sufficient_funds()
    test_withdraw_insufficient_funds()
    test_check_balance()
    test_list_transactions()
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
