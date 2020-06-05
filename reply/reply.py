# coding: utf-8-sig

import greeting as gt
import wheather as wt
import whatday as wd
import keywords as kwd


def reply(message: str) -> str:
    if message.isalpha():
        message = message.lower()

    if message in kwd.GREETINGS:
        return gt.respond(message)
    elif message in kwd.WHEATHERS:
        return wt.respond(message)
    elif message in kwd.WHATDAYS:
        return wd.respond(message)
    else:
        return '理解できません'

if __name__ == '__main__':
    pass
