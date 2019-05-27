# coding=utf-8

import random
import re
import time
import traceback
# 请求时间

def sample_time():
    a1=(2018, 5, 1, 0, 0, 0, 0, 0, 0)
    a2=(2019, 6, 31, 23, 59, 59, 0, 0, 0)

    start=time.mktime(a1)    #生成开始时间戳
    end=time.mktime(a2)      #生成结束时间戳

    t=random.randint(start,end)    #在开始和结束时间戳中随机取出一个
    date_touple=time.localtime(t)          #将时间戳生成时间元组
    date=time.strftime("[%d/%b/%Y:%H:%M:%S +0800]", date_touple)  #将时间元组转成格式化字符串（1976-05-21）
    return date



def generate_log():

    f = open("/Users/yangwenrui/yang/access.log", "w+")
    count = 0
    company = []
    for pro in
        query_log = '{company} {city} {name} {price} {time} {age} {work} {address} {traffic}'.format(
            company=sample_pro(),  city=sample_time(), method=sample_method(), url=sample_url(), status_code=sample_status_code(),
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