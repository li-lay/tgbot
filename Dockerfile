FROM python:3.12-slim

WORKDIR /app
COPY src /app/src

COPY requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["python", "src/main.py"]
