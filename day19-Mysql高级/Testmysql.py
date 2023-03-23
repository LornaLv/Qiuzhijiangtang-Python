# Date: 2023/3/23 下午1:42
# 创建数据库的连接
from pymysql import *

conn = connect(host='localhost', user='root', password='1', database='study', charset='utf8')

# 创建一个游标对象 可以利用这个对象进行数据库的操作
try:
    cur = conn.cursor()

    '''插入数据'''
    # insertsql='''
    # insert into students(name) values ('小笼包')
    # '''
    # cur.execute(insertsql)
    # conn.commit()

    '''读取数据'''
    # cur.execute('select * from students where id=%s', [100])
    cur.execute('select * from students')
    result = cur.fetchall()
    for item in result:
        print(f'姓名：{item[1]}\t性别：{item[2]}\t地址：{item[3]}\t班级：{item[4]}\t年龄：{item[5]}')
    print('success')

except Exception as ex:
    print(ex)
finally:
    cur.close()
    conn.close()
