from seleniumbase import BaseCase
import cv2
import time
from model import Model
import streamlit as st

json = {
    'api_url':  st.secrets['API_URL'],
    'folder_id':  st.secrets['FOLDER_ID'],
    'token_url':  st.secrets['TOKEN_URL']
}


class ComponentsTest(BaseCase):

    def test_answer_ru(self):
        model = Model(json)
        res = model.get_answer(
            'Как тебя зовут?', 'Мне тридцать лет, Меня зовут Петр, я из города Санкт-Петребург')
        assert res['answer'].find('Петр') > 0

    def test_answer_en(self):
        model = Model(json)
        res = model.get_answer(
            'What is your name?', 'I am thirty years old, my name is Peter, I am from the city of St. Petersburg')
        assert res['answer'].find('Peter') > 0

    def test_big_context_answer_ru(self):
        model = Model(json)
        res = model.get_answer(
            'Какой самолет стал самым успешным у Airbus?', 'Модельный ряд продукции Airbus начался в начале 1970-х годов с двухдвигательного самолёта A300. Укороченный вариант A300 известен как A310. Этот самолёт стал в начале 90-х годов первой «иномаркой» в российском ГВФ. Из-за недостаточного успеха модели A300, Airbus начал разработку среднемагистрального проекта A320 с инновационной системой управления fly-by-wire. Совершивший первый полёт в 1987 году, A320 стал самым большим коммерческим успехом для компании. Airbus A318 и A319 являются укороченными вариантами А320, которые с некоторыми изменениями предлагаются Airbus’ом для рынка корпоративных реактивных самолётов (Airbus Corporate Jet). Удлинённая версия А320 известна как A321 и конкурирует с более поздними моделями Boeing 737.')
        assert res['answer'].find('A320') > 0

    def test_big_context_answer_ru(self):
        model = Model(json)
        res = model.get_answer(
            'Who is in charge of the company?', "Airbus's registered headquarters is in Leiden, Netherlands, but its head office is located in Toulouse, France. The 'SE' in its corporate name means it is a societas Europaea, which enables it to be registered as a European rather than a national corporation. Its shares are traded in France, Germany and Spain. The company is led by CEO Guillaume Faury and is a component of the Euro Stoxx 50 stock market index")
        assert res['answer'].find('Faury') > 0

    def test_question_missed(self):
        model = Model(json)
        res = model.get_answer(
            "", "Мне тридцать лет, Меня зовут Петр, я из города Санкт-Петребург")
        assert 'input_error' in res

    def test_context_missed(self):
        model = Model(json)
        res = model.get_answer(
            "Как тебя зовут?", "")
        assert 'input_error' in res

    def test_question_context_missed(self):
        model = Model(json)
        res = model.get_answer(
            "", "")
        assert 'input_error' in res

    def test_internal_error(self):
        model = Model({'api_url':  'aabbccddeeffgghhjj',
                      'folder_id':  st.secrets['FOLDER_ID'], 'token_url':  st.secrets['TOKEN_URL']})
        res = model.get_answer(
            'Как тебя зовут?', 'Мне тридцать лет, Меня зовут Петр, я из города Санкт-Петребург')
        assert 'internal_error' in res
   


