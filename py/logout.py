# -*- coding: utf8 -*-
import MySQLdb
import cx_Oracle
import matching
import logging
logger = logging.getLogger(__name__)
def lotout(cellphone_no,id_no):
    logger.info("开始匹配手机号和身份证号")
    try:
        return_cellphone_no = matching.getPhoneNumFrom(cellphone_no)
        return_id_no = matching.verify_string(id_no)
        if return_cellphone_no ==[] or return_id_no== False:
            returnresult='手机号或身份证不符合规则'
            logger.info(returnresult)        
            return returnresult
        else:
            id_no = id_no.upper()
            cellphone_no=return_cellphone_no[0]
            logger.info("手机号为： "+cellphone_no+"  身份证号为： "+id_no)
            logger.info("手机号身份证号符合规则，清除开始    "+cellphone_no+'     '+id_no)
            conn_orcl = cx_Oracle.connect('p2p_test_154', '#hu*zAO0lz', '10.106.58.51:1521/test') #yrd 45
            conn_passport = cx_Oracle.connect('passport_test_01', 'gh#c!7jsdNY', '10.106.58.33:1521/test') #passport  
            
#             conn_orcl = cx_Oracle.connect('p2p_test_21', 'h%z8aIACDU0', '10.106.58.42:1521/test') #yrd 45

#             conn_orcl = cx_Oracle.connect('p2p_test_158', '#GH%4LGVR$3BT', '10.106.58.42:1521/test') #yrd 158
# #             conn_passport = cx_Oracle.connect('passport_test_01', 'gh#c!7jsdNY', '10.106.58.33:1521/test') #passport  
#             conn_passport = cx_Oracle.connect('passport_test_02', '^*(0+auZ', '10.106.58.33:1521/test') #passport  
#             conn_passport = cx_Oracle.connect('passport_test_djxt', '*(9jhTaIOZR', '10.106.58.33:1521/test') #passport  
# #             conn_passport = cx_Oracle.connect('passport_test_yfb', '%(K^B*jOQz!q', '10.106.58.33:1521/test') #passport  
  
            conn_mysql=MySQLdb.connect(host="10.106.58.141",user="mobilemoney",passwd="devel@D3rjJpB6",db="mobilemoney",port=3306,charset="utf8")   #mysql
            conn_mysql.select_db('mobilemoney')
            
            cur_orcl=conn_orcl.cursor()
            cur_passport=conn_passport.cursor()
            cur_mysql=conn_mysql.cursor()
            returnresult="" 
            logger.info( "数据库连接完毕")
        
            try:
                logger.info( "查找账户是否存在")
                #row = cur_passport.execute(r"select s.PASSPORT_ID from sso_user s where s.nickname like '"+cellphone_no+"%' or s.login_name like  '%"+cellphone_no+"%'").fetchone ()  
                row1 = cur_orcl.execute(r"select c.I_USER_ID from C_USER_REGIST_INFO c where c.S_MOBILE_ACCOUNT like '%"+cellphone_no+"%'").fetchone ()
                
                row2 = cur_orcl.execute(r"select b.I_USER_ID from b_basic_info b where  b.s_id_card like '%"+id_no+"'").fetchone ()
                row3 = cur_orcl.execute(r"select li.IUSER_ID  from lender_info li where  li.sid_card like '%"+id_no+"%'").fetchone ()
                
                if row1 == None :#or row == None:
                    if row1 == None:
                        returnresult = "C_USER_REGIST_INFO没有该条数据"
                   # else:
                        #returnresult = "PASSPORT_sso_user没有该条数据"
                    logger.info(returnresult)
                    return returnresult
                else:
                    logger.info("查找手机号与身份证是否匹配")
                    b = row1[0]
                    print b
                    if row2== None:
                        USER_ID = row3[0]
                    else:
                        USER_ID = row2[0]
                    if b != USER_ID:
                        logger.info("C_USER_REGIST_INFO中USER_ID为"+b)
                        logger.info("lender_info或b_basic_info中USER_ID为"+USER_ID)
                        returnresult = '手机号与身份证不符合'
                        logger.info(returnresult)
                        return returnresult
                    else:
                        
                        #--宜人贷数据库   
                        #passport_id = row[0]
                        cur_orcl.execute(r"update C_USER_REGIST_INFO c set S_CNNAME='11111111111' ,S_NICK_NAME='1',S_MOBILE_ACCOUNT='11111111111'  where c.S_MOBILE_ACCOUNT = '"+cellphone_no+"'")
                        cur_orcl.execute(r"update VERIFY_MOBILE_NUMBER_T VMN set NEW_MOBILE_NUMBER='1',OLD_MOBILE_NUMBER='1'  where vmn.NEW_MOBILE_NUMBER = '"+cellphone_no+"'")
                        logger.info("清除宜人贷数据库")
                        #借款、出借人身份证信息
                        cur_orcl.execute(r"update  b_basic_info b set S_ID_CARD='1',S_CUSTTOMER_NAME='1',C_MOBILE='1'  where b.s_id_card = '"+id_no+"'")
                        cur_orcl.execute(r"update  lender_info li set SLENDER_NAME='1',SID_CARD='1',SMOBILE='1' where  li.sid_card = '"+id_no+"'")
                        logger.info("清除借款、出借人身份证信息 ")
                        #开户信息
                        cur_orcl.execute(r"update  user_account_bank_info u set USER_NAME='1',ID_CARD_NO='1',BANK_ACCOUNT_NO='1'  where  u.id_card_no = '"+id_no+"'")
                        logger.info("清除开户信息 ")
                        #修改passport中的信息
                        #cur_passport.execute(r"update sso_user set nickname='1' where passport_id='"+passport_id+"'")
                        #cur_passport.execute(r"update sso_user set login_name='1' where passport_id='"+passport_id+"'")
                        #cur_passport.execute(r"update sso_userex set mobile='1'  where passport_id='"+passport_id+"'")
                        #logger.info("清除passport中的信息")
                        #删除宜定赢中的用户信息
                        cur_mysql.execute("delete from t_p2puser where MOBILE_NO='"+cellphone_no+"'")
                        cur_mysql.execute("delete from t_p2puser where ID_CARD_NO='"+id_no+"'")
                        logger.info("清除宜定赢中的用户信息")
                        
                        logger.info( "oracle版本为"+conn_orcl.version)
                        returnresult='成功'
                        logger.info("清除成功")
            except Exception,ex: 
                returnresult = "查找账户不存在" 
                
            conn_orcl.commit()
            conn_passport.commit()
            conn_mysql.commit()
            
            cur_orcl.close()
            cur_passport.close()
            cur_mysql.close()
            
            conn_orcl.close()
            conn_passport.close()
            conn_mysql.close()

    except Exception,ex:
        returnresult = ex 
    return returnresult
if  __name__ == '__main__':
    #print 1
    #print '61012419860913721x'.upper()
#     a=  lotout("18682493128","61012419860913721X")
    a=  lotout("13058041296","430821199108035122")
    print a
# 17755555551  370211197607180016 王涛
#"郝明月",          "21100319841010364X",           "6222000200117749002"                    17700000001