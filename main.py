import requests
import json
import datetime


class Vacancy:

    def __init__(self, vac_name: str, vac_url: str, vac_discript: str, vac_salary):
        self.vac_name = vac_name
        self.vac_url = vac_url
        self.vac_discript = vac_discript
        self.vac_salary = vac_salary

    def __repr__(self):
        return f'Вакансия {job["name"]}\nссылка на описание: {job["url"]}'


def NoneToStr(obj):
    if obj is None:
        return "Нет данных"
    else:
        return obj


# """Преобразуем json файл в список для дальнейшей обработки"""
# with open('data_page0.json', 'r', encoding='utf-8') as file:
#     data_list = json.load(file)
# it = data_list[0]
# print(data_list)

headers = {
    'User-Agent': 'api-test-agent',
}

# str = input("Введите интересующую вас профессию: ")  # Ключевое слово для поиска
str = "Python"
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

    json_resp = response.json()

    Vacancys = []


    for job in json_resp["items"]:
        name = job["name"]
        url = job["url"]

        discript = NoneToStr(job["snippet"]["requirement"]) + NoneToStr(job["snippet"]["responsibility"])  # TODO LOGIG CAN'T BE NONE

        if job['salary'] is None:
            salary = "Нет данных"
        else:
            salary = (job['salary']['from'], job['salary']['to'])
        new_vacancy = Vacancy(name, url, discript, salary)
        Vacancys.append(new_vacancy)
        print(job)

    for vac in Vacancys:
        print(vac)

    # Записываем в файл со страницой i json
    with open('data_page{}.json'.format(i), 'a', encoding='utf-8') as file:
        json.dump(todos, file, ensure_ascii=False, indent=4)

    ## Добавить обработку json создать экземляры класса vacancy

"""Создаём класс для отображения информации через магический метод repr__"""
