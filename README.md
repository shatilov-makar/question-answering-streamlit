[![Python application](https://github.com/shatilov-makar/question-answering-streamlit/actions/workflows/python-app.yml/badge.svg)](https://github.com/shatilov-makar/question-answering-streamlit/actions/workflows/python-app.yml)

# Проект по дисциплине "Программная инженерия"

## Состав команды:

- Шатилов Макар — Тимлид, развертывание приложения на платформе Яндекс.Облако, общая поддержка проекта;
- Кудрин Данил — Разработка тестов и настройка github;
- Шерер Даниил — Разработка дизайна и функциональности приложения.

## Описание приложения

Цель приложения — определение ответа на поставленный вопрос исходя из предложенного контекста.

Алгоритм работы:

1. Ввод вопроса, на который пользователь хочет получить ответ
2. Ввод контекста, к которому будет задаваться вопрос
3. Вычисление ответа [моделью](https://huggingface.co/AlexKay/xlm-roberta-large-qa-multilingual-finedtuned-ru)
4. Вывод результата и точности

Приложение развернуто на платформе Streamlit: https://shatilov-makar-question-answering-streamlit-index-mqzwg7.streamlit.app/

## Пример работы приложения:

![image](https://user-images.githubusercontent.com/62944516/211281288-da38c20b-0203-4f49-a8e8-30b9753467f4.png)
