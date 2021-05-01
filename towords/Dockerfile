FROM python:alpine

WORKDIR /src

COPY . .

RUN python3 -m pip install --no-cache-dir -r requirements.txt

CMD ["python3", "get.py"]