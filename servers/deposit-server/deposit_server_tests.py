# Import functions to be tested
from deposit_tracker import deposit, check_balance, list_transactions, check_balance

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

def test_multi_user_deposit():
    name1 = generateUniqueName()
    deposit(name1, 100)
    assert check_balance(name1) == 100
    assert list_transactions(name1) == [('deposit', 100)]
    name2 = generateUniqueName()
    deposit(name2, 100)
    assert check_balance(name2) == 100
    assert list_transactions(name2) == [('deposit', 100)]
    # check user1 again
    assert check_balance(name1) == 100
    assert list_transactions(name1) == [('deposit', 100)]

def test_check_balance():
    name = generateUniqueName()
    deposit(name, 50)
    deposit(name, 50)
    assert check_balance(name) == 100

def test_list_transactions():
    name = generateUniqueName()
    deposit(name, 100)
    deposit(name, 200)
    expected_transactions = [('deposit', 100), ('deposit', 200)]
    assert list_transactions(name) == expected_transactions

def run_tests():
    test_deposit()
    test_multi_user_deposit()
    test_check_balance()
    test_list_transactions()
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
