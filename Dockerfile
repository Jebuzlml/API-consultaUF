FROM python:3-slim

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt

RUN pip install --upgrade -r /api/requirements.txt

COPY ./ /api

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
