import os

import pymssql

from common import logger
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 寻找setting.ini文件
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
# 读取 setting.ini文件中sqlserver标识下的内容
data = data.load_ini(data_file_path)["sqlserver"]

DB_CONF = {
    "host":data["SQLSERVER_HOST"],
    "port":data["SQLSERVER_PORT"],
    "user":data["SQLSERVER_USER"],
    "password":data["SQLSERVERL_PASSWD"],
    "database":data["SQLSERVER_DB"],
    "charset":data["SQLSERVER_CHARSET"]
}

class SqserverDb():
    def __init__(self,db_conf=DB_CONF):
        # 通过字典拆包传递配置信息，建立数据库连接
        try:
            self.conn = pymssql.connect(**db_conf)
            if self.conn:
                print("数据库链接成功")
            self.cur = self.conn.cursor()
        except Exception as e:
            print(e)


    def __del__(self):
        try:
            # 关闭游标
            self.cur.close()
            # 关闭数据库链接
            self.conn.close()
        except Exception as e:
            print(e)

    def select_db(self,sql):
            # 执行sql
            self.cur.execute(sql)
            results = self.cur.fetchall()
            return results

    def execute_db(self,sql):
        # 更新/新增/删除
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            logger.info("操作SQL SERVER出现错误，错误原因：{}".format(e))
            self.conn.rollback()

db = SqserverDb(DB_CONF)

if __name__ == '__main__':
    # aa ='select COUNT(*) from hd_patient'
    # print(db.select_db(aa))
    # print(BASE_PATH)
    # print(data_file_path)
    # print(data)
    # print("++++++++++++++")
    # print(type(DB_CONF))
    # print(DB_CONF)
    # print(SqserverDb())

    sql = "select * from hd_patient where state  = 999 and AREA is not null"
    print(db.select_db(sql))
    sql01 ="update hd_patient set state = 1 where state  = 999 and AREA is not null"
    sql02 ="update hd_patient set STATE = 999 where id = '0a3d5fe2-92d3-4799-81a2-99ab82afb323' or id = 'f0f0fd6d-df93-48b9-bd37-ba577a1461ad'"
    sql03 = "select state from hd_patient where id = '0a3d5fe2-92d3-4799-81a2-99ab82afb323' or id = 'f0f0fd6d-df93-48b9-bd37-ba577a1461ad'"
    print(db.execute_db(sql01))
    print(db.execute_db(sql02))
    print(db.select_db(sql03))
