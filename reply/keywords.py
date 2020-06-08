# coding: utf-8-sig

# variables
greeting_hi = ['hi', 'やあ', '元気', '元気？', 'げんき', 'げんき？', 'ごきげんよう', 'ご機嫌よう']
greeting_morning = ['good morning', 'morning', 'おはよう', 'おはようございます']
greeting_hello = ['hello', 'こんにちは', 'こんにちわ', '今日は']
greeting_evening = ['good evening', 'evening', 'こんばんは', 'こんばんわ']

# dict of modules
GREETINGS = {
    'KWORDS': greeting_hi + greeting_morning + greeting_hello + greeting_evening,
    'M_NAME': 'あいさつ',
    'M_FUNC': '適切な挨拶を返します。'
}

WHEATHERS = {
    'KWORDS': ('tenki', 'wheather', '天気', 'てんき'),
    'M_NAME': '天気予報（名古屋）',
    'M_FUNC': '名古屋の天気予報を表示します。'
}

WHATDAYS = {
    'KWORDS': ('what day', 'whatday', 'なんのひ', 'なんの日', '何のひ', '何の日'),
    'M_NAME': '今日は何の日',
    'M_FUNC': '過去の今日の出来事やイベントを表示します。'
}

OMIKUJI = {
    'KWORDS': ('omikuji', 'おみくじ'),
    'M_NAME': 'おみくじ',
    'M_FUNC': 'おみくじを引けます。点数もつけます。'
}

HELP = {
    'KWORDS': ('help', 'おしえて', '教えて', 'わからない'),
    'M_NAME': 'ヘルプ機能',
    'M_FUNC': '機能の紹介をします。'
}

# list of dicts
MODULES = [GREETINGS, WHEATHERS, WHATDAYS, OMIKUJI, HELP]
