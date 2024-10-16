    # Crie uma função chamada verificar_paridade que receba um número inteiro como argumento e retorne uma mensagem indicando se o número é par ou ímpar.
    
def verificar_paridade(num=0):
    if num % 2 == 0:
        return f'O número {num} é par'
    else:
        return f'O número {num} é ímpar'
    
numero_recebido = num = int(input('Digite um número: '))
resultado = verificar_paridade(numero_recebido)
print(resultado)

