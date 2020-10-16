import pymysql

conexao = pymysql.connect (
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'banco_dados' #excluir essa linha para criar banco de dados
)

cursor = conexao.cursor()

comando_sql = "UPDATE pessoas SET idade = '55' WHERE id = '1'"

cursor.execute(comando_sql)

conexao.commit()

#contagem das linhas inseridas
print(cursor.rowcount,"dado modificado com sucesso")