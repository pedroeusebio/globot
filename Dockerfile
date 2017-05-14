FROM ubuntu:16.04
MAINTAINER Thiago Perrotta "tbperrotta@gmail.com"
RUN apt-get update -y -q
RUN apt-get install -y -q python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["messenger.py"]
