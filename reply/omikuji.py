# coding: utf-8-sig

import random

import keywords as kwd


MU = 0.5
SIGMA = MU * 0.6827

K_KYO = 0.11
K_SUEKICHI = K_KYO + 0.19
K_SHOKICHI = K_SUEKICHI + 0.13
K_TYUKICHI = K_SHOKICHI + 0.10
K_KICHI = K_TYUKICHI + 0.24
K_DAIKICHI = K_KICHI + 0.23

DRAW = {
    '凶': K_KYO,
    '末吉': K_SUEKICHI, '小吉': K_SHOKICHI, '中吉': K_TYUKICHI,
    '吉': K_KICHI, '大吉': K_DAIKICHI
}

def _draw_omikuji():

    rand = random.normalvariate(MU, SIGMA)
    if rand < 0:
        rand = 0
    elif rand > 1:
        rand = 1

    key = ''
    for k, v in DRAW.items():
        if rand <= v:
            key = k
            break

    return key, rand

def respond(message: str) -> str:
    '''respond about message
    args:
        message: str
    returns:
        str
    '''
    key, rand = _draw_omikuji()
    return f'今日の運勢は{key}です。\n点数だと{int(rand*100)}点。'

if __name__ == '__main__':
    pass
