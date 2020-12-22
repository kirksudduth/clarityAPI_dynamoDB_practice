FROM django

WORKDIR /clarityAPI

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD [ "pyman runserver 0.0.0.0:8000" ]