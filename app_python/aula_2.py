#a = 10
#b = 5
a = int(input('Entre com o primeiro valor'))
b =int(input('Entre com o segundo valor'))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a/b
resto = a%b
print(type(soma))
# soma = str(soma) converte para string
#print(type(soma))
print('soma: ' + str(soma))
print(subtracao)
print(multiplicacao)
print(divisao)
print(resto)
print('Soma: {} \n Subtração {}\n Multiplicação {}'.format(soma, subtracao, multiplicacao))
print('Divisão: {divisao} \n Resto {resto}'.format(resto = resto, divisao = divisao))