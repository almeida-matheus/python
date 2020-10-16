import bcrypt
import sqlite3


def valida_senha(senha_digitada, hash_senha):
    return bcrypt.hashpw(senha_digitada, hash_senha) == hash_senha


def insere_usuario(conexao, usuario, senha):
    hash_senha = bcrypt.hashpw(senha.encode('utf8'), bcrypt.gensalt())
    conexao.execute('insert into USUARIOS values ("%s", "%s")' % (usuario, hash_senha))
    conexao.commit()


def usuario_autenticado(conexao, usuario, senha):
    cursor = conexao.execute('select SENHA from USUARIOS where NOME = "%s"' % (usuario,))
    dados = cursor.fetchone()
    hash_senha = str(dados[0])
    return valida_senha(senha, hash_senha)

# alguns testes
if __name__ == '__main__':
    conexao = sqlite3.connect('arquivo2.db')
    comando = conexao.cursor()
    conexao.execute("CREATE TABLE IF NOT EXISTS USUARIOS (NOME text,SENHA text)")
    insere_usuario(conexao, 'maria', 'teste')
    insere_usuario(conexao, 'joao', 'teste123')
    if usuario_autenticado(conexao, 'joao', 'teste123'):
        print
        'joao está autenticado!'
    else:
        print
        'Xiiiii...'