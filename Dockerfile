FROM python:3.11

RUN apt-get update
RUN apt-get install -y python3 python3-pip

WORKDIR /app/

COPY . /app/

RUN pip3 install -r requirements.txt

CMD ["python3", "/app/bot/main.py"]