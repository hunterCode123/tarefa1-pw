FROM python:3.11-slim

WORKDIR /site

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]