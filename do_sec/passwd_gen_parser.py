import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation

def generate_password(letters=8, numbers=4, punctuation=2):
    generated = ""
    generated += random_chars(letters, LETTERS)
    generated += random_chars(numbers, NUMBERS)
    generated += random_chars(punctuation, PUNCTUATION)
    return shuffle_string(generated)

def shuffle_string(text): #funcao para embaralhar a string
    text = list(text) #transformar em lista ['a', 'b', 'c']
    random.shuffle(text) #embaralhr cada letra
    return ''.join(text) #transformar para uma string, tirando os ''

def random_chars(length, chars):
    generated = ""
    for x in range(length):
        generated += random.choice(chars) #choice = pegar 1 caractere aleatorio da lista
    return generated

if __name__ == '__main__': #se estiver rodando o programa nesse arquivo
    import argparse
    parser = argparse.ArgumentParser('Password Generetor')
    parser.add_argument('--letters', type=int, default=8, help='letters quantity')
    parser.add_argument('--numbers', type=int, default=4, help='numbers quantity')
    parser.add_argument('--punctuation', type=int, default=2, help='punctuation quantity')
    args = parser.parse_args()
    print(generate_password(
        letters=args.letters,
        numbers=args.numbers,
        punctuation=args.punctuation
    ))