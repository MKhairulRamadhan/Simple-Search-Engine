#!/usr/bin/python3
import json
import sys
import os
from pathlib import Path

if not sys.argv[2]:
    print("tidak ada query...")
    sys.exit(1)

listterm, query, result = dict(), dict(), dict()
with open('data/indexing/index.txt', 'r') as file:
    file = file.read()
    for lines in file.split('\n'):
        line = lines.split(' ')
        listterm[line[0]] = dict()
        for col in line[1:]:
            datacol = col.split(':')
            listterm[line[0]][datacol[0]] = datacol[1]

for word in sys.argv[2:]:
    word = word.lower()
    if word in query:
        query[word] += 1
    else:
        query[word] = 1

for word, term in query.items():
    if word not in listterm:
        continue
    index = sorted(listterm[word].items(), key=lambda x: x[1], reverse=True)
    for doc, score in index:
        if score is '0':
            break
        if doc in result:
            result[doc] += float(score) * term
        else:
            result[doc] = float(score)

results = sorted(result.items(), key=lambda x: x[1], reverse=True)
outjson = []

top = sys.argv[1] if sys.argv is not None else len(results)

i = 0

with open('data/link/link.txt', 'r') as link:
    links = link.read().split('\n')
    for doc, score in results:
        index = doc.split('.')
        index = index[0].split('data')
        if score is '0' or int(top) is i:
            break
        # ada beberapa yang tidak memiliki datanya
        try:
            outjson.append({
                'doc': doc,
                'score': score,
                'url': links[int(index[1])],
            })
            i += 1
        except IndexError:
            pass

print(json.dumps(outjson))
