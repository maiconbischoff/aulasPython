
a = int(input('Primeiro bimestre'))
while a > 10: #valida na hora que o usuario digita
    a = int(input('Voce digitou errado. Primeiro Bimestre'))
b = int(input('Segundo bimestre'))
while b > 10:
    b = int(input('Voce digitou errado. Segundo Bimestre'))
c = int(input('Terceiro bimestre'))
while c > 10:
    c = int(input('Voce digitou errado. Terceiro Bimestre'))
d = int(input('Quarto bimestre'))
while d > 10:
    d = int(input('Voce digitou errado. Quarto Bimestre'))

media = (a +b + c +d) /4
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('Média: {}'.format(media))
else:
    print('Foi informada alguma nota errada')



# nota = int(input('Digite a nota'))
# while nota > 10:
#     nota = int(input('Nota inválida: Digite a nota correta'))




# a = 0
# while a <= 10:
#     print(a)
#     a += 1


#numeros primos
# a = int(input('Digite um valor'))
# for num in range(a + 1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(num)
#



# for num in range(101):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(num)




# a = int(input('Digite um número: '))
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div = div+1 # div +=1 também funciona
#
# if div == 2:
#     print('Numero {} é primo'.format(a))
# else:
#     print('Numero {} não é primo'.format(a))


# for x in range(100):
#     print(x)