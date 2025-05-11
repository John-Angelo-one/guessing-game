import socket

host = 'localhost'
port = 7777

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

print(f"Server listening on {host}:{port}...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    client_socket.send("Hello, Client! You are connected.".encode())

    message = client_socket.recv(1024).decode()
    print(f"Received from client: {message}")

    client_socket.send(f"Server received: {message}".encode())

    client_socket.close()
