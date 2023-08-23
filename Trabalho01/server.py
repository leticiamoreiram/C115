import socket
from pymongo import MongoClient


def main():
    host = '0.0.0.0'
    port = 12345

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Servidor escutando na porta:", port)

    client_socket, addr = server_socket.accept()
    print("Conexão de:", addr)

    client = MongoClient('mongodb://mongodb:27017')
    db = client['knowledge_db']
    questions_collection = db['questions']
    questions = questions_collection.find()

    for question in questions:
        question_text = question['text']
        question_choices = ', '.join(question['choices'])
        correct_answer = question['correct_answer']

        client_socket.send(question_text.encode())
        client_socket.send(question_choices.encode())

        answer = client_socket.recv(1024).decode()
        response = "Correct!" if answer == correct_answer else f"Wrong! The correct answer is {correct_answer}."
        client_socket.send(response.encode())

    client_socket.close()

if __name__ == '__main__':
    main()
