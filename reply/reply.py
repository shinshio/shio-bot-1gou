# coding: utf-8-sig

import keywords as kwd


def reply(message: str) -> str:
    if message.isalpha():
        message = message.lower()

    if message in kwd.GREETINGS['KWORDS']:
        import greeting as gt
        return gt.respond(message)
    elif message in kwd.WHEATHERS['KWORDS']:
        import wheather as wt
        return wt.respond(message)
    elif message in kwd.WHATDAYS['KWORDS']:
        import whatday as wd
        return wd.respond(message)
    elif message in kwd.OMIKUJI['KWORDS']:
        import omikuji as mj
        return mj.respond(message)
    elif message in kwd.HELP['KWORDS']:
        import osiete
        return osiete.respond(message)
    else:
        return '理解できません'

if __name__ == '__main__':
    pass
