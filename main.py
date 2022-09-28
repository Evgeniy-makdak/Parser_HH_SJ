import requests
import json
import datetime


class Vacancy:

    def __init__(self, vac_name: str, vac_url: str, vac_discript: str, vac_salary):
        self.vac_name = vac_name
        self.vac_url = vac_url
        self.vac_discript = vac_discript
        self.vac_salary = vac_salary

    """Создаём класс для отображения информации через магический метод repr__"""

    def __repr__(self):
        return f'Вакансия {self.vac_name}\nссылка на описание: {self.vac_url}\nнеобходимые навыки: {self.vac_discript}\n' \
               f'с зарплатой {self.vac_salary}'


def NoneToStr(obj):
    if obj is None:
        return "Нет данных"
    else:
        return obj


headers = {
    'User-Agent': 'api-test-agent',
}

search_prof = input("Введите искомую профессию: ")  # Ключевое слово для поиска

# Цикл с несколькими запросами
for i in range(1):
    # Создаём/очищаем файл со страницой i
    with open('data_page{}.json'.format(i), 'w', encoding='utf-8') as empty_file:
        pass

    per_page = input("Введите количество вакансий на одной странице: ")  # Кол-во вакансий на 1 странице

    # Отправляем запрос на получение вакансий с i-ой страницы
    response = requests.get(
        'https://api.hh.ru/vacancies?text={}&per_page={}&page={}'.format(search_prof, per_page, i), headers=headers,
        verify=False)

    # print(response)  # Статус запроса (200 - нет ошибки, else ошибка) см стандарт html
    # print(response.text)  # Текст Ответа
    todos = json.loads(response.text)  # Текст Ответа -> JSON

    json_resp = response.json()

    Vacancys = []

    for job in json_resp["items"]:
        name = job["name"]
        url = job["apply_alternate_url"]

        discript = NoneToStr(job["snippet"]["requirement"]) + NoneToStr(job["snippet"]["responsibility"])

        if job['salary'] is None:
            salary = "Нет данных"
        else:
            salary = (job['salary']['from'], job['salary']['to'])
        new_vacancy = Vacancy(name, url, discript, salary)
        Vacancys.append(new_vacancy)
        # print(job)

    for vac in Vacancys:
        print(vac)

    # Записываем в файл со страницой i json
    with open('data_page{}.json'.format(i), 'a', encoding='utf-8') as file:
        json.dump(todos, file, ensure_ascii=False, indent=4)


