import time
from urllib import parse

import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)


def param_str(_type, page=None):
    if _type == 'list':
        content = '{"a":"8.0","b":{"a":"65493","actionType":"1.0","b":"795d7759-0c9c-4b54-8638-1b8d28731d38","c":"","d":"","e":"","f":"","g":"应用案例","h":"","i":"","j":"","k":"","l":"推荐","m":"desc","n":"1","o":"10","r":"","strTime":"1652003356844"}}'
    elif _type == 'detail':
        content = '{"a":"8.0","b":{"a":"65493","actionType":"3.0","b":"795d7759-0c9c-4b54-8638-1b8d28731d38","c":"2412","d":"1","strTime":"1652003398720"}}'
    else:
        print('未开发该类型接口')
        return None
    return content


def case_quote(text):
    new_text = parse.quote(text)
    return new_text


def case_req(encode_text):
    info = case_quote(encode_text)
    link = f'https://www.soliao.com/api/app/server?data={info}'
    headers = {
        'Host': 'www.soliao.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.12.12'
    }

    resp = requests.get(url=link, headers=headers)
    pp.pprint(resp.json())


if __name__ == '__main__':
    _text = 'nfQkrbeX7qULuQIhYGUJjA3KsrVH5+ZRcA1AMoKqzDhiB3Na/bjgPhoK5jVKoIdN4UXylsk5mhnU%0AcZyXRXvIlClz2ED2Og0Gz3k56LY41lnPGWTUNmHDe0ubbpALpUlBpht9YkxSiQtPrzfSJKhb9LMZ%0A3EReNgCHEdWhgbZTyGti8YEKSQwQcm2RxXQi6w/NSl3wZO8BIBJKLjCZOo9eV/38bqTb8+v3jM0c%0Am4K65xHdW6jmSGbvH5FnwRjGAoqS6u7QOyfClHWyAHynXLcPqlcC2B2xBPH2E9Vj47xYJx3061e7%0AHLvA5VxPhmm+xZ0LCF6+1lg0JcW4vs7NtA4T1A=='
    case_req(_text)
