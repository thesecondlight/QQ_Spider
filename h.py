import pymysql.cursors


# 连接MySQL数据库
connection = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='qq_spider',
                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

# 通过cursor创建游标
cursor = connection.cursor()

# 创建sql 语句，并执行
sql = "INSERT INTO `users` (`email`, `password`) VALUES ('huzhiheng@itest.info', '123456')"
cursor.execute(sql)

# 提交SQL
connection.commit()