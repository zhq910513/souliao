#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author: the king
@file: sl_encrypt.py
@time: 2022/5/8 18:04
"""

import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKC
import rsa
from urllib.parse import urlencode

# Crypto.RSA 加密
def encrypt(plaintext,length=100):
    # 加载公钥
    rsa_key = RSA.import_key(open("D:\Projects\souliao\client_public.pem").read())

    # 加密
    cipher_rsa = Cipher_PKC.new(rsa_key)
    content = plaintext.encode("utf-8")
    if len(content) <= length:
        en_data = cipher_rsa.encrypt(content) # 加密
    else:
        rsa_text = []
        # 对编码后的数据进行切片，原因：加密长度不能过长
        for i in range(0, len(content), length):
            cont = content[i:i + length]
            # 对切片后的数据进行加密，并新增到text后面
            rsa_text.append(cipher_rsa.encrypt(cont))
        # 加密完进行拼接
        en_data = b''.join(rsa_text)

    # base64 进行编码
    base64_text = base64.b64encode(en_data)
    return base64_text.decode() # 返回字符串

# rsa 加密
def rsaEncrypt(plaintext):
    pubkey = rsa.PublicKey(112589984008212718692705259193944372249782211112088510987075898768994940950434990803948711201570710932916881147902507799109684598069324212146298434886616356316597578161839553557185767404108919194503230088104598642071102679172856797188445394861990619673071701814921024243375551997130470844682603957499090475157, 65537)

    # 公钥加密
    en_data = rsa.encrypt(plaintext.encode("utf-8"), pubkey)

    # base64 进行编码
    base64_text = base64.b64encode(en_data)
    return base64_text.decode() # 返回字符串


if __name__ == '__main__':
    content = '{"a":"8.0","b":{"a":"65493","actionType":"3.0","b":"795d7759-0c9c-4b54-8638-1b8d28731d38","c":"2412","d":"1","strTime":"1652064519516"}}'
    en_content = encrypt(content)
    print(en_content)
    print(urlencode(en_content))

    # print(rsaEncrypt(content))