FROM python:3.12
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y sqlite3
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "run.py"]