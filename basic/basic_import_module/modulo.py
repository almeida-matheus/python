def soma(x:float,y:float) -> float:
    return x + y

print(__name__)

if __name__=='__main__': #se o arquivo esta sendo executado diretamente, nao importado
    print(soma(20,30))

#or

def main() -> None:
    print(soma(20,20))

if __name__=='__main__':
    main()