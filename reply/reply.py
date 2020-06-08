# coding: utf-8-sig

import keywords as kwd


def reply(message: str) -> str:
    if message.isalpha():
        message = message.lower()

    if message in kwd.GREETINGS:
        import greeting as gt
        return gt.respond(message)
    elif message in kwd.WHEATHERS:
        import wheather as wt
        return wt.respond(message)
    elif message in kwd.WHATDAYS:
        import whatday as wd
        return wd.respond(message)
    elif message in kwd.OMIKUJI:
        import omikuji as mj
        return mj.respond(message)
    else:
        return '理解できません'

if __name__ == '__main__':
    pass
