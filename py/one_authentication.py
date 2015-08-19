# -*- coding: utf8 -*-
'''
Created on 2015年8月4日

@author: Administrator
'''
import MySQLdb
import cx_Oracle

def one_authentication(bank_card_no):
    print bank_card_no
    conn_paycenter = cx_Oracle.connect('paycenter_srv_test_158', '#GH%4LGVR$3BT', '10.106.58.33:1521/test') #yrd
    conn_mysql=MySQLdb.connect(host="10.106.4.102",user="mobilemoney",passwd="devel@D3rjJpB6",db="mobilemoney",port=3306,charset="utf8")   #mysql
    conn_mysql.select_db('mobilemoney')
    cur_paycenter=conn_paycenter.cursor()
    cur_mysql=conn_mysql.cursor()
    #returnresult=''        
    sql1 = r"select * from auth_records t where t.BANK_CARDNO='"+bank_card_no+"'"
    sql2 = r"update auth_records ti set IS_DEL='0'  where ti.BANK_CARDNO='"+bank_card_no+"'"
    sql3 = r"delete from t_user_bank where BANK_CARD_NO='"+bank_card_no+"'"
    print  sql1,sql2,sql3
    row = cur_paycenter.execute(sql1).fetchall()
    print row[0]
    print cur_paycenter.execute(sql2)
    print cur_mysql.execute(sql3)
    return True

    cur_paycenter.commit()
    conn_mysql.commit()
    cur_paycenter.close()
    cur_mysql.close()
    cur_paycenter.close()
    conn_mysql.close()
        
if  __name__ == '__main__':
    one_authentication('6214830118056125')
    #one_authentication('6214830118056125')