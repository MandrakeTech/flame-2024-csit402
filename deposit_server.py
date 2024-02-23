
from socket_server import handle_server_requests, start_socket_server
from deposit_tracker import check_balance, deposit, list_transactions


def start_server():
  expense_server = start_socket_server(8081)
  handle_server_requests(expense_server, remote_protocol_handler)

def remote_protocol_handler(message):
    """ 
      The 'exit; command is already handled by the socker server
      All other commands need a "name" to work with.
    """
    # ensure all surrounding space characters are ignored    
    message = message.strip()
    if message == "exit":
        return "exit"

    args = message.split('|')

    response = handle_expense_client_request(args)
    
    # if response is a list, return it as a string separated by '|'
    # if response is a number, return it as a string
    # anything else, print the response, and return "internal error"
    if isinstance(response, list):
        # response is a list of tuples of (str, int), so convert it to a string array
        response_arr = [f"{item[0]},{item[1]}" for item in response]
        response = '|'.join(response_arr)
    elif isinstance(response, int):
        response = str(response)
    else:
        print(response)
        response = "internal error"
        
    return response

def handle_expense_client_request(args):
    command, name, *cmd_params = args
    # if name is not supplied, return "invalid command"
    if name == "":
        return "invalid command"
    
    # all other commands need an amount to be specified,
    # and it needs to be numeric
    if len(cmd_params) == 0:
        # these commands work only if amount is not specified
        if command == "balance":
            return check_balance(name)
        elif command == "list":
            return list_transactions(name)
    elif len(cmd_params) == 1:
      amount = cmd_params[0]
      if amount.isdigit():
        amount = int(amount)
        if command == "deposit":
            # amount needs to be specified, and it should be numeric
            return deposit(name, amount)
    
    return f"invalid command and params: {args}"

if __name__ == "__main__":
    start_server()

