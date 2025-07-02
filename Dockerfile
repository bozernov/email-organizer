FROM python:3.10-slim

WORKDIR /app

COPY hello_world.py .

RUN pip install openai==0.28.1

CMD ["python", "hello_world.py"]
