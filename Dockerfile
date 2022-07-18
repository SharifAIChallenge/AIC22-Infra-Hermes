FROM reg.aichallenge.ir/python:3.8


WORKDIR /home
ADD ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt
ADD ./ ./

CMD ["python3", "event_consumer.py"]

