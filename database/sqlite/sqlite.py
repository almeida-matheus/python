import sqlite3
#http://pythonclub.com.br/guia-rapido-comandos-sqlite3.html
#criar o banco de dados
conn = sqlite3.connect('banco.db')
#atraves do cursos digita comando para criar tabela, excluir, adicionar registros
cursor = conn.cursor()
#criar tabela com o nome pessoa
cursor.execute("CREATE TABLE pessoas (nome text,idade integer,email text)")
#inserir dados na tabela
cursor.execute("INSERT INTO pessoas VALUES('Maria',40,'maria@gmail.com')")
#confirmar q esta colocando isso no banco
conn.commit()

'''
#ler o banco de dados
https://sqlitebrowser.org/
#selecionar todos os dados da tabela pessoas
cursor.execute("SELECT * FROM pessoas")
result = cursor.fetchall()
print(result)

user@host:~/$ sqlite usuarios.db
sqlite> select * from usuarios;
'''

#cursor: é um interador que permite navegar e manipular os registros do bd.
#execute: lê e executa comandos SQL puro diretamente no bd.