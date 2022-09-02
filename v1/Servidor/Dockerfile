FROM ubuntu:latest

run apt update
run apt install python3 -y

WORKDIR /usr/app/src

COPY server.py ./

CMD ["python3", "./server.py"]