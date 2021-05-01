import redis
import json
import os

ROOT_DIR = os.path.dirname(os.path.abspath('.')) + '/books'

def getKeys():
    keyArr = []
    red = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)
    for key in red.keys('*'):
        value = red.get(key)
        pair = {key : value}
        #print(pair)
        keyArr.append(pair)
    return keyArr

#print(len(getKeys()))
pairlist = getKeys()
jsonwords = {}
for pair in pairlist:
    jsonwords.update(pair)
words = {'wordlist': pairlist}
with open(ROOT_DIR + '/src/words.txt', 'w') as file:
    file.write(json.dumps(words))
with open(ROOT_DIR + '/src/pairs.txt', 'w') as file:
    file.write(json.dumps(pairlist))
with open(ROOT_DIR + '/src/json.txt', 'w') as file:
    file.write(json.dumps(jsonwords))
print(os.path.abspath("."))