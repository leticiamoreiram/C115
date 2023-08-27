import socket

def main():
    HOST = '127.0.0.1'
    PORT = 50000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    for _ in range(3):
        question = client_socket.recv(4096).decode()
        print(question)
        user_answer = input("Insira a letra correspondente à resposta correta: ").lower()
        client_socket.sendall(str.encode(user_answer))

        feedback = client_socket.recv(4096).decode()
        print(feedback)

    client_socket.close()

if __name__ == '__main__':
    main()
