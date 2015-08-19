# -*- coding: utf-8 -*-
'''
Created on 2015年7月24日

@author: mrlong
'''
import urllib2
import json
def download_bing():
    url= r'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=16'
    djson = json.loads(urllib2.urlopen(url).read())
    pic_url0 = {'url':djson['images'][0]['url'],'copyright':djson['images'][0]['copyright'],'copyrightlink':djson['images'][0]['copyrightlink']}
    pic_url = []
    for i in range(1,6):
        dic= {'url':djson['images'][i]['url'],'copyright':djson['images'][i]['copyright'],'copyrightlink':djson['images'][i]['copyrightlink']}
        pic_url.append(dic)
    return pic_url0,pic_url

def download_weather():
    url= r'http://www.weather.com.cn/data/101010100.html'
    djson = json.loads(urllib2.urlopen(url).read())
    print djson['weatherinfo']['city']
    print 1
    

if  __name__ == '__main__':
    download_weather()
  
    