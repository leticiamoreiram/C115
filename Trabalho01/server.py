import socket
import json

def main():
    host = '0.0.0.0'
    port = 12345

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server listening on port:", port)

    client_socket, addr = server_socket.accept()
    print("Connection from:", addr)

    with open('questions.json', 'r') as file:
        questions = json.load(file)

    for question in questions:
        client_socket.send(question['text'].encode())
        choices = ', '.join(question['choices'])
        client_socket.send(choices.encode())

        answer = client_socket.recv(1024).decode()
        correct_answer = question['correct_answer']
        response = "Correct!" if answer == correct_answer else f"Wrong! The correct answer is {correct_answer}."
        client_socket.send(response.encode())

    client_socket.close()

if __name__ == '__main__':
    main()
