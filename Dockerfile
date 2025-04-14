FROM python:3.13.2-slim

WORKDIR /app
COPY src /app/src

COPY requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["python", "src/main.py"]
