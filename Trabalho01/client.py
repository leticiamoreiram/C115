import socket
from pymongo import MongoClient

def main():
    host = 'localhost'
    port = 12345

    client_socket = socket.socket()
    client_socket.connect((host, port))

    print("Conectado ao servidor. Vamos responder algumas perguntas?\n")

    client = MongoClient('mongodb://mongodb:27017')
    db = client['knowledge_db']
    questions_collection = db['questions']
    questions = questions_collection.find()

    for question in questions:
        question_text = question['text']
        question_choices = ', '.join(question['choices'])

        print(question_text)
        print(question_choices)

        answer = input("Your answer: ")
        client_socket.send(answer.encode())

        response = client_socket.recv(1024).decode()
        print(response)

    client_socket.close()

if __name__ == '__main__':
    main()
