# coding: utf-8-sig

import sys
sys.path.append('./')
sys.path.append('/reply')

import greeting as gt
import wheather as wt
import keywords as kwd


def reply(message: str) -> str:
    if message.isalpha():
        message = message.lower()

    if message in kwd.GREETINGS:
        return gt.respond(message)
    elif message in kwd.WHEATHERS:
        return wt.respond(message)
    else:
        return '理解できません'

if __name__ == '__main__':
    pass
