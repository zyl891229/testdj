# -*- coding: utf8 -*-
'''
Created on 2015年7月24日

@author: Administrator
'''

def nav_search(dict,query):
    #dict = {1:"华为科技技术有限公司",2:"中兴通讯有限公司",3:"华为通讯技术公司",4:"中国移动",5:"华为科技研究院"}
    keys = [x[0] for x in dict.items() if query in x[1]]
    return keys


