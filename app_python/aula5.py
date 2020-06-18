#listas e tuplas
#lista é mutavel
lista = [12, 3, 54, 7]
lista_animais = ['cachorro', 'gato', 'elefante', 'arara']
# print(type(lista))
print(lista[1])

soma = 0
for x in lista:
    print(x)
    soma += x
print(soma)
print(sum(lista))
print(max(lista))
print(min(lista))
print(min(lista_animais))
a = input('Digite um tipo de animal: ')
if a in lista_animais:
    print('já existe  {} na lista'.format(a))
else:
    print('Não existe {} na lista'.format(a))
    lista_animais.append(a)
    print('O animal {} foi incluido a sua lista' .format(a))
    print(lista_animais)
#    lista_animais.pop(0) #retira o ultimo da pilha se nao colocar a posição
#    print(lista_animais)
#lista_animais.remove(a)
#print(lista_animais)
lista.sort()
lista_animais.sort()
print(lista)
print(lista_animais)
lista_animais.reverse() #ordena de forma reversa
print(lista_animais)
print(len(lista_animais))
lista_animais.insert(0, 'boi') #insere posição, elemento
print(lista_animais)

# for x in lista_animais:
#     print(x)
#nova_lista = lista_animais * 3
#print(nova_lista)


#___________________________________________________________________________________
#tuplas são imutaveis

tupla = (1, 10, 12, 14)
print('os valores da tupla são', tupla)
print('o valor selecionado da tupla é ', tupla[1])
print(len(tupla))
tupla_animal = tuple(lista_animais) #converte para tipo tuple
print(type(tupla_animal))
print(tupla_animal)
lita_numerica = list(tupla) #converte para tipo list
print(type(lita_numerica))
print(lita_numerica)