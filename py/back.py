# -*- coding: utf8 -*-

#恢复旧账户
import MySQLdb
import cx_Oracle


#只需要改手机号，按F5执行，提示保存按OK就行，都是蓝字就是成功，有红字就说明没有该账户
cellphone_no = '15600212263'






print cellphone_no
conn_orcl = cx_Oracle.connect('p2p_test_45', '#hu*zAO0lz', '10.106.58.42:1521/test') #yrd
conn_mysql=MySQLdb.connect(host="10.106.4.102",user="mobilemoney",passwd="devel@D3rjJpB6",db="mobilemoney",port=3306,charset="utf8")   #mysql
conn_mysql.select_db('mobilemoney')

cur_orcl=conn_orcl.cursor()
cur_mysql=conn_mysql.cursor()



cursor = cur_mysql.execute(r"select P2PUSER_ID from t_p2puser where MOBILE_NO = '"+cellphone_no+"'")
print cursor 
P2PUSER_ID = cur_mysql.fetchall()[0][0]
print P2PUSER_ID

sql1 = "update C_USER_REGIST_INFO c set S_CNNAME='"+cellphone_no+"',S_NICK_NAME='"+cellphone_no+"',S_MOBILE_ACCOUNT='"+cellphone_no+"'where c.I_USER_ID = '"+P2PUSER_ID+"'"
print sql1
sql2 = "update VERIFY_MOBILE_NUMBER_T VMN set NEW_MOBILE_NUMBER='"+cellphone_no+"'  where vmn.USER_ID = '"+P2PUSER_ID+"'"
print sql2

print cur_orcl.execute(sql1)
print cur_orcl.execute(sql2)


conn_orcl.commit()
conn_mysql.commit()
    
cur_orcl.close()
cur_mysql.close()
    
conn_orcl.close()
conn_mysql.close()
 
