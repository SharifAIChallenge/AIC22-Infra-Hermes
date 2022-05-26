FROM reg.aichallenge.ir/python:3.10

WORKDIR /home
ADD ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt
ADD ./ ./

