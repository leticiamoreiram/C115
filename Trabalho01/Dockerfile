FROM python:3.9

RUN pip install pymongo

COPY server.py /app/server.py
COPY questions.json /app/questions.json

WORKDIR /app

CMD ["python", "server.py"]
