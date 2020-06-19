# coding: utf-8-sig

import keywords as kwd

def _make_doc(dict: dict):
    text = f'''
    「{dict['M_NAME']}」
    {dict['M_FUNC']}
    反応ワード：{(',').join(dict['KWORDS'][:2])} など
    '''
    return text

def respond(message: str) -> str:
    '''respond about message
    args:
        message: str
    returns:
        str
    '''
    text = [f'''
    以下の機能があります。※アルファベットは大文字小文字どちらでもOK。
    ''']
    for mods in kwd.MODULES:
        text.append(_make_doc(mods))

    return ('').join(text)

if __name__ == '__main__':
    pass
