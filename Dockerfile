FROM python:3.9

WORKDIR /

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3.9", "-m" , "pytest", "", "tests/test_tags.py"]
