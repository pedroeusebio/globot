FROM ubuntu:16.10
MAINTAINER Thiago Perrotta "tbperrotta@gmail.com"
RUN apt-get update -y -q
RUN apt-get install -y -q phantomjs python3-pip python-dev build-essential python3
COPY . /app
WORKDIR /app
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["messenger.py"]
