import pymssql





if __name__ == '__main__':
    conn = pymssql.connect(
        host='139.224.237.164',
        # server ='iZs6h9xk7upqn0Z',
        port='1633',
        user='sa',
        password='Sr_hdisdev@20!9',
        database='HDIS_ZHONGSHAN',
        charset ="utf8"
    )
    if conn:
        print("链接成功")
    # conn.close
    cur = conn.cursor()
    print("111111")
    conn.autocommit(True)
    print("2222222")
    sql = "select * from hd_patient where state  = 999 and AREA is not null"
    # sql = sql.replace("","")
    print(sql)
    cur.execute(sql)
    print(type(cur.execute(sql)))
    print("333333333")
    # print(cur.fetchall())
    data1=cur.fetchall()
    # print(data1)
    cur.close()
    # conn.cmmit()
    conn.close()
    print(data1)