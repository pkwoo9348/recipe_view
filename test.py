import pymysql
import time
conn = pymysql.connect(host='database-2.clufoxjoavjk.ap-northeast-2.rds.amazonaws.com', user='admin', password='kpadmin12', db='test', charset='utf8')

sql = "SELECT * FROM recipe "

with conn:
    with conn.cursor() as cur:
        cur.execute(sql)
        result = cur.fetchall()
        for data in result:
            print(data)
            time.sleep(3)
            print('\n')
        