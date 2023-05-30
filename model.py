import json
import requests
import streamlit as st


connection_data = {
    'api_url':  st.secrets['API_URL'],
    'folder_id':  st.secrets['FOLDER_ID'],
    'token_url':  st.secrets['TOKEN_URL']
}

class Model:
    def __init__(self, API):
        self.api_url = st.secrets['API_URL']
        self.folder_id = st.secrets['FOLDER_ID']
        try:
            token = requests.request(
                "GET",st.secrets['TOKEN_URL']).content.decode()
            self.headers = {"Authorization": f'Bearer {token}',
                            "Content-Type": "application/json"}
        except requests.exceptions.RequestException as e:
            return None

    def __query(self, data):
        if len(self.headers['Authorization']) == 193:
            try:
                response = requests.request(
                    "POST", self.api_url, headers=self.headers, data=data)
                return json.loads(response.content.decode("utf-8"))
            except requests.exceptions.RequestException as e:
                return {'internal_error': 'Ошибка при подключении к модели'}
        else:
            return {'internal_error': 'Ошибка при подключении к модели'}

    def get_answer(self, question, context):
        if question.strip() and context.strip():
            json_data = {"folder_id": self.folder_id, "input": {"input_str": {
                "question": question, "context": context}}}
            data = json.dumps(json_data)
            response = self.__query(data)
           # if (not 'output' in response):
           #     return {'internal_error': 'Ошибка при подключении к модели'}
            return response['output']['output_str']
        #return {"input_error": "Для вычисasdasdaления ответа нужно написать вопрос и определить контекст!"}
