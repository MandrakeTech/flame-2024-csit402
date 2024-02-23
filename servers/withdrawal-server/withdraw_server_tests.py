# Import functions to be tested
from withdraw_tracker import withdraw, check_balance, list_transactions, check_balance

counter = 1

def generateUniqueName():
    global counter
    counter += 1
    return f"user_{counter}"

def test_multi_user_withdraw():
    name1 = generateUniqueName()
    withdraw(name1, 100)
    assert check_balance(name1) == -100
    assert list_transactions(name1) == [('withdrawal', 100)]
    name2 = generateUniqueName()
    withdraw(name2, 100)
    assert check_balance(name2) == -100
    assert list_transactions(name2) == [('withdrawal', 100)]
    # check user1 again
    assert check_balance(name1) == -100
    assert list_transactions(name1) == [('withdrawal', 100)]

def test_withdraw():
    name = generateUniqueName()
    withdraw(name, 50)
    assert check_balance(name) == -50
    assert list_transactions(name) == [('withdrawal', 50)]

def test_check_balance():
    name = generateUniqueName()
    withdraw(name, 50)
    withdraw(name, 50)
    assert check_balance(name) == -100

def test_list_transactions():
    name = generateUniqueName()
    withdraw(name, 50)
    expected_transactions = [('withdrawal', 50)]
    assert list_transactions(name) == expected_transactions

def run_tests():
    test_withdraw()
    test_multi_user_withdraw()
    test_check_balance()
    test_list_transactions()
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
