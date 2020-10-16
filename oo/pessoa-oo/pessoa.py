from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
       self.nome = nome
       self.idade = idade
       self.comendo = comendo
       self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False
    #metodo de instancia/precisa de um atributo self
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
    #metodo de classe/ tem acesso a atributo da classe ano_atual
    #cls se refere a Pessoa, a classe
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


#metodo de instancia
p1 = Pessoa('Luiz', 29)
p2 = Pessoa.por_ano_nascimento('Daniel', 1990)
print(p1.get_ano_nascimento())
print(p2.nome, p2.idade)

#metodo de classe ele retorna um objeto da classe
#quando utilizar: esse metodo é relacionado a classe em geral (ao molde)
# ou a instancia, cada objeto vai ter um valor diferente pra esse metodo