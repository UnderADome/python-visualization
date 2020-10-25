import xlrd
from xlrd import xldate_as_tuple #用于转换时间格式
from datetime import date, datetime #用于标准化时间

book = xlrd.open_workbook(r"C:\WISDRI\Heatflux\Excel.xls")
sheet = book.sheets()[0] #获取文件中的第一个表
std = [] #定义一个空列表，准备存放后面将要读到的数据
for i in range(1, sheet.nrows): #一行一行遍历数据，sheet.nrows为excel中数据的总行数
    #因为数据被读取后，数据的格式会发生变化，所以下面要把数据的格式转换以下
    temp = sheet.row_values(i) #获取第i行的数据
    #数据读出时，整形、时间类型都变成了浮点数，所以需要进行格式转换
    print(temp[0], temp[1])
    # temp[0] = date(*xldate_as_tuple(temp[0], book.datemode)[:3]).strftime('%Y-%m-%d')
    std.append(tuple(temp))

import pymysql
#处理数据库
conn = pymysql.connect(host='localhost', user='root', passwd='root', db='heatload_v2', charset='utf8')
cur = conn.cursor()
sql = 'insert into HeatloadAndThickness(id, coolingwall_id, writetime, t0) values(null, 20, %s, %s);'
cur.executemany(sql, std) #执行多行插入
conn.commit()
cur.close()
conn.close()

