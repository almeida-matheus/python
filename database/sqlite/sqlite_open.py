import sqlite3

banco = sqlite3.connect('passwords.db')

cursor = banco.cursor()

cursor.execute('SELECT * FROM users')

result = cursor.fetchall()

x = open('result_sqlite','w')

for item in result:
    print(item[0])

    #x.writelines(item[1]+'\n')
#x.close()
#banco.close()