import requests
import json
import datetime

headers = {
    'User-Agent': 'api-test-agent',
}

str = input("Введите интересующую вас профессию: ")  # Ключевое слово для поиска
date_from = (datetime.datetime.now() - datetime.timedelta(minutes=5)).strftime(
    '%Y-%m-%dT%H:%M:%S')  # Дата начала поиска Пока не реализовали
date_to = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

# Цикл с несколькими запросами
for i in range(1):
    # Создаём/очищаем файл со страницой i
    with open('data_page{}.json'.format(i), 'w', encoding='utf-8') as empty_file:
        pass

    per_page = 100  # Кол-во вакансий на 1 странице

    # Отправляем запрос на получение вакансий с i-ой страницы
    response = requests.get(
        'https://api.hh.ru/vacancies?text={}&per_page={}&page={}'.format(str, per_page, i), headers=headers,
        verify=False)

    # print(response)  # Статус запроса (200 - нет ошибки, else ошибка) см стандарт html
    # print(response.text)  # Текст Ответа
    todos = json.loads(response.text)  # Текст Ответа -> JSON

    # Записываем в файл со страницой i json
    with open('data_page{}.json'.format(i), 'a', encoding='utf-8') as file:
        json.dump(todos, file, ensure_ascii=False, indent=4)

    ## Добавить обработку json создать экземляры класса vacancy


