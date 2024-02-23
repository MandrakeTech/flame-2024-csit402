import time

def generateUniqueName() -> str:
    uniq_suffix = int(time.time())
    generated_name = f"user_{uniq_suffix}"
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
    
    response = transactions.split('~')
    if response[0].find(',')!= -1:
        response = [(item.split(',')[0], int(item.split(',')[1])) for item in response]

    return response