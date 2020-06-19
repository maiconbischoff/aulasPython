conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}'.format(conjunto_uniao))
conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))
conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença conjunto 1 para conjunto 2: {}'.format(conjunto_diferenca1))
print('Diferença conjunto 2 para conjunto 1 {}'.format(conjunto_diferenca2))
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simétrica(é o que não tem nos dois): {}'.format(conjunto_diff_simetrica))

conjuntoa = {1, 2, 3}
conjuntob = {1, 2, 3, 4, 5}
conjunto_subConjunto = conjuntoa.issubset(conjuntob)
print(conjunto_subConjunto)
conjunto_superConjunto = conjuntob.issuperset(conjuntoa)
print(conjunto_superConjunto) #b tem todos elementos da a e mesmo que tenha mais elementos nao tem problema

#converter lista para conjunto, para por exemplo remover duplicidade da lista

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)




# conjunto = {1, 2, 3, 4}
# print(type(conjunto)) #set é conjunto
# conjunto.add(5)
# conjunto.discard(1)
# print(conjunto)

#características, tupla(), lista[] e conjunto{}