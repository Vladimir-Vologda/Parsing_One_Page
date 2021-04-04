#   Импорт требующихся библиотек
import requests  # Библлиотека запроса
from bs4 import BeautifulSoup  # Библиотека разбора HTML
import json  # Библиотека работы с форматом JSON

# User-Agent: для того, что бы requests выглядел как браузер (можно посмотреть свой у себя в браузере, либо найти в
# интернете список User-Agent-ов для разных браузеров и систем)
user_a = {
    'User-Agent': 'Mozilla / 5.0(iPad; CPU OS 11_0 like Mac OS X) AppleWebKit / 604.1 .34(KHTML, like Gecko) Version '
                  '/ 11.0 Mobile / 15 A5341f Safari / 604.1',
    'Accept-Language': 'ru, en; q = 0.9',
}  # Присваиваем его любой переменной, у меня она - user_a


#   Функция получкния страници в HTML формате
def get_html(url):  # Получение URL функцией
    response = requests.get(url, headers=user_a)  # Запрос к URL и подставление нашего USER-AGENT
    return response.text  # Возвращение полученой страници в HTML формате


#   Разбор HTML
def one_block_html(html):   # Получение HTML от пердыдущей функции
    links = []  # Список для записи спарсиных ссылок
    soup = BeautifulSoup(html, 'lxml')
    all_block = soup.find('body').find('div',
                                       class_="subcategory")  # Поиск всего что относится к этому тегу и классу (к
    # первому найденному классу)
    one_block = all_block.find_all('a',
                                   class_="subcategory__item ui-link ui-link_blue")  # Поиск всех отделов по этому
    # тегу и классу в ALL_BLOCK
    for i in one_block:  # Перебор всех найденных отделов ONE_BLOCK
        link_blocks = i.get('href')  # Поиск элемента имеющего href
        links.append(
            {
            'Link': f'https://www.dns-shop.ru{link_blocks}'
            }
        )  # Запись всех найденных элементов в список (способом добавления)
    return links  # Возвращение полученного списка


# def two_block_html(html):
#     link_list = []
#
#     return link_list


#   Функция записи в JSON формат
def writer(data):
    with open('list.json', 'w', encoding='utf=16') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


#   Функция собирающая предыдущие
def main():
    url = 'https://www.dns-shop.ru/catalog/af47fe7c3bae7fd7/smartfony-i-gadzhety/'
    html = get_html(url)    # 1-я функция, подстовляем наш url
    link = one_block_html(html)    # 2-я функция, подстовляем полученный предыдущей функцией html
    writer(link)    # 3-я функция, записываем полученный предыдущей функцией результат в JSON формат


#   Запуск функции
if __name__ == '__main__':
    main()


# P.S.
# Теги, Классы, ID и т.д. для каждого сайта индивидуальны
