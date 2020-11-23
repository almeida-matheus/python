from tkinter import Tk
from tkinter import filedialog as dlg
import os

Tk().withdraw() #janela principal oculta
path = dlg.askopenfilename() #permite selecionar o arquivo
path1 = 'D:\\Arquivos\\matheus\\Documents\\Code\\python\\secret\\api_twitter.txt'

'''
#windows = 'C:\\System32\\teste.txt'
#linux = 'home//user//Maria'

path_os = os.path.join('Arquivos', 'matheus','Documents','Code','python','secret','api_twitter.txt')
print(path_os)
'''

with open(path, 'r') as tfile:
    consumer_key = tfile.readline().strip('\n')
    consumer_secret = tfile.readline().strip('\n')

    token_key = tfile.readline().strip('\n')
    token_secret = tfile.readline().strip('\n')

print(consumer_key)