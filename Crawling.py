from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from pathlib import Path
import sys
import requests
import argparse
import string

# scrapping url method
def scrap(data):
    path = Path()/"data/crawling"/f'data{data[0]}.txt'
    with open(path, 'w') as crawl:
        soup = BeautifulSoup(requests.get(data[1]).text, 'html.parser')
        content = soup.select_one('.read__content')
        for i in content('script'):
            i.decompose()
        title = soup.select_one('.read__title').get_text().strip()
        content = content.get_text().strip()  
        # data[2].write(data[1]+'\n')
        crawl.write(title+'\n')
        crawl.write(content)


# argument documentary
arg = argparse.ArgumentParser()
option = arg.add_mutually_exclusive_group()
option.add_argument("-p", "--page-limit",
                    help="limit file by number of files", type=int)
option.add_argument("-d", "--day-limit",
                    help="limit file by days backward", type=int)
args = vars(arg.parse_args())

# dinamic link
indexlink = "http://indeks.kompas.com/terpopuler/?site=all&date="

# get time of today
date = datetime.today()

# number of day and limit
day, day_limit = 1, args['day_limit'] if args['day_limit'] != None else None

# number of page and limit
page, page_limit = 0, args['page_limit'] if args['page_limit'] != None else None

# looping to get dynamic link by time
f = open('data/link/link.txt','w');
# with open ('data/link/link.txt','w') as buka:
while True:
    link = f'{indexlink}{date.strftime("%Y-%m-%d")}'
    # looping to get all detail link
    while True:
        print(f'get url  : {link}')
        soup = BeautifulSoup(requests.get(
            link).text.encode('utf-8'), 'html.parser')
        print("Url found      : ", len(soup.select('.article__title')))
        for url in soup.select('.article__title'):
            urls = url.find('a')['href']
            try:
                f.write(urls+'\n')
                # clean url and put on directory
                scrap([page, urls])
            except AttributeError:
                print('error atribute..')
            page += 1
            if page == page_limit:
                sys.exit(f'Program mencapai batas max {page_limit} page')
        else:
            break
    if day == day_limit:
        sys.exit(f'Program mencapai batas max {day_limit} day')
    date += timedelta(days=-1)
    day += 1
