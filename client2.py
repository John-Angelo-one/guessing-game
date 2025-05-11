import socket

host = 'localhost'
port = 7777

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((host, port))

greeting = client_socket.recv(1024).decode()
print(f"Server says: {greeting}")

message = "Hello, Server! This is the client."
client_socket.send(message.encode())

response = client_socket.recv(1024).decode()
print(f"Server response: {response}")

client_socket.close()
