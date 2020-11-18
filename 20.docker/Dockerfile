FROM python:3.8.6-buster

WORKDIR /app

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="/root/.poetry/bin:${PATH}"
RUN poetry config virtualenvs.create false

COPY my-shop/pyproject.toml my-sop/poetry.lock ./

RUN poetry install --no-interaction --no-ansi

EXPOSE 5000

COPY my-shop .

CMD ["python", "main.py"]

