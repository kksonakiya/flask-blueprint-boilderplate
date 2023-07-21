FROM python:3.10.9

WORKDIR /apps
COPY . .

RUN pipenv install --ignore-pipfile

CMD [ "flask", "run", "--host", "0.0.0.0", "--reload"]