# -*- coding: utf8 -*-
import datetime
def mainpage():
    current_date = datetime.datetime.now()
    h=int(current_date.strftime("%H") )
    m=int(current_date.strftime("%M") )
    if h<10:
        work = '来的挺早的嘛'
    elif 12> h>=10:
        work = '上午要好好工作'
    elif 13> h>=12:
        work = '中午吃饱了才有力气'
    elif 14> h>=13:
        work = '子曰：中午不睡，下午崩溃'
    elif 19> h>=14:
        work = '漫长的下午 开工！加油！'
    elif 24> h>=19:
        work = '不早了啊  早点回家' 
    return current_date,work