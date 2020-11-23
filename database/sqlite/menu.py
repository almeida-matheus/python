def menu():
    print('***************************')
    print(' i : inserir nova senha')
    print(' l : listar serviços salvos')
    print(' r : recuperar senha')
    print(' s : sair')
    print('****************************')

while True:
    menu()
    op = input('opção selecionada: ')
    if op not in ['i', 'l', 'r', 's']:
        print('opção inválida')
        print('\n')
        continue

    if op == 's':
        break