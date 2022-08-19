FROM    python:3.10-slim

RUN     apt -y update

COPY    ./requirements.txt /tmp/
RUN     pip install -r /tmp/requirements.txt

COPY    . /srv/cafe
WORKDIR /srv/cafe/app

CMD     ["python", "manage.py", "runserver", "0:8000"]