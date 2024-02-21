# Import functions to be tested
from expense_tracker import reset_data, deposit, withdraw, check_balance, list_transactions, check_balance

def test_deposit():
    reset_data()
    deposit(100)
    assert check_balance() == 100
    assert list_transactions() == [('deposit', 100)]

def test_withdraw_sufficient_funds():
    reset_data()
    deposit(100)
    withdraw(50)
    assert check_balance() == 50
    assert list_transactions() == [('deposit', 100), ('withdrawal', 50)]

def test_withdraw_insufficient_funds():
    reset_data()
    deposit(50)
    withdraw(100)
    assert check_balance() == 50  # Balance should remain unchanged
    assert list_transactions() == [('deposit', 50)]

def test_check_balance():
    reset_data()
    deposit(50)
    withdraw(50)
    deposit(50)
    assert check_balance() == 50

def test_list_transactions():
    reset_data()
    deposit(100)
    withdraw(50)
    expected_transactions = [('deposit', 100), ('withdrawal', 50)]
    assert list_transactions() == expected_transactions

def run_tests():
    test_deposit()
    test_withdraw_sufficient_funds()
    test_withdraw_insufficient_funds()
    test_check_balance()
    test_list_transactions()
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
