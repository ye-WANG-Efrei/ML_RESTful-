# Dockerfile to build a flask app
FROM python:3
WORKDIR /usr
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python","-m","flask","run"]