from bs4 import BeautifulSoup
import requests
import re

# Сохранение ссылок аннотаций
def save_annotations(page_soup):
    annotation_links = []    

    regex = re.compile(r'^http://council.gov.ru/media/files/')
    a_elements = page_soup.find_all('a', href=regex)

    for a in a_elements:
        if a.text.rstrip() == 'Аннотации к ФЗ':
            annotation_links.append(a['href'])

    print(annotation_links)
    return annotation_links


for page_number in range(5):
    url = f'http://council.gov.ru/activity/meetings/page/{page_number + 1}/'
    print('\nURL: ', url + '\n')
    
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')

    save_annotations(soup)
