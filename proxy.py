# -*- coding:utf-8 -*-

import requests
from config  import *

def xdaili_proxy():
    results = requests.get(url=API).json()['RESULT']
    agents = ['http://{}:{}'.format(res['ip'], res['port']) for res in results]

    # 测试
    # headers = {
    #             'Host': 'www.dianping.com',
    #             'Upgrade-Insecure-Requests': '1',
    #             'User-Agent': UserAgent().random,
    # }

    proxies = {
        "http": random.choice(agents),
        "https": random.choice(agents)
    }
    return proxies
    # response = requests.get(url='http://www.dianping.com/xian/ch10/p1', headers=headers, proxies=proxies)
    # print(response.text)

def general_proxy():
    # 代理服务器
    proxyHost = PROXY_HOST
    proxyPort = NIU_PROXY_PORT

    # 代理隧道验证信息
    proxyUser = NIU_PROXY_USER
    proxyPass = NIU_PROXY_PASS

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "user": proxyUser,
        "pass": proxyPass,
        "host": proxyHost,
        "port": proxyPort,
    }

    proxies = {
        "http": proxyMeta,
        "https": proxyMeta,
    }
    return proxies

if __name__ == '__main__':
    # print(xdaili_proxy())
    pass