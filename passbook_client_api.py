import socket
from server_lookup import find_server
from socket_client import connect_socket_client, disconnect_socket_client, send_socket_message
from tools import deserialize_transaction_list

client_socket: socket.socket = None

def connect_client():
  global client_socket
  if client_socket is None:
    (server, port) = find_server("passbook")
    client_socket = connect_socket_client(server, port)

def check_balance(name) -> int:
  connect_client()
  request = f"balance|{name}"
  response = send_socket_message(client_socket, request)
  # if response is a numeric string, return that
  try:
    return int(response)
  except:
    return f"Invalid balance: {response}"

def list_transactions(name) -> list:
  connect_client()
  request = f"list|{name}"
  response = send_socket_message(client_socket, request)
  # split the response based on '|'
  transactions = deserialize_transaction_list(response)

  return transactions

def disconnect_client():
  global client_socket
  if client_socket is not None:
    # check if socker is still connected
    disconnect_socket_client(client_socket)
    client_socket = None
  