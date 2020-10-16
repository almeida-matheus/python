import pymysql

conexao = pymysql.connect (
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'banco_dados' #excluir essa linha para criar banco de dados
)

cursor = conexao.cursor()

comando_sql = "INSERT INTO pessoas (nome,idade,email) VALUES (%s,%s,%s)"
dados = ("jonas","33","jonas@gmail.com")
cursor.execute(comando_sql,dados)

conexao.commit()

#contagem das linhas inseridas
print(cursor.rowcount,"dado inserido com sucesso")