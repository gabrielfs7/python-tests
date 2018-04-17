"""

- Read webpage
- Colect and format data
- Save data to csv file

"""

import requests
import pandas
from bs4 import BeautifulSoup


def get_news_tags(url):
    response = requests.get(url)
    content = response.content

    soup = BeautifulSoup(content, "html.parser")

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


def iterate_news(page_count):
    news_list = []
    url = 'http://www.saojose.sc.gov.br/index.php/sao-jose/publicacoes-legais/categoria/concursos'

    if page_count > 0:
        url = url + '/P' + str(page_count)

    print(url)

    for news_tag in get_news_tags(url):
        dictionary = {}
        dictionary["Title"] = get_news_title(news_tag)
        dictionary["Keywords"] = get_news_keywords(news_tag)
        dictionary["Date"] = get_news_event_date(news_tag)
        dictionary["Description"] = get_news_description(news_tag)
        dictionary["Link"] = get_news_link(news_tag)

        news_list.append(dictionary)

    return news_list


final_news_list = []
page_count = 0
has_items = True

# While find items in webpage to process, increment the list
while has_items:
    news_list = iterate_news(page_count)

    final_news_list.extend(news_list)

    has_items = len(news_list) > 0
    page_count = page_count + 12


data_frame = pandas.DataFrame(final_news_list)
data_frame.to_csv("beautiful_soup.csv")