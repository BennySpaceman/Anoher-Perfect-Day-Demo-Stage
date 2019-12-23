import requests
from bs4 import BeautifulSoup

query = input('Type your request: ')
r = requests.get(f'https://www.avito.ru/moskva?q={query}')
soup = BeautifulSoup(r.text, 'html.parser')

refs = soup.select('h3 > a')
print('-----------------------------------------------')

clean_refs = []
for i in refs:
    clean_refs.append(i['href'])
for url in clean_refs[:3]:
    print(f'https://www.avito.ru{url}')
