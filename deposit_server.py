
from socket_server import handle_server_requests, start_socket_server
from deposit_tracker import check_balance, deposit, list_transactions
from tools import serialize_transaction_list


def start_server():
  expense_server = start_socket_server(8081)
  handle_server_requests(expense_server, handle_expense_client_request)

def handle_expense_client_request(args):
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
        if command == "deposit":
            amount = 0
            try:
                amount = int(cmd_params[0])
                # amount needs to be specified, and it should be numeric
                balance = deposit(name, amount)
                return str(balance)
            except:
                pass
    return f"invalid command and params: {args}"

if __name__ == "__main__":
    start_server()
