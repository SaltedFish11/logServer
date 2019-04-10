#coding=UTF-8

import random
import re
import time
import traceback
import  sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
os_type = [
    '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)', '(X11; Linux x86_64)',
    '(Macintosh; Intel Mac OS X 10_12_6)', '(iPhone; CPU iPhone OS 12_1_2 like Mac OS X)',
    '(Linux; Android 8.1.0; COL-AL10 Build/HUAWEICOL-AL10; wv)','(iPhone; CPU iPhone OS 11_4_1 like Mac OS X)'
]


status_codes = ["200", "404", "500", "503", "403"]


def sample_url():
    url_paths = [
        "https://www.jd.com/"
    ]
    return url_paths[0]

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
    start='1.1.1.1'
    starts = start.split('.')
    A = int(starts[0])
    B = int(starts[1])
    C = int(starts[2])
    D = int(starts[3])
    A = random.randint(A, 256)
    B = random.randint(B, 256)
    C = random.randint(C, 256)
    D = random.randint(D, 256)

    ip = "%d.%d.%d.%d" %(A, B, C, D)
    if(judge_legal_ip(ip)):
        if ip is None:
            sample_ip()
        else:
            return ip
    else:
        sample_ip()

# 请求时间
def sample_time():
    a1=(2018, 1, 1, 0, 0, 0, 0, 0, 0)              #设置开始日期时间元组（1976-01-01 00：00：00）
    a2=(2019, 6, 31, 23, 59, 59, 0, 0, 0)    #设置结束日期时间元组（1990-12-31 23：59：59）

    start=time.mktime(a1)    #生成开始时间戳
    end=time.mktime(a2)      #生成结束时间戳

    t=random.randint(start,end)    #在开始和结束时间戳中随机取出一个
    date_touple=time.localtime(t)          #将时间戳生成时间元组
    date=time.strftime("[%d/%b/%Y:%H:%M:%S +0800]", date_touple)  #将时间元组转成格式化字符串（1976-05-21）
    return date



def sample_send_byte():
    return random.randint(0,5000)
def sample_referer(cols):
    if random.uniform(0, 1) > 0.2:
        return "-"
    try:
        refer_str = "https://www.jd.com/Search?keyword={query}"
        key = str(cols[random.randint(0,len(cols)-1)]).lstrip()
        split = key.split(' ')[0]
        midd= split.encode('utf-8')
        # query_str = str(key).decode('utf8')
        # print query_str
        res = refer_str.format(query=midd)
        return res
    except Exception, e:
        msg = traceback.format_exc()
        print(msg)
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


def generate_log(cols):
    try:
        f = open("/yang/access.log", "w+")
        count = 0
        while count<100:
            referer = sample_referer(cols=cols)
            query_log = '{ip} - - {date} "{method} {url} HTTP/1.1" {status_code} {send_byte} "{referer}" "{ua}"'.format(
                ip=sample_ip(),  date=sample_time(), method=sample_method(), url=sample_url(), status_code=sample_status_code(),
                send_byte=sample_send_byte(), referer=referer, ua=sample_ua())

            f.write(query_log + "\n")
            count = count + 1
            print query_log
    except Exception, e:
        msg = traceback.format_exc()
        print(msg)
import xlrd

def open_excel(file= 'file.xls'):
    try:
        xlrd.Book.encoding = "gbk"
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))

def excel_table_byname():#修改自己路径
    print "读取文件开始"
    file= './ywr.xlsx'
    # by_name=u'Sheet1'
    data = open_excel(file)
    table = data.sheet_by_index(0) #获得表格
    nrows = table.nrows  # 拿到总共行数
    row = table.col_values(3)

    list=[]
    for rownum in range(0,nrows):

        list.append(row[rownum])
    print "读取文件结束"
    return list

if __name__ =="__main__":
    try:
        cols = excel_table_byname()
        generate_log(cols)
    except Exception, e:
        msg = traceback.format_exc()
        print(msg)