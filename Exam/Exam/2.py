import os
import shutil
TYPES = {'EXE': 'exe',
         'JPG': 'jpg',
         'ZIP': 'zip'}


def create_dirs():
    for dirname in ('EXE', 'JPG', 'ZIP', 'Other'):
        if not os.path.exists(dirname):
            os.mkdir(dirname)


def sort_files(path):
    os.chdir(path)
    create_dirs()
    all_files = list(filter(os.path.isfile, os.listdir(path)))
    files = [i for i in all_files if not i.endswith('.py') and not i.startswith('.')]
    for filename in files:
        ext = filename[filename.rfind('.') + 1:]
        for i in TYPES:
            if ext in TYPES[i]:
                shutil.move(filename, f'{i}/{filename}')
        if os.path.isfile(filename):
            shutil.move(filename, f'Other/{filename}')


sort_files(r'C:\Users\danil\PycharmProjects\untitled1')
