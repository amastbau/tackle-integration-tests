FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD swagger_client /app/swagger_client
ADD tests/ /app/tests
COPY helpers.py /app/

CMD [ "ls", "/app" ]
CMD [ "python3.9", "-m" , "pytest", "/app/tests/test_tags.py"]
