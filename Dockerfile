FROM python:3.7
WORKDIR ./app
COPY . ./app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt