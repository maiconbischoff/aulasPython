class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1
    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1
print(__name__) # quando chama pelo mesmo arquivo o name é main, quando chama pelo console, é aula7_televisao
if __name__ == '__main__': # quando quem ta chamando for o main, ou seja, for o mesmo arquivo, ele faz o que esta dentro

    televisao = Televisao() #instancia da televisao
    print('Televisao esta ligada {}'.format(televisao.ligada))
    televisao.power()
    print('Televisao esta ligada {}'.format(televisao.ligada))
    televisao.power()
    print('Televisao esta ligada {}'.format(televisao.ligada))
    televisao.power()
    print('Televisao esta ligada {}'.format(televisao.ligada))
    print('Canal: {}'.format(televisao.canal))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.diminui_canal()
    print('Canal: {}'.format(televisao.canal))
