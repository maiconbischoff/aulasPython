class Error(Exception): # cria uma classe pra de erro, que herda de Exception
    pass#o pass  nao faz nada é so pra nao ficar vazio

class ImputError(Error): #cria a classe que herda de Error sempre que precisar criar uma classe de erro personalizada tem que criar uma qe herde de outra classe que herda de Exceprion
    def __init__(self, message):
        self.message = message
while True:
    try:
        x = int(input('Digite uma nota de 0 a 10'))
        print(x)
        if x > 10:
            raise ImputError('nota nao pode ser maior do que 10') #raise força uma exception
        elif x < 0:
            raise ImputError('nota nao pode ser menor do que 0') #raise força uma exception
        break
    except ValueError:
        print('Valor invalido. deve se digitar apenas numeros')
    except ImputError as ex:
        print(ex)