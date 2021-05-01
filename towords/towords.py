import sys, re
import requests
import threading
import redis
import logging
import time
import os

ROOT_DIR = os.path.dirname(os.path.abspath('.')) + '/books'

log = logging.getLogger()
log.setLevel(logging.INFO)

stdout_handler = logging.StreamHandler(sys.stdout)

log.addHandler(stdout_handler)

def getBook(url):
    req = requests.get(url)
    book = req.text.replace('\n', '').replace('\r', '').lower()
    book = re.sub(r'\W+', ' ', book)
    red = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)
    logging.info("Connecting to redis")
    for word in book.split()[:1000]:
        red.incr(word)
    logging.info("%s is done", url)

#print('Argument list: %s' % str(sys.argv))

urls = []
for arg in sys.argv[1:]:
    if 'http' in arg:
        urls.append(arg)

threads = list()
for url in urls:
    logging.info("Main    : create and start thread for %s.", url)
    x = threading.Thread(target=getBook, args=(url, ))
    threads.append(x)
    x.start()