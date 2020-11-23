import sqlite3
#import getpass
#banco de dados relaciona q usa sql, ele cria um arquivo q o python pode acessar usando o sqlite.3connect
MASTER_PASSWORD = '123456'
#cursor: é um interador que permite navegar e manipular os registros do bd.
#execute: lê e executa comandos SQL puro diretamente no bd.
senha = input('insira a senha principal: ')
#senha = getpass.getpass(prompt='insira sua senha:', stream=None)

if senha != MASTER_PASSWORD:
    print('senha inválida')
    exit()
#conecta a um banco sqlite
conn = sqlite3.connect('passwords.db') #'c:/sqlite/aula/estudo.db' ('/root/arquivo.txt') ('c:\\windows\\arquivo.txt') # 2 barras representam 1 barra
#definindo um cursor
cursor = conn.cursor() #atribuir oq quer receber como resposta
#criar a tabela caso users nao exista(schema)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')

def menu():
    print('***************************')
    print(' i : inserir nova senha')
    print(' l : listar serviços salvos')
    print(' r : recuperar senha')
    print(' s : sair')
    print('****************************')

#executar um select no banco de dados para buscar user e password
#e buscar por serviço, unica coisa q  vc tem q saber para usar o programa é o serviço q vc quer pegar a senha
def get_password(service): #funcao para pegar a senha
        cursor.execute(f'''
            SELECT username, password FROM users
            WHERE service = '{service}'
        ''')
        rows = cursor.fetchall()
        qnt_results = (len(rows))
#se o numero de resultados q retornar for 0 quer dizer q nao tem nada com aquele nome de serviço
        if qnt_results == 0: #cursor.rowcount == 0:
            print('servico não cadastrado (use l para verificar os serviços)')
        else: #se nao mostro os resultados em tuplas cadastradas / mostra todos os usuarios
            for user in rows:
                print(user)
#inserir senhas
#dado o s, u, p eu faço inset no banco de dados e commit
def insert_password(service, username, password): #funcao para inserir novo serviço
    cursor.execute(f'''
        INSERT INTO users (service, username, password)
        VALUES('{service}', '{username}', '{password}')
    ''')
    conn.commit()
#pra mostrar tem que fazer um select
#mostrando um serviço pra pesquisar por um serviço, dado ele vou mostrar a senha dele usando o r
def show_services(): #função para mostrar todos os serviços
    cursor.execute('''
        SELECT service FROM users;
        ''')
    for service in cursor.fetchall():
        print(service)

while True:
    menu()
    op = input('opção selecionada: ')
    if op not in ['i', 'l', 'r', 's']:
        print('opção inválida')
        print('\n')
        continue

    if op == 's':
        break

    if op == 'i':
        service = input('qual o nome do serviço? ')
        username = input('qual o nome do usuario? ')
        password = input('qual a senha? ')
        insert_password(service, username, password)

    if op == 'l':
        show_services()

    if op == 'r':
        service = input('qual é o serviço para obter a senha? ')
        get_password(service)

conn.close()