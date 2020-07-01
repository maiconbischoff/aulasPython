from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%d/%m/%Y') #converte para formtato brasileiro, ver documentaçao do datetime do python
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario_str))

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y-%H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.weekday())
    print(data_atual.day)
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', ' Sábado', 'Domingo') #cria uma tupla que chama pelo weekday pode se fazer com o mes indice zero começa    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2020'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)
    print(type(data_convertida))
    nova_data = data_convertida - timedelta(days=365)#permite soma e subraçao com datas e horas
    print(nova_data)

if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()
