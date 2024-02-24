
from server_lookup import find_server
from socket_server import handle_server_requests, start_socket_server
from tools import serialize_transaction_list
from withdraw_tracker import check_balance, list_transactions, withdraw


def start_server():
    (_, port) = find_server("withdraw")
    withdraw_server = start_socket_server(port)
    handle_server_requests(withdraw_server, handle_withdraw_client_request)

def handle_withdraw_client_request(args):
    command, name, *cmd_params = args.split("|")
    # if name is not supplied, return "invalid command"
    if name == "":
        return "invalid command"
    
    # all other commands need an amount to be specified,
    # and it needs to be numeric
    if len(cmd_params) == 0:
        # these commands work only if amount is not specified
        if command == "balance":
            balance = check_balance(name)
            return str(balance)
        elif command == "list":
            transactions = list_transactions(name)
            return serialize_transaction_list(transactions)
    elif len(cmd_params) == 1:      
      if command == "withdraw":
        try:
           amount = int(cmd_params[0])
           balance = withdraw(name, amount)
           return str(balance)
        except:
           pass                
    
    return f"invalid command and params: [{args}], [{command}][{name}][{cmd_params}]"

if __name__ == "__main__":
    start_server()

