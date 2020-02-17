FROM python:3.7-alpine
LABEL maintainer=Shaun.Garwood@gmail.com

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python"]
CMD ["app.py"]
