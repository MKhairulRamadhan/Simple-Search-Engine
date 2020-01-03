#!/usr/bin/python3
from pathlib import Path
from string import punctuation
import os
import sys

def clean(data):
    with open(f'data/cleaning/{data[1]}', 'w') as file:
        for index, line in enumerate(data[0].split('\n')):
            if index is 1:
                main_sentence = line.split('.')
                try:
                    file.write(main_sentence[1].translate(
                        str.maketrans('', '', punctuation))+'\n')
                except IndexError:
                    pass
                    # print('index error..')
                for sentence in main_sentence[2:]:
                    file.write(sentence.translate(
                        str.maketrans('', '', punctuation)))
                continue
            file.write(line.translate(
                str.maketrans('', '', punctuation))+'\n')

if os.path.exists('data/crawling'):
    print(f'Directory : data/crawling')
    print('Cleaning prosesss....!')
    for f in Path('.').glob(f"data/crawling/*.txt"):
        name = str(f).split('/')
        File = open(f, 'r').read()
        clean([File, name[2]])
else:
    print("directory no found")
    sys.exit(1)
