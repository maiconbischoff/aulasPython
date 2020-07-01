#pip instal requests
import requests

def retorna_dados_cep(cep):
    response = requests.get('http://viacep.com.br/ws/{}/json/'.format(cep))
    response1 = requests.get('https://ibmdev-api.bancorenner.com.br:8083/v4.0/noAuth/autenticada/cartoes/dolar')
    print(response.status_code)
    print(response.text)
    print(type(response.json()))
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    response = retorna_response('https://www.feevale.br')
    print(response)
    #retorna_dados_cep(95650000)
    #dados_pokemon = retorna_dados_pokemon("pikachu")
    #print(dados_pokemon)
    #print(dados_pokemon['sprites']['front_shiny'])
