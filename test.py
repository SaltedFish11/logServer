
if __name__=="__main__":
    refer_str = "https://www.jd.com/Search?keyword={query}"
    query_str = str(" 西部数据（WD） My Passport  Ultra USB3.0 1TB 超便携移动硬盘 （黑色）WDBZFP0010BBK-PESN ").encode('utf8')
    print refer_str.format(query=query_str)