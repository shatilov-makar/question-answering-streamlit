import streamlit as st
import json
import requests


class Model:
    def __init__(self, API):
        self.api_url = API['api_url']
        self.folder_id = API['folder_id']
        token = requests.request("GET", API['token_url']).content.decode()
        self.headers = {"Authorization": f'Bearer {token}',
                        "Content-Type": "application/json"}

    def __query(self, data):
        response = requests.request(
            "POST", self.api_url, headers=self.headers, data=data)
        return json.loads(response.content.decode("utf-8"))

    def get_answer(self, question, context):
        json_data = {"folder_id": self.folder_id, "input": {"input_str": {
            "question": question, "context": context}}}
        data = json.dumps(json_data)
        response = self.__query(data)
        return response['output']['output_str']
