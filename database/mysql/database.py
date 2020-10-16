import pymysql

conexao = pymysql.connect (
    host = 'localhost',
    user = 'root',
    passwd = ''
)

cursor = conexao.cursor()


#criar banco de dados
#cursor.execute ('CREATE DATABASE banco_dados')

cursor.execute ('SHOW DATABASES')

for x in cursor:
    print(x)

'''
There are thee MySQL adapters for Python that are currently maintained:

mysqlclient - By far the fastest MySQL connector for CPython. Requires the mysql-connector-c C library to work.

PyMySQL - Pure Python MySQL client. According to the maintainer of both mysqlclient and PyMySQL, you should use PyMySQL if:
You can't use libmysqlclient for some reason.
You want to use monkeypatched socket of gevent or eventlet.
You wan't to hack mysql protocol.

mysql-connector-python - MySQL connector developed by the MySQL group at Oracle, also written entirely in Python. It's performance appears to be the worst out of the three. Also, due to some licensing issues, you can't download it from PyPI (but it's now available through conda).
'''