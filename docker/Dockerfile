FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY ui ./ui

CMD ["python", "app/main.py", "--logfile", "app/logs/sample_auth.log"]
