# coding: utf-8-sig


import sys
sys.path.append('./')
sys.path.append('/reply')

import keywords as kwd


def respond(message: str) -> str:
    '''respond about message
    args:
        message: str
    returns:
        str
    '''
    if message in kwd.greeting_hi:
        return '元気です'
    elif message in kwd.greeting_morning:
        return 'おはようございます'
    elif message in kwd.greeting_hello:
        return 'こんにちは'
    elif message in kwd.greeting_evening:
        return 'こんばんは'
    else:
        return '理解できません'

if __name__ == '__main__':
    pass
