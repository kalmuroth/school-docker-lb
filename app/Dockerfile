FROM python:3.9

WORKDIR /app

COPY . .

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install --no-cache-dir -r requirements.txt

RUN python3 -m unittest discover -p test_app.py

EXPOSE 5000

CMD [ "python", "app.py"]
