FROM ubuntu:16.04
MAINTAINER Thiago Perrotta "tbperrotta@gmail.com"
RUN apt-get update -y -q
RUN apt-get install -y -q python3-pip python-dev build-essential python3
COPY . /app
WORKDIR /app
RUN pip3 install --upgrade pip3 && pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["messenger.py"]
