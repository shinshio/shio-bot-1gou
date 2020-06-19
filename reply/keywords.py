# coding: utf-8-sig

# variables
greeting_hi = ['やあ', 'hi', 'yaa', r'genki(\?|？)', 'gokigenyou']
greeting_morning = ['おはよう', 'good morning', 'morning', r'ohayo(u|ugozaimasu)']
greeting_hello = ['こんにちは', 'hello', 'konnichi(ha|wa)']
greeting_evening = ['こんばんは', 'good evening', 'evening', r'konban(ha|wa)']

# dict of modules
GREETINGS = {
    'KWORDS': greeting_hi + greeting_morning + greeting_hello + greeting_evening,
    'M_NAME': 'あいさつ',
    'M_FUNC': '適切な挨拶を返します。'
}

WHEATHERS = {
    'KWORDS': ('てんき', 'tenki', 'wheather'),
    'M_NAME': '天気予報（名古屋）',
    'M_FUNC': '名古屋の天気予報を表示します。'
}

WHATDAYS = {
    'KWORDS': ('なんのひ', 'what day', 'whatday', r'(nan|nani)no(hi|nichi)'),
    'M_NAME': '今日は何の日',
    'M_FUNC': '過去の今日の出来事やイベントを表示します。'
}

OMIKUJI = {
    'KWORDS': ('おみくじ', 'omikuji', r'omiku(ji|zi)'),
    'M_NAME': 'おみくじ',
    'M_FUNC': 'おみくじを引けます。点数もつけます。'
}

HELP = {
    'KWORDS': ('おしえて', 'help', r'o(si|shi)ete', 'wakaranai'),
    'M_NAME': 'ヘルプ機能',
    'M_FUNC': '機能の紹介をします。'
}

VERSIONS = {
    'KWORDS': ('バージョン', 'version', r'baajon'),
    'M_NAME': 'バージョン読み出し',
    'M_FUNC': 'バージョンの確認をします。'
}

# list of dicts
MODULES = [GREETINGS, WHEATHERS, WHATDAYS, OMIKUJI, HELP, VERSIONS]

# version name
RELEASE_VERSION = 'Ver4.0'
