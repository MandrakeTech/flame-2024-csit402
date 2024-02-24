
from server_lookup import find_server
from socket_server import handle_server_requests, start_socket_server
from passbook_tracker import check_balance, list_transactions
from tools import serialize_transaction_list

def start_server():
  (_, port) = find_server("passbook")
  pb_server = start_socket_server(port)
  handle_server_requests(pb_server, handle_pb_client_request)

def handle_pb_client_request(args) -> str:
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
            transaction = list_transactions(name)
            return serialize_transaction_list(transaction)
    
    return f"invalid command and params: {args}"

if __name__ == "__main__":
    start_server()

