import socket
from server_lookup import find_server
from socket_client import connect_socket_client, disconnect_socket_client, send_socket_message
from tools import deserialize_transaction_list

client_socket: socket.socket = None # type: ignore

def connect_client():
  global client_socket
  if client_socket is None:
    (server, port) = find_server("withdraw")
    client_socket = connect_socket_client(server, port)

def withdraw(name, amount) -> int:
  connect_client()
  request = f"withdraw|{name}|{amount}"
  response = send_socket_message(client_socket, request)
  # if response is a numeric string, return that
  if response.isdigit():
    return int(response)

  return response

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

  return deserialize_transaction_list(response)

def disconnect_client():
  global client_socket
  if client_socket is not None:
    disconnect_socket_client(client_socket)
    client_socket = None # type: ignore
  