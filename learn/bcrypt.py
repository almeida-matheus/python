#https://github.com/pyca/bcrypt
import bcrypt

#encriptando a senha
def validar_hash_password(senha):
    hashed = bcrypt.hashpw(senha.encode('utf8'),bcrypt.gensalt())
    return hashed

senha = 'abc123'
senha1 = b'abc123'
senha_encode = senha.encode('utf8')
#encriptando a senha
secret_password = bcrypt.hashpw(senha_encode, bcrypt.gensalt())
# gensalt's log_rounds parameter determines the complexity.

print(secret_password)
print(type(secret_password))
print(senha_encode)
print(type(senha_encode))
print('\n')
#comparando a senha
if bcrypt.checkpw(senha_encode,secret_password):
    print('it match')
    print(senha_encode)
    print(secret_password)
else:
    print('it does not match')

teste1 = 'abc123'
print(bcrypt.hashpw(teste1.encode('utf8'),secret_password) == secret_password)

'''
import bcrypt
key = bcrypt.kdf(
password=b'password',
salt=b'salt',
desired_key_bytes=32,
rounds=100)

password = b"an incredibly long password" * 10
hashed = bcrypt.hashpw(
base64.b64encode(hashlib.sha256(password).digest()),
bcrypt.gensalt()

("b'$2b$12$axoLPkvOi6smIEUxaUnNTukmgQaXp8YhkTCtaeUvkl1w.55BYHqIC'",)
print(hash_senha[5:int(len(hash_senha)-3])
b'$2b$12$lzeja6Pi8ktCHgB26tkLS.cJ1TO5gykfYkYQMr4FQQlP5nSvv3Dhi'

b'1234'
b'$2b$12$axoLPkvOi6smIEUxaUnNTukmgQaXp8YhkTCtaeUvkl1w.55BYHqIC'


'''
print('\n')
hash_senha = str("b'$2b$12$axoLPkvOi6smIEUxaUnNTukmgQaXp8YhkTCtaeUvkl1w.55BYHqIC'",)

hash_senha = hash_senha[2:int(len(hash_senha)-1)]
print(hash_senha)