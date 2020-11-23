#documentation: https://pysimplegui.readthedocs.io/en/latest/
#https://user-images.githubusercontent.com/46163555/70382042-796da500-1923-11ea-8432-80d08cd5f503.jpg

import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('Default')
        #layout
        layout = [
            [sg.Text('',size=(6,0)),sg.Text('programa de cadastro')],
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0),key='nome')],
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(15,0),key='idade')],
            [sg.Text('Quais provedores de e-mail serão aceitos?')],
            [sg.Checkbox('gmail', key='gmail'),sg.Checkbox('outlook', key='outlook')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim','cartões',key='aceitaCartao'),sg.Radio('Não','cartões',key='naoaceitaCartao')],
            [sg.Slider(range=(0,255), default_value=0,orientation='h',size=(15,20),key='sliderVelocidade')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30,10))],
        ]
        #janela
        self.janela = sg.Window('Dados do usuário',layout)

    def Iniciar(self):
        while True:
            #extrair dados da tela
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoaceitaCartao']
            velocidade_script = self.values['sliderVelocidade']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'aceita gmail: {aceita_gmail}')
            print(f'aceita outlook: {aceita_outlook}')
            print(f'aceita cartão: {aceita_cartao}')
            print(f'não aceita cartão: {nao_aceita_cartao}')
            print(f'Velocidade Scripts: {velocidade_script}')
            if self.button in (None, 'exit'): #se fechar a janela clicando no x
                break

tela = TelaPython()
tela.Iniciar()


