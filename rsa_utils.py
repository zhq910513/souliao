import base64
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pksc1_v1_5
from Crypto.PublicKey import RSA


def encrpt(password, public_key):
    public_key = '-----BEGIN PUBLIC KEY-----\n' + public_key + '\n-----END PUBLIC KEY-----'
    rsakey = RSA.importKey(public_key)
    cipher = Cipher_pksc1_v1_5.new(rsakey)
    password = str(password)  # 密码为int类型时需要转化为str类型
    cipher_text = base64.b64encode(cipher.encrypt(password.encode()))
    return cipher_text.decode()

def decrpt(password, private_key):
    encrypt_text = password.encode('utf-8')
    private_key = '-----BEGIN RSA PRIVATE KEY-----\n' + private_key + '\n-----END RSA PRIVATE KEY-----'
    print(private_key)
    rsakey = RSA.importKey(private_key)
    cipher = Cipher_pksc1_v1_5.new(rsakey)
    text = cipher.decrypt(base64.b64decode(encrypt_text), 1024)
    print(text.decode('utf-8'))
    return text.decode('utf-8')

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

def rsa_long_decrypt(priv_key_str, msg, length=128):
    """
    1024bit的证书用128，2048bit证书用256位
    """
    privobj = RSA.importKey(priv_key_str)
    privobj = Cipher_pksc1_v1_5.new(privobj)
    res = []
    for i in range(0, len(msg), length):
        res.append(privobj.decrypt(msg[i:i+length], 'xyz'))
    return "".join(res)




if __name__ == '__main__':
    pwd = '{"a":"8.0","b":{"a":"65493","actionType":"3.0","b":"795d7759-0c9c-4b54-8638-1b8d28731d38","c":"2412","d":"1","strTime":"1652064519516"}}'
    pub_key = """MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCgVV2WmQVfLUqEgXmcSh6N0d5W\nWjONmiN2UQXwyADctCBBDB8+60zYqH9wpoxhIXxOOyFzr5HzHaKJh22pak/AQBCq\nu06POajBB3Nb/tPt/zHelPytSiAdboeY2jRsW0rgDiKQ1+JEDFHi+yMW7ldcsogp\nsmEhrUkcuE4PzqCYlQIDAQAB"""

    # pwd_key = encrpt(pwd, pub_key)
    # print(pwd_key)

    enres = rsa_long_encrypt(pub_key, pwd, 100)
    print(enres)


