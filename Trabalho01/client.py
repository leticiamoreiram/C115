import socket

def main():
    host = 'server'  # Nome do serviço do servidor no Docker Compose
    port = 12345

    client_socket = socket.socket()
    client_socket.connect((host, port))

    print("Connected to server. Let's start answering questions!\n")

    for _ in range(3):
        question = client_socket.recv(1024).decode()
        choices = client_socket.recv(1024).decode()

        print(question)
        print(choices)

        answer = input("Your answer: ")
        client_socket.send(answer.encode())

        response = client_socket.recv(1024).decode()
        print(response)

    client_socket.close()


if __name__ == '__main__':
    main()
