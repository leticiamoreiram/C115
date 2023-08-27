import socket
from pymongo import MongoClient

RED_COLOR = "\033[91m"  # Código para vermelho
GREEN_COLOR = "\033[92m"  # Código para verde
RESET_COLOR = "\033[0m"   # Reseta a cor para a padrão

def main():
    client = MongoClient('mongodb://mongoadmin:secret@localhost:27017')
    db = client['knowledge_db']
    questions = db.questions

    HOST = 'localhost'
    PORT = 50000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print("Aguardando conexão de um cliente...")

    client_socket, addr = server_socket.accept()
    print("Conectado em: ", addr)

    results = questions.find().limit(3)  # Limitar a três perguntas
    for question in results:
        question_str = question['text'] + "\n"
        for idx, choice in enumerate(question['choices']):
            question_str += f"{chr(97 + idx)}) {choice}\n"

        client_socket.sendall(str.encode(question_str))
        user_answer = client_socket.recv(1024).decode()

        correct_letter = chr(97 + question['choices'].index(question['correct_answer']))

        if user_answer == correct_letter:
            feedback = GREEN_COLOR + "\nSua resposta está correta! :)" + RESET_COLOR + "\n"
        else:
            feedback = RED_COLOR + f"\nVocê errou :( A resposta correta é a letra: {correct_letter}" + RESET_COLOR + "\n"

        client_socket.sendall(str.encode(feedback))

    print("Perguntas enviadas. Fechando conexão...")
    client_socket.close()
    server_socket.close()

if __name__ == '__main__':
    main()

