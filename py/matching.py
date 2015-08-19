# -*- coding: utf8 -*-
'''
Created on 2015年8月4日

@author: Administrator
'''
import re
import sys


def getPhoneNumFrom(fobj):
    regex = re.compile(r'1\d{10}', re.IGNORECASE)
    phonenums = re.findall(regex, fobj)
    return phonenums
  
chmap = {  
    '0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,  
    'x':10,'X':10  
    }  
  
def ch_to_num(ch):  
    return chmap[ch]      
  
def verify_string(s):  
    char_list = list(s)  
    num_list = [ch_to_num(ch) for ch in char_list]  
    return verify_list(num_list)  
  
def verify_list(l):  
    sum = 0  
    for ii,n in enumerate(l):  
        i = 18-ii  
        weight = 2**(i-1) % 11  
        sum = (sum + n*weight) % 11  
    return sum==1  
      

if __name__ == '__main__':
    print getPhoneNumFrom('11800138000')[0]
    print '------------------------------------------------------------------------------------'
    result = verify_string('110101122294018')  
    print result