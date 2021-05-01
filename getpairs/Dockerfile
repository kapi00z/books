FROM python:alpine
WORKDIR /app
RUN mkdir /src

COPY . .

RUN python3 -m pip install --no-cache-dir -r requirements.txt



CMD python3 getpairs.py