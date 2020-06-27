import shutil
#manipulando arquivos

#arquivo = open('teste.txt', 'w') #o w é para escrever, write para criar
#arquivo.write('Minha primeira escrita')
#arquivo = open('teste.txt', 'a') #o a atualiza, o texto
#arquivo.write('\nTerceira linha')
#arquivo.close()
def escrever_arquivo(texto):
    diretorio = 'C:/Users/MaiconBischoffBischo/Documents/Projetos/aulasPython/app_python/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r') #le arquivo read
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')# sempre que ele encontrar um \n ou seja enter ele insere na lista
    print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0) #Tira primeira posicao
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):

    shutil.copy(nome_arquivo, 'C:/Users/MaiconBischoffBischo/Documents/Projetos/aulasPython/notas2.txt')#se nao por nome ele copia com msm nome

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/MaiconBischoffBischo/Documents/Projetos/aulasPython/')

if __name__ == '__main__':
    move_arquivo('teste.txt')
    #copia_arquivo('notas.txt')
    #lista_media = media_notas('notas.txt')
    #print(lista_media)
    #media_notas('notas.txt')
    #escrever_arquivo('primeira linha.\n')
    #aluno = 'Miguel, 10, 10, 10, 10\n'
    #atualizar_arquivo('notas.txt', aluno)
    #ler_arquivo('teste.txt')