#pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests
import json

res = requests.get("https://digitalinnovation.one")
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser') #instancia o beautiful soap entregando a renderizacao do texto que vem do request e dando um parser no html para que o BS transforme todo o texto em html

links = soup.find(class_="pagination").find_all('a') #encontra os links das paginas e pega todas tag 'a'

all_pages = []
for link in links:
    page = requests.get(link.get('href')) #percorre todos os links e apresenta os endereços
    all_pages.append(BeautifulSoup(page.text, 'html.parser'))
print(len(all_pages))

posts = soup.find_all(class_="post")

#print(res.text) #printa o html em texto
#print(soup) #printa o html em html


#print(all_posts)
#print(posts[0]) #printa o indice zero

all_posts = []
for posts in all_pages:
    posts = posts.find_all(class_="post")  # procura todas as classes do html com nome de "post" e transforma em array
    for post in posts:
        info = post.find(class_="post-content")
        #print(post.find('h2').text) #pega todos h2 e transforam em texto
        title = info.h2.text
        preview = info.p.text
        author = info.find(class_="post-author").text #se nao colocar o .text ele traz a tag
        time = info.footer.date['datetime']
        img = info.find(class_="wp-post-image")['src']#o find pega apenas o primeiro item que encontrar
        #all_posts(title, preview, author)
        all_posts.append({
            'title': title,
            'preview': preview,
            'author': author,
            'img': img,
            'time': time})

print(all_posts)
with open('posts.json', 'w') as jsonfile:
    json.dump(all_posts, jsonfile, indent=3, ensure_ascii=False)

