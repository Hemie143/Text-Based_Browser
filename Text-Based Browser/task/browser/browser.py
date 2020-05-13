import sys
import os
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import Fore

# write your code here
TAGS = ['p', 'a', 'ul', 'ol', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
args = sys.argv
dir_name = args[1]
cache_files = []

if not os.path.exists(dir_name):
    os.mkdir(dir_name)

history = deque()

while True:
    cmd = input()
    if cmd == 'exit':
        break
    if cmd == 'back':
        if len(history) > 1:
            history.pop()
            cmd = history.pop()

    if cmd in cache_files:
        filename_full = f'{dir_name}/{cmd}'
        with open(filename_full, 'r') as f:
            print(f.read())
        history.append(cmd)
    elif '.' not in cmd:
        print('error')
    else:
        url = cmd
        if not cmd.startswith('https://'):
            url = f'https://{cmd}'
        r = requests.get(url)
        # r_text = r.content
        soup = BeautifulSoup(r.content, 'html.parser')
        html = soup.find('html')
        body = html.find('body')
        filtered_soup = body.find_all(TAGS)
        filename = '.'.join(cmd.split('.')[:-1])
        filename_full = f'{dir_name}/{filename}'
        with open(filename_full, 'w') as f:
            for line in filtered_soup:
                text = line.get_text().strip()
                if text:
                    print(Fore.BLUE + text)
                    print(Fore.BLUE + text, file=f)
        cache_files.append(filename)
        history.append(cmd)
