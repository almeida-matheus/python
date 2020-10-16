import pymysql

conexao = pymysql.connect (
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'banco_dados' #excluir essa linha para criar banco de dados
)

cursor = conexao.cursor()

#criar tabela no banco de dados
#cursor.execute ("CREATE TABLE pessoas(nome VARCHAR(255),idade INT(3),email VARCHAR(255))")

#adicionar coluna na tabela
#cursor.execute("ALTER TABLE pessoas ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#remover tabela do banco de dados
#cursor.execute("DROP TABLE nome_tabela")

cursor.execute("SHOW TABLES")

for x in cursor:
    print (x)