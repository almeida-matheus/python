import pymysql

conexao = pymysql.connect (
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'banco_dados' #excluir essa linha para criar banco de dados
)

cursor = conexao.cursor()

comando_sql = "DELETE FROM pessoas WHERE id = '4'"

cursor.execute(comando_sql)

conexao.commit()

#contagem das linhas inseridas
print(cursor.rowcount,"dado deletado com sucesso")