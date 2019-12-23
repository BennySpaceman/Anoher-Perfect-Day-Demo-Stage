import requests
from bs4 import BeautifulSoup
from urllib.parse import parse_qs
query = input('Type you request: ')
r = requests.get(f'https://google.com/search?q={query}')
soup = BeautifulSoup(r.text, 'html.parser')

refs = soup.select('a')
print('-----------------------------------------------')

clean_refs = []
for i in refs:
  if i['href'].startswith('/url?q='):
    clean_refs.append(i['href'])

for url in clean_refs[:3]:
  query_parts = parse_qs(url)
  print(query_parts['/url?q'][0])
