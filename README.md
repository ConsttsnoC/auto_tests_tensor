<!-- Заголовок -->
<h1 align="center">
  <br>
  Тестовое задание для Тензор
  <br>
</h1>
<!-- Описание -->
<p align="center">
  <a href="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" target="_blank">
  </a>
</p>
<!-- Иконки -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12.3-green">
  <img src="https://img.shields.io/badge/Page Object Model-red">
</p>

## Описание

Этот проект представляет собой тестовое задание для компании Тензор. Тесты написаны на Python с использованием подхода Page Object Model (POM). Для логирования используется библиотека `loguru`, а для отчётности и создания скриншотов при падении тестов используется `Allure`.

## Установка

### Предварительные требования

- Убедитесь, что у вас установлен Python 3.12.3.
- Вы умеете создавать виртуальные окружения и работать с ними.
- Установите зависимости из requirements.txt

## Запуск тестов 

### Запуск тестов с Pytest
Для запуска тестов используйте команду: 
`pytest`

## Запуск тестов с генерацией отчёта Allure
### Для запуска тестов с генерацией отчёта в Allure используйте команду: 
`pytest --alluredir=allure-results`

### После выполнения тестов, чтобы сгенерировать отчёт Allure, выполните:
`allure serve allure-results`

## Запуск тестов в headless режиме
### Для запуска тестов в headless режиме используйте команду:
`pytest --headless`
