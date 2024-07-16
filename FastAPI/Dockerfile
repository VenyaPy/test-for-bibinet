FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:8001", "main:app", "-k", "uvicorn.workers.UvicornWorker"]
