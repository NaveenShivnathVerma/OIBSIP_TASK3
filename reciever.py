import socket

# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 1234))

while True:
    # Send message to server
    client_socket.send(input("You: ").encode('utf-8'))
    # Receive response from server
    message = client_socket.recv(1024).decode('utf-8')
    print(f"Server: {message}")