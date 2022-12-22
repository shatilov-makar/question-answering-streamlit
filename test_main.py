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
    # def test_basic(self):

    #     # open the app and take a screenshot
    #     self.open("http://localhost:8501")

    #     time.sleep(10)  # give leaflet time to load from web
    #     self.save_screenshot("current-screenshot.png")

    #     # test screenshots look exactly the same
    #     original = cv2.imread(
    #         "visual_baseline\main.jpg"
    #     )
    #     duplicate = cv2.imread("current-screenshot.png")

    #     assert original.shape == duplicate.shape

    #     difference = cv2.subtract(original, duplicate)
    #     b, g, r = cv2.split(difference)
    #     assert cv2.countNonZero(b) == cv2.countNonZero(
    #         g) == cv2.countNonZero(r) == 0

    def test_right_answer(self):
        model = Model(json)
        res = model.get_answer(
            'Как тебя зовут?', 'Мне тридцать лет, Меня зовут Петр, я из города Санкт-Петребург')
        time.sleep(10)
        assert res['answer'].find('Петр') > 0
