import pymysql

conexao = pymysql.connect (
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'banco_dados' #excluir essa linha para criar banco de dados
)

cursor = conexao.cursor()
#cursor.execute("SELECT * FROM pessoas")
#cursor.execute("SELECT nome,idade FROM pessoas")
#cursor.execute("SELECT * FROM pessoas WHERE idade = '44'")

#ordenar info desc=decrescente
cursor.execute("SELECT * FROM pessoas ORDER BY idade DESC")


#fazer a busca por todas as informacoes dos dados da tabela
resultado = cursor.fetchall()

print(resultado[1])

for x in resultado:
    print(x)