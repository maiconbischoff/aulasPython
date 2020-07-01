#trabalhando com exceptions
lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read()
    divisao = 10 / 0
    #numero = lista[3]
    #x = a
    #print('fechando arquivo')
    #arquivo.close()
except ZeroDivisionError: #classe do python de exception por divisao por zero
    print('Nao é possivel realizar uma divisão por zero')
except ArithmeticError:
    print('Houve um erro ao realizar uma operaçao aritmética')
except IndexError:
    print('erro ao acessar um indice invalido da lista')
except BaseException as ex:
    #print(ex)
    print('Erro desconhecido. Erro: {}'.format(ex)) #ver  hierarquia das classes de exception no topo vai sempre os filhos
else:
    print('Executa quando nao ocorre exceçao')
finally:
    print('finaly sermpre executa')
    print('fechando arquivo')
    arquivo.close()
 