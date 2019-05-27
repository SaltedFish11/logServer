#coding=UTF-8
import urllib
import simplejson
import random
import re
import time
import traceback

os_type = [
    '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)', '(X11; Linux x86_64)',
    '(Macintosh; Intel Mac OS X 10_12_6)', '(iPhone; CPU iPhone OS 12_1_2 like Mac OS X)',
    '(Linux; Android 8.1.0; COL-AL10 Build/HUAWEICOL-AL10; wv)','(iPhone; CPU iPhone OS 11_4_1 like Mac OS X)'
]

ip_pre = ["110.96.","183.63.","27.223.","183.159.","49.95.","180.175.","175.175.","182.143.","115.63.","27.31.","220.191.",
           "223.159.","120.15.","106.95.","223.15.","106.239.","202.203.","223.247.","123.167.","171.111.","122.143.","182.247.",
           "221.197.","123.179.","222.81.","60.165.","114.139.","223.199.","111.113.","223.221.","101.249.","49.246."]



status_codes = ["200", "404", "500", "503", "403"]

# 搜索引擎
http_referers = [
    "http://www.baidu.com/s?wd={query}",
    "https://www.sougou.com/web?query={query}",
    "http://cn.bing.com/search?q={query}",
    "https://search.yahoo.com/search?q={query}"
]

def sample_url():
    url_paths = [
        "class/112.html",
        "class/128.html",
        "class/145.html",
        "class/146.html",
        "class/131.html",
        "class/130.html",
        "learn/821",
        "course/list"
    ]
    return random.sample(url_paths, 1)[0]

# 判断ip是否合法
def judge_legal_ip(one_str):
    '''
    正则匹配方法
    判断一个字符串是否是合法IP地址
    '''
    compile_ip=re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if compile_ip.match(one_str):
        return True
    else:
        return False

# 生成随机ip
def sample_ip():
    # start='1.1.1.1'
    # starts = start.split('.')
    # A = int(starts[0])
    # B = int(starts[1])
    # C = int(starts[2])
    # D = int(starts[3])
    # A = random.randint(A, 256)
    # B = random.randint(B, 256)
    # C = random.randint(C, 256)
    # D = random.randint(D, 256)
    #
    # ip = "%d.%d.%d.%d" %(A, B, C, D)

    ip=random.sample(ip_pre,1)[0]
    ip += ".".join(map(str, (random.randint(0, 255)
                             for _ in range(2))))
    if(judge_legal_ip(ip)):
        if ip is None:
            sample_ip()
        else:
            return ip
    else:
        sample_ip()
# 搜索的课程名字
search_keyword = [
    "Spark SQL实战",
    "Hadoop基础",
    "Storm实战",
    "Spark Streaming实战",
    "大数据面试"
]

# 请求时间
def sample_time():
    a1=(2019, 5, 1, 0, 0, 0, 0, 0, 0)              #设置开始日期时间元组（1976-01-01 00：00：00）
    a2=(2019, 6, 31, 23, 59, 59, 0, 0, 0)    #设置结束日期时间元组（1990-12-31 23：59：59）

    start=time.mktime(a1)    #生成开始时间戳
    end=time.mktime(a2)      #生成结束时间戳

    t=random.randint(start,end)    #在开始和结束时间戳中随机取出一个
    date_touple=time.localtime(t)          #将时间戳生成时间元组
    date=time.strftime("[%d/%b/%Y:%H:%M:%S +0800]", date_touple)  #将时间元组转成格式化字符串（1976-05-21）
    return date



def sample_send_byte():
    return random.randint(0,5000)
def sample_referer():
    if random.uniform(0, 1) > 0.2:
        return "-"

    refer_str = random.sample(http_referers,1)
    query_str = random.sample(search_keyword,1)
    return refer_str[0].format(query = query_str[0])

def sample_status_code():
    return random.sample(status_codes, 1)[0]

def sample_method():
# 请求方法
    request_method = ["GET"]
    return request_method[0]

def sample_ua():
    first_num = random.randint(55, 62)
    third_num = random.randint(0, 3200)
    fourth_num = random.randint(0, 140)

    chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)
    mozilla = ['Mozilla/5.0', 'Mozilla/4.0']
    ua = ' '.join([random.choice(mozilla), 'compatible; MSIE 6.0',random.choice(os_type),  ';AppleWebKit/537.36;',
                   '(KHTML, like Gecko;)', chrome_version, 'Safari/537.36']
                  )
    return ua


def generate_log():

    f = open("/Users/yangwenrui/yang/access.log", "w+")
    count = 0
    while count<1000:
        query_log = '{ip} - - {date} "{method} {url} HTTP/1.1" {status_code} {send_byte} "{referer}" "{ua}"'.format\
         (
            ip=sample_ip(),  date=sample_time(), method=sample_method(), url=sample_url(), status_code=sample_status_code(),
            send_byte=sample_send_byte(), referer=sample_referer(), ua=sample_ua())
        f.write(query_log + "\n")
        count = count + 1
        print query_log


if __name__ =="__main__":
    try:
        generate_log()
    except Exception, e:
        msg = traceback.format_exc()
        print(msg)