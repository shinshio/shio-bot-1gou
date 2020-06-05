# coding: utf-8-sig


import sys
sys.path.append('./')
sys.path.append('/reply')

from bs4 import BeautifulSoup
import requests

import keywords as kwd


URL = 'https://tenki.jp/forecast/5/26/5110/23100/'

def get_wheather():
    html = requests.get(URL).text
    soup = BeautifulSoup(html, 'html.parser')
    weather = soup.find(class_='today-weather').find(class_='weather-telop').text
    temperature = soup.find(class_='today-weather').find(class_='high-temp temp').text

    return [weather, temperature]

def respond(message: str) -> str:
    '''respond about message
    args:
        message: str
    returns:
        str
    '''
    result = get_wheather()
    return f'今日の名古屋市の天気は{result[0]}です。最高温度は{result[1]}です。'

if __name__ == '__main__':
    pass
