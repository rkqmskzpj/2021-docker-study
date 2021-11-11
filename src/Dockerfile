FROM python:3.9.7-slim
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN apt-get update && \
    apt-get install -y default-mysql-client build-essential python3-dev default-libmysqlclient-dev wget && \
    pip install --upgrade pip && \
    pip install -r requirements.txt
COPY . /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000","--reload"]
