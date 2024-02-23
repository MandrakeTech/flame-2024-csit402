import socket

def start_socket_server(port: int) -> socket.socket:
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(('localhost', port))
  server.listen()
  print(f"Server started on port {port}")
  return server

def stop_server(server: socket.socket):
  server.close()
  print("Server stopped")

def handle_client(client_socket, handler_function):
    while True:
        data = client_socket.recv(1024)  # Assuming data is sent in chunks of 1024 bytes
        if not data:  # Check if connection is closed
            print(f"Connection closed: {client_socket.getpeername()}")
            break
        message = data.decode()  # remove leading and trailing spaces
        response = handler_function(message)  # Pass message to handler_function
        if response == "exit":  # Check for "exit" from handler
            break
        client_socket.send(response.encode())  # Send response back to client
    client_socket.close()  # Close client socket   

def handle_server_requests(server: socket.socket, handler_function):
    while True:
        client_socket, client_address = server.accept()
        print(f"Accepted connection from {client_address}")
        # spawn off the socket handling to a separate thread
        # so that the server can continue to accept connections
        # while the client is handling the request
        # (otherwise the server will block while the client is handling the request)
        import threading
        threading.Thread(target=handle_client, args=(client_socket, handler_function)).start()
