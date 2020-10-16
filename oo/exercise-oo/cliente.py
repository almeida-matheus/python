
class Cliente:

    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def __str__(self):
        return "nome: " + self.nome + "\ncpf: " + self.cpf + "\nidade: " + str(self.idade)
