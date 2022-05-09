import time
from urllib import parse
import base64
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pksc1_v1_5
from Crypto.PublicKey import RSA
import requests
from common.log_out import log_err
from dbs.pipelines import MongoPipeline


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


def param_str(_type, param):
    en_content = None
    if _type == 'list':
        content = '{"a":"8.0","b":{"a":"65493","actionType":"1.0","b":"795d7759-0c9c-4b54-8638-1b8d28731d38","c":"","d":"","e":"","f":"","g":"应用案例","h":"","i":"","j":"","k":"","l":"推荐","m":"desc","n":"' + str(param) + '","o":"10","r":"","strTime":"' + str(int(time.time()*1000)) + '"}}'
    elif _type == 'detail':
        content = '{"a":"8.0","b":{"a":"65493","actionType":"3.0","b":"795d7759-0c9c-4b54-8638-1b8d28731d38","c":"' + str(param) + '","d":"1","strTime":"' + str(int(time.time()*1000)) + '"}}'
    elif _type == 'download':
        content = '{"a":"5.0","b":{"a":"65493","actionType":"7.0","b":"795d7759-0c9c-4b54-8638-1b8d28731d38","c":"' + str(param) + '","strTime":"' + str(int(time.time()*1000)) + '"}}'
    else:
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


def case_req(_type, page=1):
    encode_text = param_str(_type, page)
    if not encode_text:
        print('--- 解码失败 ---')
        return

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
    if save_case(_type, page, resp.json()):
        if _type == 'list':
            time.sleep(5)
            return case_req(_type, page+1)


def save_case(_type, page, data_json):
    try:
        if _type == 'list':
            if data_json.get('a').get('infoName') == '获取案例列表数据成功！':
                data_json['hash_key'] = f'{_type}_{page}'
                MongoPipeline('case_list').update_item({'hash_key': None}, data_json)

                if data_json.get('b').get('j') and isinstance(data_json.get('b').get('j'), list):
                    print(f"正在请求第 {page} 页， 共 {len(data_json.get('b').get('j'))} 条数据")
                    for info in data_json.get('b').get('j'):
                        info['hash_key'] = f'{_type}_{page}'
                        MongoPipeline('case_detail').update_item({'id': None}, info)
                    return True
                else:
                    return False
            else:
                log_err(data_json.get('a').get('infoName'))
        if _type == 'detail':
            if data_json.get('a').get('infoName') == '获取案例详情内容成功':
                print(f'{page} 获取案例详情内容成功')
                data_json['id'] = str(page)
                data_json['status'] = 1
                MongoPipeline('case_detail').update_item({'id': None}, data_json)
                return False
    except Exception as error:
        log_err(error)


if __name__ == '__main__':
    infos = MongoPipeline('case_detail').find({'status': None})
    for info in infos:
        case_req('detail', info['id'])
        time.sleep(3)

    # case_req('detail', 2412)