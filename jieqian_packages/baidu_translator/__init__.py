#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.0.1"

import requests
import random
import json
from hashlib import md5

# API id & key
# CJQ free API. QFS = 10
CJQappid = '20201031000603669'
CJQappkey = 'pAIVFQbeR9MnBNl84mcJ'

# YYQ free API: PFS = 1
YYQappid = '20211214001028669'
YYQappkey = 'kKq52WMWJZyjedOidsKw'

# CYM free API: PFS = 1
CYMappid = '20220309001117956'
CYMappkey = '68NTmKwlDwUpr7WPw2xD'

# ZJP free API: PFS = 1
ZJPappid = '20220309001117968'
ZJPappkey = 'yyqxgrS1_pnfE130ex42'

# LQY free API: PFS = 1
LQYappid = '20210325000741519'
LQYappkey = '07ShQBO1pandi4DLV3sU'

appid_ls = [
    CJQappid,
    YYQappid,
    CYMappid,
    ZJPappid,
    LQYappid
]

appkey_ls = [
    CJQappkey,
    YYQappkey,
    CYMappkey,
    ZJPappkey,
    LQYappkey
]

#
endpoint = 'http://api.fanyi.baidu.com'
path = '/api/trans/vip/translate'
url = endpoint + path


def translator(src, direction='auto2zh', out_type="res"):
    # 调用次数变量控制循环使用列表中的 appid，提高 PFS
    id_no = translator.call_number
    appid = appid_ls[id_no % len(appid_ls)]
    appkey = appkey_ls[id_no % len(appid_ls)]
    # print(id_no % len(appid_ls))
    # print(appid)
    translator.call_number += 1
    # print(translator.call_number)

    # src change to string
    if type(src) is str:
        str_src = src
    elif type(src) is list:
        str_src = ''
        for li in src:
            str_src += li + '\n'
    else:
        print('src type not spported translate.')
        return None

    # Generate salt and sign
    def make_md5(s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + str_src + str(salt) + appkey)

    # Build request
    headers = {
        'Content-Type': 'application/baidu_translator'
    }
    payload = {
        'appid': appid,
        'q': str_src,
        'from': direction.split('2')[0],
        'to': direction.split('2')[1],
        'salt': salt,
        'sign': sign,
        'action': 1,
    }

    try:
        res = []
        if out_type == 'dual':
            r = requests.post(url, params=payload, headers=headers)
            result = r.json()
            # print(result)
            for ri in range(len(result['trans_result'])):
                res.append(result['trans_result'][ri]['src'])
                res.append(result['trans_result'][ri]['dst'])
        elif out_type == 'res':
            r = requests.post(url, params=payload, headers=headers)
            result = r.json()
            for ri in range(len(result['trans_result'])):
                res.append(result['trans_result'][ri]['dst'])
        else:
            for ri in range(len(src.splitlines())):
                res.append(src.splitlines()[ri])
        return res
    except:
        print('request outtime')


# call_number 记录调用次数，循环使用上述 API，突破 PFS = 1 为 PFS = len(appid_ls)
translator.call_number = 0

if __name__ == '__main__':
    # test code: 测试循环调用不同 appid 的效果，OK
    src_ls = ['This is a test sentence.', 'I am a translator using BaiduApi.']
    src_str = 'Python is a perfect programming language.'
    print(translator(src_ls))
    print(translator.call_number)
    print(translator(src_str))
    print(translator.call_number)
    print(translator(src_ls))
    print(translator.call_number)
    print(translator(src_str))
    print(translator.call_number)
    print(translator(src_ls))
    print(translator.call_number)
    print(translator(src_str))
    print(translator.call_number)
    print(translator(src_ls))
    print(translator.call_number)
    print(translator(src_str))
    print(translator.call_number)
