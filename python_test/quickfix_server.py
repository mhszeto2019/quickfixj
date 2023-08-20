import socket

def handle_fix_message(message):
    # Add your business logic here
    # You can parse the incoming FIX message, process it, and generate responses
    response = "8=FIX.4.4|35=8|49=Server|56=Client|34=1|11=Order123|39=2|"
    return response

def main():
    server_ip = "127.0.0.1"
    server_port = 5050

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)

    print(f"Listening on {server_ip}:{server_port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        while True:
            data = client_socket.recv(1024).decode("utf-8")
            if not data:
                break

            print(f"Received message from client: {data}")

            response = handle_fix_message(data)
            client_socket.sendall(response.encode("utf-8"))

        client_socket.close()
        print(f"Connection with {client_address} closed")

if __name__ == "__main__":
    main()
