import socket
from socket_client import connect_socket_client, disconnect_socket_client, send_socket_message

client_socket: socket.socket = None

def connect_client():
  global client_socket
  client_socket = connect_socket_client("localhost", 8080)

def deposit(name, amount):
  request = f"deposit|{name}|{amount}"
  response = send_socket_message(client_socket, request)
  # if response is a numeric string, return that
  if response.isdigit():
    return int(response)
  
  return response

def withdraw(name, amount):
  request = f"withdraw|{name}|{amount}"
  response = send_socket_message(client_socket, request)
  # if response is a numeric string, return that
  if response.isdigit():
    return int(response)

  return response

def check_balance(name):
  request = f"balance|{name}"
  response = send_socket_message(client_socket, request)
  # if response is a numeric string, return that
  if response.isdigit():
    return int(response)
  
  return response

def list_transactions(name):
  request = f"list|{name}"
  response = send_socket_message(client_socket, request)
  # split the response based on '|'
  response = response.split('|')
  # if response[0] has a ",", convert the response to a list of tuples,
  # otherwise return the response string as is
  if response[0].find(',')!= -1:
    response = [(item.split(',')[0], int(item.split(',')[1])) for item in response]
  else:
    response = response[0]

  return response

def disconnect_client():
  global client_socket
  send_socket_message(client_socket, "exit")
  disconnect_socket_client(client_socket)
  client_socket = None
  