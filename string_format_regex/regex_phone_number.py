'''
https://pt.stackoverflow.com/questions/46672/como-fazer-uma-express%C3%A3o-regular-para-telefone-celular
https://pt.stackoverflow.com/questions/106757/express%C3%A3o-regular-para-telefones
'''
'''
celular inicia com o digito 9 e telefone tem 8 digitos e inicia com 2 a 8

^\([1-9]{2}\) (?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}$

Se você quiser deixar os parênteses, o espaço em branco e hífen opcionais, então você pode colocar um ? após cada um desses símbolos, resultando nesta expressão regular:
^\(?[1-9]{2}\)? ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$

^ - Início da string.
\( - Um abre parênteses.
[1-9]{2} - Dois dígitos de 1 a 9. Não existem códigos de DDD com o dígito 0.
\) - Um fecha parênteses.
  - Um espaço em branco.
(?:[2-8]|9[1-9]) - O início do número. Representa uma escolha entre o um dígito entre 2 e 8 (a parte do [2-8]) e de um 9 seguido de um dígito de 1 a 9 (a parte do 9[1-9]). O | separa as opções a serem escolhidas. O (?: ... ) agrupa tais escolhas. Telefones fixos começam com dígitos de 2 a 8. Telefones celulares começam com 9 e têm um segundo dígito de 1 a 9. O primeiro dígito nunca será 0 ou 1. Celulares não podem começar com 90 porque esse é o prefixo para ligações a cobrar.
[0-9]{3} - Os demais três dígitos da primeira metade do número do telefone, perfazendo um total de 4 ou 5 dígitos na primeira metade.
\- - Um hífen.
[0-9]{4} - A segunda metade do número do telefone.
$ - Final da string.

filtrar ddd real:
(?:[14689][1-9]|2[12478]|3[1234578]|5[1345]|7[134579])

completo formato obrigatorio:
^\((?:[14689][1-9]|2[12478]|3[1234578]|5[1345]|7[134579])\) (?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}$

completo formato não obrigatorio com ?:
^\(?(?:[14689][1-9]|2[12478]|3[1234578]|5[1345]|7[134579])\)? ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$
'''
'''
telefones 0800
números de operadoras e serviços como 10315 e 190
telefones representados com ou sem parênteses
aceita operadora representada como 0xx11
telefones com ou sem os separadores [ .-]
ignora telefones começados com 0 se não tiver DDD (ex: 0999-9999 não é aceito, mas 0xx11 9123-1234 é)

/^1\d\d(\d\d)?$|^0800 ?\d{3} ?\d{4}$|^(\(0?([1-9a-zA-Z][0-9a-zA-Z])?[1-9]\d\) ?|0?([1-9a-zA-Z][0-9a-zA-Z])?[1-9]\d[ .-]?)?(9|9[ .-])?[2-9]\d{3}[ .-]?\d{4}$/gm
'''