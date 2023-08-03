FROM python:3.10.10

RUN useradd -m code

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

EXPOSE 7000:7000

USER code

CMD ["uvicorn", "src.app.main:app", "--reload", "--host", "0.0.0.0", "--port", "7000"]
