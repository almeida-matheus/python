import sqlite3
import bcrypt
import re
import getpass

banco = sqlite3.connect('pessoas.db')
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS USUARIOS (usuario text,hash_senha text)")
banco.commit()

def validar_digito(usuario,senha):
    maiuscula = re.search(r'[A-Z]', senha)
    numero = re.search(r'[0-9]',senha)
    especial = re.search(r'[!@#$%<^&*?]', senha)
    if len(senha) < 8 or len(senha) > 100:
        print('digite pelo menos 8 caracteres\n')
        return 1
    elif maiuscula == None:
        print('digite pelo menos 1 caractere maiusculo\n')
        return 1
    elif numero == None:
        print('digite pelo menos 1 numero\n')
        return 1
    elif especial == None:
        print('digite pelo menos 1 caractere especial\n')
        return 1
    else:
        confirmar = str(input('digite sim para confirmar: ')).strip().upper()[0]
        if confirmar not in 'Ss':
            exit()
        else:
            print('usuario e senha adicionados\n')
            insere_encriptado(usuario,senha)
            return 0

def insere_encriptado(usuario,senha):
    hash_senha = bcrypt.hashpw(senha.encode('utf8'), bcrypt.gensalt())
    cursor.execute('insert into USUARIOS values ("%s", "%s")' % (usuario, hash_senha))
    banco.commit()

def usuario_valido(usuario,senha):
    cursor.execute(f'''
                SELECT usuario FROM USUARIOS
                WHERE usuario = '{usuario}'
            ''')
    rows = cursor.fetchall()
    qnt_results = (len(rows)) #se qnt_resulta = 0, nao existe esse usuario na tabela
    if qnt_results == 0:  # cursor.rowcount == 0:
        print('usuario incorreta')
        exit()
    else:
        return login_valido(usuario,senha)

def login_valido(usuario, senha):
    cursor.execute(f'''
            SELECT hash_senha FROM USUARIOS WHERE usuario = '{usuario}';
            ''')
    for hash_senha in cursor.fetchall():
        hash_senha = str(hash_senha)
        hash_senha = hash_senha[4:int(len(hash_senha)-4)]
        hash_senha = hash_senha.strip()
        hash_senha = hash_senha.encode('utf8')
        if bcrypt.checkpw(senha,hash_senha): #se a senha condiz com o hash da tabela = True
            print('login efetuado com sucesso')
        else:
            print('usuario ou senha incorreta')
            exit()

cont = ()

while cont != 0:
    usuario1 = input('insira o novo nome do usuario: ')
    senha1 = input('insira a nova senha: ')
    cont = validar_digito(usuario1,senha1)

#senha = getpass.getpass(prompt='insira sua senha:', stream=None)

usuario = input('insira o nome do usuario: ')
senha = input('insira a senha: ')

usuario_valido(usuario,senha.encode('utf8'))

#passwd = 'Senha123!'
#passwd_encode = passwd.encode('utf8')
#insere_user('m','123')
#usuario_valido('rincon',passwd_encode)



'''
# alguns testes
if __name__=='__main__':
    conexao = sqlite3.connect('arquivo.db')
    insere_usuario(conexao, 'maria', 'teste')
    insere_usuario(conexao, 'joao', 'teste123')
    if usuario_autenticado(conexao, 'joao', 'teste123'):
        print 'joao está autenticado!'
    else:
        print 'Xiiiii...'

erro
def usuario_autenticado(usuario, senha):
    cursor.execute('select hash_senha from USUARIOS where usuario = "%s"' % (usuario))
    dados = cursor.fetchone()
    hash_senha = str(dados[0])
    return valida_senha(senha, hash_senha)
'''
'''
hashed = bcrypt.hashpw(password.encode(‘utf8’), bcrypt.gensalt())
users.insert({
“Username”: username,
“Password”: hashed
})
'''