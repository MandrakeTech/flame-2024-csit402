import socket


def connect_socket_client(server: str, port: int) -> socket.socket:
  """
  Connects to the server and returns the socket
  """
  import socket
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((server, port))
  return client

def disconnect_socket_client(client: socket.socket):
  """
  Disconnects the client
  """
  if client is not None:
    client.close()

def send_socket_message(client: socket.socket, message: str):  
  """
  Sends the message to the server and
  Returns the response
  """
  # if socket is none, then print a message and return
  if client is None:
    print("Client is not connected")
    return "Client is not connected"
  
  client.send(message.encode())
  response = client.recv(1024).decode()
  return response