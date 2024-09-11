FROM python:3.11.9

RUN mkdir /gateway-app
WORKDIR /gateway-app

COPY . .
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev

CMD gunicorn -c conf/gunicorn.conf.py 'src.app.main.main:get_fastapi_app'