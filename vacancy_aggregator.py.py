import requests
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep 

# 1. Получение вакансий с HeadHunter API
def get_hh_vacancies(text='Python', area=48, per_page=20):
    url = 'https://api.hh.ru/vacancies'
    params = {'text': text, 'area': area, 'per_page': per_page}
    response = requests.get(url, params=params)
    data = response.json()
    names, employers, links = [], [], []
    for item in data.get('items', []):
        names.append(item['name'])
        employers.append(item['employer']['name'] if item['employer'] else 'Нет данных')
        links.append(item['alternate_url'])
    return pd.DataFrame({'Вакансия': names, 'Компания': employers, 'Ссылка': links, 'Источник': 'HeadHunter'})

# 2. Веб-скрапинг вакансий с Joobsi
def get_joobsi_vacancies(url='https://kg.joobsi.com/jobs/python/'):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    names, employers, links = [], [], []
    vacancies = soup.select('.job-item')  # Поиск элементов вакансий. Возможно нужно корректировать под реальную разметку.
    for v in vacancies:
        name = v.select_one('.job-title').get_text(strip=True) if v.select_one('.job-title') else 'Нет названия'
        employer = v.select_one('.company-name').get_text(strip=True) if v.select_one('.company-name') else 'Нет данных'
        link = v.select_one('a').get('href') if v.select_one('a') else ''
        names.append(name)
        employers.append(employer)
        links.append(link)

    return pd.DataFrame({'Вакансия': names, 'Компания': employers, 'Ссылка': links, 'Источник': 'Joobsi'})

def get_indeed_vacancies(url='https://www.indeed.com/jobs?q=python&l='):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    names, employers, links = [], [], []
    vacancies = soup.select('.jobsearch-SerpJobCard')  # основная карточка вакансии на Indeed
    for v in vacancies:
        name = v.select_one('.title a').get_text(strip=True) if v.select_one('.title a') else 'Нет названия'
        employer = v.select_one('.company').get_text(strip=True) if v.select_one('.company') else 'Нет данных'
        link = 'https://www.indeed.com' + v.select_one('.title a').get('href', '') if v.select_one('.title a') else ''
        names.append(name)
        employers.append(employer)
        links.append(link)

    return pd.DataFrame({'Вакансия': names, 'Компания': employers, 'Ссылка': links, 'Источник': 'Indeed'})


# Получение данных с сайтов
df_hh = get_hh_vacancies()
df_joobsi = get_joobsi_vacancies()
df_indeed = get_indeed_vacancies()
# Объединение данных со всеми сайтами
df_all = pd.concat([df_hh, df_joobsi, df_indeed], ignore_index=True)

# Сохранение обновленных данных
df_all.to_excel("asd.xlsx",index=False)

print(df_all)

