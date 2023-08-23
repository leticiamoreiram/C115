FROM python:3.9

COPY server.py /app/server.py
COPY client.py /app/client.py
COPY questions.json /app/questions.json

WORKDIR /app

CMD ["python", "server.py"]
