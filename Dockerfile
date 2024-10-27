FROM python:latest

WORKDIR /app
COPY src /app/src

COPY requirements.txt /app

RUN pip install --upgrade -r requirements.txt

CMD ["python", "src/main.py"]