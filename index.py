import streamlit as st
from model import Model

connection_data = {
    'api_url':  st.secrets['API_URL'],
    'folder_id':  st.secrets['FOLDER_ID'],
    'token_url':  st.secrets['TOKEN_URL']
}


st.title('Multilingual-finedtuned-ru ')
hint_text = "**Вывод**"
description_text = "Модель способная находить ответы на вопросы из контекста."
st.subheader(description_text)

text_question = st.text_input(label='Введите вопрос')
text_context = st.text_area(label='Введите контекст')
button = st.button('Получить ответ')


model = Model(connection_data)


if button and len(text_question.strip()) > 0 and len(text_context.strip()) > 0:
    response = model.get_answer(text_question, text_context)
    if ('answer' in response):
        st.markdown(hint_text)
        st.write(f"""
                 Оценка: {response['score']}\n
                 Ответ: {response['answer']}\n
                 Ссылка для ознакомления с моделью: https://huggingface.co/AlexKay/xlm-roberta-large-qa-multilingual-finedtuned-ru
                  """)
    else:
        st.markdown(list(response.values())[0], unsafe_allow_html=False)
else:
    st.markdown(hint_text)


