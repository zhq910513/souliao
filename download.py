#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author: the king
@project: zyl_company
@file: download.py
@time: 2022/4/21 14:17
"""
import hashlib
import os
import time
from multiprocessing.pool import ThreadPool
from os import path

import requests

from common.log_out import log_err
from dbs.pipelines import MongoPipeline

requests.packages.urllib3.disable_warnings()

picHeaders = {
    'accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': '27.150.182.135:8855',
    'Origin': 'http://8.129.215.170:8855',
    'Pragma': 'no-cache',
    'Referer': 'http://8.129.215.170:8855/swagger-ui.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
}
videoPageHeaders = {
    'authority': 'v.jin10.com',
    'method': 'GET',
    'path': '/details.html?id=12574',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
}

image_base_path = path.dirname(os.path.abspath(path.dirname(__file__)))


# 下载/上传 图片/视频 函数
def DownloadPicture_Video(img_path, img_info: tuple, retry=0):
    img_name = img_info[0]
    img_url = img_info[1]
    if img_url and img_url.endswith('.jpg') or img_url.endswith('.png') or img_url.endswith('.pdf') or img_url.endswith(
            '.wbep'):
        try:
            res = requests.get(img_url, timeout=60)
            if res.status_code == 200:
                basename = img_name + '.' + img_url.split('.')[-1]
                filename = os.path.join(img_path + '/' + basename)
                with open(filename, "wb") as f:
                    content = res.content
                    f.write(content)
        except requests.exceptions.ConnectionError:
            print(f'下载图片网络问题，重试中...  {img_url}')
            if retry < 3:
                return DownloadPicture_Video(img_path, img_url, retry + 1)
        except Exception as error:
            log_err(error)
            return None
        return None
    elif img_url and img_url.endswith('.mp4') or img_url.endswith('.avi') or img_url.endswith(
            '.wmv') or img_url.endswith('.mpeg') or img_url.endswith('.flv') or img_url.endswith(
            '.m4v') or img_url.endswith('.mov'):
        try:
            res = requests.get(img_url, timeout=60)
            if res.status_code == 200:
                basename = hashlib.md5(img_url.encode("utf8")).hexdigest() + '.' + img_url.split('.')[-1]
                filename = os.path.join(img_path + '/' + basename)
                with open(filename, "wb") as f:
                    content = res.content
                    f.write(content)
        except requests.exceptions.ConnectionError:
            print(f'下载视频网络问题，重试中...  {img_url}')
            if retry < 3:
                return DownloadPicture_Video(img_path, img_url, retry + 1)
        except Exception as error:
            log_err(error)
            return None
        return None
    else:
        pass


# 多线程处理数据
def command_thread(company_name, _id, image_list, Async=True):
    thread_list = []
    # 设置进程数
    pool = ThreadPool(processes=8)

    for img_info in image_list:
        file_path = f'D:/Projects/souliao/download_data/{company_name}/{_id}'
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        if Async:
            out = pool.apply_async(func=DownloadPicture_Video, args=(file_path, img_info,))  # 异步
        else:
            out = pool.apply(func=DownloadPicture_Video, args=(file_path, img_info,))  # 同步
        thread_list.append(out)
        # break
    pool.close()
    pool.join()

    MongoPipeline('case_detail').update_item({'id': None}, {'id': _id, 'status': 2})


def run():
    infos = MongoPipeline('case_detail').find({'status': 1})
    for info in infos:
        imgs = []
        imgs_info = []
        if info.get('litpic'):
            if str(info.get('litpic')).startswith('/news'):
                img_url = 'https://www.soliao.com' + info.get('litpic')
            elif str(info.get('litpic')).startswith('https://www.soliao.com'):
                img_url = info.get('litpic')
            else:
                print(f"图片链接异常：{info.get('litpic')}")
                img_url = None
            if img_url:
                img_name = img_url.split('/')[-1].split('.')[0]
                imgs.append(img_url)
                imgs_info.append((img_name, img_url))

        if info.get('b'):
            if info.get('b').get('g') and isinstance(info.get('b').get('g'), dict):
                if info.get('b').get('g').get('fileName'):
                    if str(info.get('b').get('g').get('fileName')).startswith('/news'):
                        img_url = 'https://www.soliao.com' + info.get('b').get('g').get('fileName')
                    elif str(info.get('b').get('g').get('fileName')).startswith('https://www.soliao.com') or str(info.get('b').get('g').get('fileName')).startswith('http://www.soliao.com'):
                        img_url = info.get('b').get('g').get('fileName')
                    elif '.pdf' in info.get('b').get('g').get('fileName'):
                        img_url = 'https://slfiles.soliao.com/soliao/case/other/' + info.get('b').get('g').get('fileName')
                    else:
                        img_url = None
                        print(f"图片链接异常：{info.get('b').get('g').get('fileName')}")
                    if img_url:
                        name = str(info.get('title')).replace('\n', '').replace('\t', '').replace('\r', '').replace('/', '').strip()
                        img_name = f"搜料网-案例-{name}"
                        imgs.append(img_url)
                        imgs_info.append((img_name, img_url))

            if info.get('b').get('i') and isinstance(info.get('b').get('i'), list):
                for img in info.get('b').get('i'):
                    if str(img).startswith('/news'):
                        img_url = 'https://www.soliao.com' + img
                    elif str(img).startswith('https://www.soliao.com') or str(img).startswith('http://www.soliao.com'):
                        img_url = img
                    else:
                        print(f"图片链接异常：{img}")
                        img_url = None
                    if img_url:
                        img_name = img_url.split('/')[-1].split('.')[0]
                        imgs.append(img_url)
                        imgs_info.append((img_name, img_url))

        print(imgs_info)
        command_thread('souliao', info['id'], imgs_info, Async=True)
        time.sleep(1)
        # break



if __name__ == '__main__':
    while True:
        run()
