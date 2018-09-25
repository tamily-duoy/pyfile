# -*- coding: UTF-8 -*-
'''
Created on 2018.08.13
@author: sunnydeng
'''
import MySQLdb
import ConfigParser
import sys

def fun2(cursor_dcn,cursor_padm):
    #获取处理日期
    try:
        sql_process_date = "select PROCESS_DATE from TM_SYSTEM_STATUS"
        cursor_dcn.execute(sql_process_date)
        rows = cursor_dcn.fetchall()
        process_date = rows[0][0]
    except:
        print ("error:处理日期获取出错，设置默认值'2024-07-27'")
        process_date = '2024-07-27'

    #根据处理日期，获取dcn中的业务流水号和转账状态（主动还款）
    sql_id_status1 = "select CONSUMER_TRANS_ID,TRANSFER_STATUS from TM_TRANSFER_TRACE where BIZ_DATE='"+str(process_date)+"' and TRANSFER_TYPE='C'"
    cursor_dcn.execute(sql_id_status1)
    rows = cursor_dcn.fetchall()
    for row in rows:
        print ("业务流水号:"+str(row[0])+u",转账状态:"+str(row[1]))
        consumer_trans_id = row[0]
        transfer_status = row[1]

        # 根据业务流水号，获取统一支付还款状态
        try:
            sql_padm="select pay_ret_status from t_deduction where global_busi_transId='"+str(consumer_trans_id)+"'"
            cursor_padm.execute(sql_padm)
            rows = cursor_padm.fetchall()
            pay_ret_status=rows[0][0]
            print ("统一支付还款状态："+str(pay_ret_status))
        except:
            print ("error:统一支付还款状态获取出错")
        else:
            if(transfer_status=='TRAN_SUCC' and pay_ret_status=='PR02'):
                #修改统一支付的状态为成功PR03
                print ("修改统一支付的状态为成功PR03")
                sql_update = "update t_deduction set pay_ret_status='PR03' where global_busi_transId='"+str(consumer_trans_id)+"'"
                cursor_padm.execute(sql_update)

            if (transfer_status == 'TRAN_FAIL' and pay_ret_status == 'PR03'):
                # 修改统一支付的状态为失败PR02
                print ("修改统一支付的状态为失败PR02")
                sql_update = "update t_deduction set pay_ret_status='PR02' where global_busi_transId='"+str(consumer_trans_id)+"'"
                cursor_padm.execute(sql_update)

    # 根据处理日期，获取dcn中的业务流水号和转账状态（自扣）
    sql_id_status2 = "select CONSUMER_TRANS_ID,TRANSFER_STATUS from TM_DD_REG where DD_REQUEST_DATE='" + str(process_date) + "'"
    cursor_dcn.execute(sql_id_status2)
    rows = cursor_dcn.fetchall()
    for row in rows:
        print ("业务流水号:" + str(row[0]) + u",转账状态:" + str(row[1]))
        consumer_trans_id = row[0]
        transfer_status = row[1]

        # 根据业务流水号，获取统一支付还款状态
        try:
            sql_padm = "select pay_ret_status from t_deduction where global_busi_transId='" + str(
                consumer_trans_id) + "'"
            cursor_padm.execute(sql_padm)
            rows = cursor_padm.fetchall()
            pay_ret_status = rows[0][0]
            print ("统一支付还款状态：" + str(pay_ret_status))
        except:
            print ("error:统一支付还款状态获取出错")
        else:
            if (transfer_status == 'TRAN_SUCC' and pay_ret_status == 'PR02'):
                # 修改统一支付的状态为成功PR03
                print ("修改统一支付的状态为成功PR03")
                sql_update = "update t_deduction set pay_ret_status='PR03' where global_busi_transId='"+str(consumer_trans_id)+"'"
                cursor_padm.execute(sql_update)

            if (transfer_status == 'TRAN_FAIL' and pay_ret_status == 'PR03'):
                # 修改统一支付的状态为失败PR02
                print ("修改统一支付的状态为失败PR02")
                sql_update = "update t_deduction set pay_ret_status='PR02' where global_busi_transId='"+str(consumer_trans_id)+"'"
                cursor_padm.execute(sql_update)

def fun1(env):
    # 获取数据库配置参数
    configer = ConfigParser.ConfigParser()
    configer.read("config.ini")

    #dcn1
    Cpsdb1_ip = configer.get(env, "Cpsdb1_ip")
    Cpsdb1_port = configer.getint(env, "Cpsdb1_port")
    Cpsdb1_user = configer.get(env, "Cpsdb1_user")
    Cpsdb1_pswd = configer.get(env, "Cpsdb1_pswd")

    #dcn2
    Cpsdb2_ip = configer.get(env, "Cpsdb2_ip")
    Cpsdb2_port = configer.getint(env, "Cpsdb2_port")
    Cpsdb2_user = configer.get(env, "Cpsdb2_user")
    Cpsdb2_pswd = configer.get(env, "Cpsdb2_pswd")

    #padm
    Padmdb_ip = configer.get(env, "Padmdb_ip")
    Padmdb_port = configer.getint(env, "Padmdb_port")
    Padmdb_user = configer.get(env, "Padmdb_user")
    Padmdb_pswd = configer.get(env, "Padmdb_pswd")

    #连接数据库
    try:
        db_src1 = MySQLdb.connect(host=Cpsdb1_ip,port=Cpsdb1_port,user=Cpsdb1_user,passwd=Cpsdb1_pswd,db='cpsdb',charset='utf8')
        db_src2 = MySQLdb.connect(host=Cpsdb2_ip,port=Cpsdb2_port,user=Cpsdb2_user,passwd=Cpsdb2_pswd,db='cpsdb',charset='utf8')
        db_padm2 = MySQLdb.connect(host=Padmdb_ip, port=Padmdb_port, user=Padmdb_user, passwd=Padmdb_pswd, db='payment_platform_mid_payment',
                                  charset='utf8')
    except:
        print ("error:数据库连接错误")
        sys.exit(0)
    cursor_src_dcn1 = db_src1.cursor()
    cursor_src_dcn2 = db_src2.cursor()
    cursor_src_padm = db_padm2.cursor()

    #调用数据处理函数
    fun2(cursor_src_dcn1,cursor_src_padm)
    fun2(cursor_src_dcn2,cursor_src_padm)

    #提交padm的事务
    db_padm2.commit()

    #关闭游标
    cursor_src_dcn1.close()
    cursor_src_dcn2.close()
    cursor_src_padm.close()

    #关闭数据库连接
    db_src1.close()
    db_src2.close()
    db_padm2.close()

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print ('example: python repaymentStatusCorrectionTool.py F1')
        sys.exit(0)
    s = sys.argv[1]
    fun1(env)