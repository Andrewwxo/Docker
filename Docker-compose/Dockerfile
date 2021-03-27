FROM python:3.8-buster

WORKDIR /var/app

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY my-shop/pyproject.toml ./
RUN poetry install --no-interaction --no-ansi

COPY my-shop/my_shop .

EXPOSE 5000   #hint to forward the port








