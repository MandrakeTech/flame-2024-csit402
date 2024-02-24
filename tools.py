import time

counter = 0

def generateUniqueName() -> str:
    global counter
    uniq_suffix = int(time.time()*100000)
    counter += 1
    generated_name = f"user_{uniq_suffix}_{counter}"
    print(f"Generated name: {generated_name}")
    return generated_name

def serialize_transaction_list(transactions: list) -> str:
    response_arr = []
    if isinstance(transactions, list):
        # response is a list of tuples of (str, int), so convert it to a string array
        response_arr = [f"{item[0]},{item[1]}" for item in transactions]

    response = '~'.join(response_arr)
    return f"list|{response}"

def deserialize_transaction_list(message: str) -> list:
    data_type, transactions = message.split('|')
    if data_type != "list":
        return []
    
    if transactions == "":
        return []
    
    transaction_str_list = transactions.split('~')
    # convert transaction_str_list into transaction_list
    # where each item in transaction_str_list, if it has a comma, is a tuple of (str,int)
    # otherwise ignore item
    transaction_list = []
    for item in transaction_str_list:
        (txn_type, txn_amount_str) = item.split(',')
        if txn_type!= "" and txn_amount_str!= "":
            transaction_list.append((txn_type, int(txn_amount_str)))

    return transaction_list