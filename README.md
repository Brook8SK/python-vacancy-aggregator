# python-vacancy-aggregator
Job vacancies scraper/aggregator written in Python (requests, pandas, BeautifulSoup)



# Агрегатор вакансий Python-разработчика

Скрипт собирает вакансии Python‑разработчика с нескольких источников (HeadHunter, Joobsi, Indeed) и сохраняет их в один Excel‑файл `asd.xlsx`.

## Функции

- Запрос вакансий через API HeadHunter по ключевому слову и городу (параметр `area`).
- Веб‑скрапинг вакансий с сайта Joobsi.
- Веб‑скрапинг вакансий с Indeed с подстановкой заголовка, компании и ссылки.
- Объединение всех вакансий в один `DataFrame` и сохранение в Excel.

## Технологии

- Python 3
- requests
- pandas
- BeautifulSoup (bs4)

## Установка

Склонируй репозиторий и установи зависимости:﻿

git clone https://github.com/Brook8SK/python-vacancy-aggregator.git
cd python-vacancy-aggregator
pip install -r requirements.txt

## Запуск

Запусти скрипт:﻿
python main.py
