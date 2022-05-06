FROM python

WORKDIR /app

COPY ./requirements.txt .

ENV DB_URL = dummyurl

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT ["python","app.py"]