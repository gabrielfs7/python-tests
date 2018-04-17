import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.saojose.sc.gov.br/index.php/sao-jose/publicacoes-legais/categoria/concursos')
content = response.content

soup = BeautifulSoup(content, "html.parser")

"""
<div class="row-noticia">
<span class="radius">Comunicados</span>
<span class="radius">Concursos</span>
<small class="row-evento-small">09 de Abril de 2018 - 17h07</small>
<a href="http://www.saojose.sc.gov.br/index.php/sao-jose/publicacoes-legais-desc/convocacaeo-do-concurso-publico-edital-n.-001-2014-gab-agente-administrativ"><h4>Convocação do Concurso Público - Edital n. 001/2014 - GAB - Agente Administrativo</h4></a>
<p>Convocação do Concurso Público - Edital n. 001/2014 - GAB - Agente Administrativo</p>
</div>
"""


def get_news_tags():
    all = soup.find_all('div', {'class': 'container conteudo interna'})

    return all[0].find_all('div', {'class': 'row-noticia'})


def get_news_keywords(news_tag):
    out = []

    for keyword in news_tag.find_all('span', {'class' : 'radius'}):
        out.append(keyword.text)

    return ', '.join(out)


def get_news_event_date(news_tag):
    return news_tag.find('small', {'class': 'row-evento-small'}).text


def get_news_title(news_tag):
    return news_tag.find('h4').text


def get_news_link(news_tag):
    return news_tag.find('a')['href']


def get_news_description(news_tag):
    p = news_tag.find('p')

    if p is not None:
        return p.text

    return ''


for news_tag in get_news_tags():
    print("Title: " + get_news_title(news_tag))
    print("Keywords: " + get_news_keywords(news_tag))
    print("Event Date: " + get_news_event_date(news_tag))
    print("Description: " + get_news_description(news_tag))
    print("Link: " + get_news_link(news_tag))
    print("\n")