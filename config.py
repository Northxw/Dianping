# -*- coding:utf-8 -*-

from fake_useragent import UserAgent
import random

API = 'http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=cavnkfabvajfhv12fa1v4fv12g1ba2b1gsgb&orderno=vanfjvadfb1sg5b4s4bf4b1s2n&returnType=2&count=1'

INIT_URL = 'http://www.dianping.com/beijing/ch10/p{}'
CSS_URL = 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/f8198800680006c0424b3c7412023ee7.css'
SVG_NUM_URL = 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/20b501902c483d49e1e66d2159f1d2b8.svg'
SVG_FONT_URL = 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/37b6ad50c87b9ec0e1744f4291efb622.svg'

MAX_PAGES = 20

# 获取随机UA
with open('./utils/ua.log', 'r', encoding='utf-8') as f:
    random_ua = random.choice(f.read().split('\n'))

HEADERS = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
            'Cache-Control': 'max-age=0',
            'Host': 'www.dianping.com',
            'Referer': 'http://www.dianping.com/beijing/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': random_ua,
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
            # "Proxy-Tunnel": str(random.randint(1,10000))  # 使用亿牛云代理时需设置
}

# 阿布云
PROXY_HOST = "http-dyn.abuyun.com"
PROXY_PORT = "9020"
PROXY_USER = 'HL3E438N64G79I6D'
PROXY_PASS = 'C54E0F0C2E3EC0DE'

# 亿牛云
NIU_PROXY_HOST = 'p5.t.16yun.cn'
NIU_PROXY_PORT = '6445'
NIU_PROXY_USER = 'SASDV58VF'
NIU_PROXY_PASS = 'Vf5v21vF'

DEFAULT_STAR = '三星级商户'
DEFAULT_NAME = 'Unnamed'
DEFAULT_NUM = 10

MONGO_CLIENT = 'mongodb://localhost:27017'