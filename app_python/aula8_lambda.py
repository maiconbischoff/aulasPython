#funçoes lambda, ou funcoes anonimas, a lambda só e eficiente com funcoes que da para resolver em uma unica linha
contador_letras = lambda lista: [len(x) for x in lista] #foi feito o contador de letras em uma unica linha

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
print(soma(5, 10))

subtracao = lambda a, b: a - b
print(subtracao(10, 5))

calculadora = { #criando um dicionario
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}

print(type(calculadora)) #tipo dicionario
soma = calculadora['soma']
subtracao = calculadora['subtracao']
multiplicacao = calculadora['multiplicacao']
divisao = calculadora['divisao']
print(soma(5, 6))
print(subtracao(20,10))
print(multiplicacao(10, 10))
print(divisao(50, 10))