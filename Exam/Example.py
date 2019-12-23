"""
Группировка файлов по категориям
"""
# import os
# import shutil
# import time
# TYPES = {'DOC': ('doc', 'docx', 'txt', 'pdf'),
#         'PPT': ('ppt', 'pptx'),
#         'XL': ('xls', 'xlsx', 'csv') }

# def sort_files(path):
#     os.chdir(path)
#     for dirname in ('DOC', 'PPT', 'XL', 'ETC'):
#         if not os.path.exists(dirname):
#             os.mkdir(dirname)
#     files = [i for i in os.scandir() if i.is_file() and not i.name.endswith('.py') and not i.name.startswith('.')]

#     for filename in files:
#         ext = filename.name[filename.name.rfind('.')+1: ]
#         print(ext)
#         for type_ in TYPES:
#             if ext in TYPES[type_]:
#                 shutil.move(filename.name, f'{type_}/{filename.name}')
#         if os.path.isfile(filename.name):
#              shutil.move(filename.name, f'ETC/{filename.name}')
# sort_files('.')


"""
Вычисление эффективности алгоритмов
"""
import time
# starttime = time.time()
# print(simple_gcd(4,8))
# endtime = time.time()
# print(f'simple completed in {(endtime-starttime):.5} seconds')


def simple_gcd(a, b):
    starttime = time.time()
    candidates = []
    for i in range(1, min(a, b)):
        if (a % i ==0) and (b % i == 0):
            candidates.append(i)
    endtime = time.time()
    print(f'Simple completed in {endtime - starttime} seconds with a result of {candidates[-1]}')


simple_gcd(44, 33)


def euclide_gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return euclide_gcd(b, b % a)


starttime = time.time()
print(f'Euclide result: {euclide_gcd(33, 44)}.', end=' ')
endtime = time.time()
print(f'Time: {(endtime-starttime):.5} seconds')

"""
По запросу возвращает первые 5 ссылок из гугла
"""

# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import parse_qs
# # query = input('Type a request: ')
# query = 'banana'
# r = requests.get(f'https://google.com/search?q={query}')
#
# soup = BeautifulSoup(r.text, 'html.parser')
# # print(soup.prettify())
#
# refs = soup.select('a')
# clean_refs = []
# for i in refs:
#     if i['href'].startswith('/url?q='):
#         # print(i['href'], end = '\n\n')
#         clean_refs.append(i['href'])
# # print(clean_refs)
#
# # # print(clean_refs[0])
# # clean_refs[0] = clean_refs[0][7: clean_refs[0].find('&sa')]
# # # print(clean_refs[0])
#
# # query_parts = parse_qs(clean_refs[1])
# # print(query_parts['/url?q'][0])
#
# for url in clean_refs[:5]:
#   query_parts = parse_qs(url)
#   print(query_parts['/url?q'][0])
