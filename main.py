import time
from urllib import parse

import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)


def param_str(_type, page=None):
    if _type == 'list':
        encrypt = '{"a":"8.0","b":{"a":"65493","actionType":"1.0","b":"795d7759-0c9c-4b54-8638-1b8d28731d38","c":"","d":"","e":"","f":"","g":"应用案例","h":"","i":"","j":"","k":"","l":"推荐","m":"desc","n":"1","o":"10","r":"","strTime":"1652003356844"}}'
    elif _type == 'detail':
        encrypt = '{"a":"8.0","b":{"a":"65493","actionType":"3.0","b":"795d7759-0c9c-4b54-8638-1b8d28731d38","c":"2412","d":"1","strTime":"1652003398720"}}'
    else:
        print('未开发该类型接口')
        return None
    return encrypt


def case_quote(text):
    new_text = parse.quote(text)
    return new_text


def case_req(encode_text):
    link = f'https://www.soliao.com/api/app/server?data={case_quote(encode_text)}'
    headers = {
        'Host': 'www.soliao.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.12.12'
    }

    resp = requests.get(url=link, headers=headers)
    pp.pprint(resp.json())


if __name__ == '__main__':
    _text = 'ka66WFllfShJv9cuVB%2Fg3IvmWjb3qqy7k6ZuIMe4kLcyJbI1jPpx9pe3KVAlovSo%2BUwat07Nt1yZ%0A80bLPw4dkI5V5tzhXoSVm1ldLOqU6b5kuc1k6EnIC9oBhJUX7%2BJztx31DHA5g2vC3l08Z3OxrcbC%0Al8c%2FmkMI%2FNks59Hgg2tnvn1UXIAFL6pv%2BTpoFsKCkKDyMlGte8b9QQ0vgUd0tkIRzCbfi1Sjgty5%0A4l4sv6sOvZ%2BJ0rbVoDOeMJJbZKyPq2koncpv1DeXJGvdwaGl9ZpTU2lO0gLsDNxE6nV7Xf0Me8bk%0ATCxYRMGdYTg%2FEoOt1Q1GIb9hKtxc4RJjFKnTdg%3D%3D'
    case_req(_text)
