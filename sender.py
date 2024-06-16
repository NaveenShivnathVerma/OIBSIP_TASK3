import socket
import threading

# Function to handle each client connection
def handle_client(client_socket):
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Client says: {message}")
                # Send message back to client
                client_socket.send("Message received".encode('utf-8'))
        except:
            # Close connection if any error occurs
            client_socket.close()
            break

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 1234))
server_socket.listen()

print("Server listening on 'localhost' port 12345")

while True:
    # Accept new connections
    client_socket, address = server_socket.accept()
    print(f"Connection from {address} has been established.")
    # Start a new thread to handle the client
    threading.Thread(target=handle_client, args=(client_socket,)).start()