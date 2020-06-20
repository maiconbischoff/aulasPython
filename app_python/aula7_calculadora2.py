class Calculadora:
    def __init__(self):
       pass #pass nao faz nada, só pra nao ficar vazio desse modo podemos tirar o init, pois nao inicializamos na classe e sim na função
    def soma(self, a, b):
        return a + b
    def subrtracao(self, a, b):
        return a - b
    def multiplicacao(self, a, b):
        return a * b
    def divisao(self, a, b):
        return a / b

calculadora = Calculadora()
print(calculadora.soma(2, 2))
print(calculadora.subrtracao(10, 2))
print(calculadora.multiplicacao(10, 10))
print(calculadora.divisao(10, 5))