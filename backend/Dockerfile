FROM python:3.11

WORKDIR /src

COPY ./requirements.txt .

RUN  pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "uvicorn", "host", "0.0.0.0", "main:app" ]