FROM python:3.10.12-slim

WORKDIR /app

COPY bs4 /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "bank/safra.py"]
