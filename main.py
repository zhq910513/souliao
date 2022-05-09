import time
from urllib import parse
import base64
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pksc1_v1_5
from Crypto.PublicKey import RSA
import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

pub_key = """MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCgVV2WmQVfLUqEgXmcSh6N0d5W\nWjONmiN2UQXwyADctCBBDB8+60zYqH9wpoxhIXxOOyFzr5HzHaKJh22pak/AQBCq\nu06POajBB3Nb/tPt/zHelPytSiAdboeY2jRsW0rgDiKQ1+JEDFHi+yMW7ldcsogp\nsmEhrUkcuE4PzqCYlQIDAQAB"""

def rsa_long_encrypt(pub_key_str, msg, length=100):
    """
    单次加密串的长度最大为 (key_size/8)-11
    1024bit的证书用100， 2048bit的证书用 200
    """
    pub_key_str = '-----BEGIN PUBLIC KEY-----\n' + pub_key_str + '\n-----END PUBLIC KEY-----'
    pubobj = RSA.importKey(pub_key_str)
    pubobj = Cipher_pksc1_v1_5.new(pubobj)
    res = []
    for i in range(0, len(msg), length):
        cont = msg[i:i+length]
        res.append((pubobj.encrypt(cont.encode())))
    # 加密完进行拼接
    cipher_text = b''.join(res)
    # base64进行编码
    result = base64.b64encode(cipher_text)
    return result.decode()


def param_str(_type, page=None):
    en_content = None
    if _type == 'list':
        content = '{"a":"8.0","b":{"a":"65493","actionType":"1.0","b":"795d7759-0c9c-4b54-8638-1b8d28731d38","c":"","d":"","e":"","f":"","g":"应用案例","h":"","i":"","j":"","k":"","l":"推荐","m":"desc","n":"1","o":"10","r":"","strTime":"1652003356844"}}'
    elif _type == 'detail':
        content = '{"a":"8.0","b":{"a":"65493","actionType":"3.0","b":"795d7759-0c9c-4b54-8638-1b8d28731d38","c":"2412","d":"1","strTime":"1652003398720"}}'
    else:
        print('未开发该类型接口')
        return None
    if content:
        en_content = rsa_long_encrypt(pub_key, content, 100)
    return en_content


def case_quote(text):
    new_text = parse.quote(text)
    return new_text


def case_urlencode(text):
    for _r in [
        ['%', '%25'],
        ['\n', '%0A'],
        ['+', '%2B'],
        [' ', '%20'],
        ['/', '%2F'],
        ['?', '%3F'],
        ['#', '%23'],
        ['&amp;', '%26'],
        ['=', '%3D']
    ]:
        text = text.replace(_r[0], _r[1])
    return text


def case_req():
    encode_text = param_str('list')
    urlencode_text = case_urlencode(encode_text)
    info = case_quote(urlencode_text)
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
    case_req()
