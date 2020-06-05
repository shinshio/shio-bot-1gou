# coding: utf-8-sig

from bs4 import BeautifulSoup
import requests

import keywords as kwd


URL = 'https://kids.yahoo.co.jp/today/'

def _get_whatday():
    html = requests.get(URL).text
    soup = BeautifulSoup(html, 'html.parser')
    topics = soup.find(class_='mainCt clfix').find('dt').text
    contents = soup.find(class_='mainCt clfix').find('dd').text

    return topics, contents

def respond(message: str) -> str:
    '''respond about message
    args:
        message: str
    returns:
        str
    '''
    result = _get_whatday()
    print(result)
    result_disp = '\\n'.join(result)
    return f'今日は\\n\\n{result_disp}\\n'

if __name__ == '__main__':
    print(respond(''))
