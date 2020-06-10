# coding: utf-8-sig

import re

from pykakasi import kakasi

import keywords as kwd


kakasi = kakasi()
kakasi.setMode('J', 'a')
kakasi.setMode('H', 'a')
kakasi.setMode('K', 'a')
conv = kakasi.getConverter()

def _pattern_match(message: str, dict: dict) -> bool:
    '''judge if message is in keywords
    Args:
        message: str
        dict: dict that have keys of[KWORDS]
    Return:
        bool
    '''
    if message.isalpha():
        message = message.lower()

    message = conv.do(message)

    return any([re.fullmatch(itr, message) for itr in dict['KWORDS']])

def reply(message: str) -> str:

    if _pattern_match(message, kwd.GREETINGS):
        import greeting as gt
        return gt.respond(message)
    elif _pattern_match(message, kwd.WHEATHERS):
        import wheather as wt
        return wt.respond(message)
    elif _pattern_match(message, kwd.WHATDAYS):
        import whatday as wd
        return wd.respond(message)
    elif _pattern_match(message, kwd.OMIKUJI):
        import omikuji as mj
        return mj.respond(message)
    elif _pattern_match(message, kwd.HELP):
        import osiete
        return osiete.respond(message)
    else:
        return '理解できません'

if __name__ == '__main__':
    pass
