import streamlit as st
from model import Model

connection_data = {
    'api_url':  st.secrets['API_URL'],
    'folder_id':  st.secrets['FOLDER_ID'],
    'token_url':  st.secrets['TOKEN_URL']
}


st.title('Multilingual-finedtuned-ru ')
hint_text = "**Вывод**"
error_text = '**Нужно загрузить модель, для этого [перейдите на страницу модели](https://huggingface.co/makarshatilov/transliteration_v1), нажмите Compute, немного подождите пока модель не загрузится, а затем перезагрузите текущую страницу**'
description_text = "Модель способная находить ответы на вопросы из контекста."
st.subheader(description_text)

text_question = st.text_input(label='Введите вопрос')
text_context = st.text_area(label='Введите контекст')
button = st.button('Получить ответ')


model = Model(connection_data)


if button and text_question != '' and text_context != '':
    response = model.get_answer(text_question, text_context)
    if ('error' in response):
        st.markdown(error_text, unsafe_allow_html=False)
    else:
        st.markdown(hint_text)
        st.write(f"""
                 Оценка: {response['score']}\n
                 Ответ: {response['answer']}\n
                 Ссылка для ознакомления с моделью: https://huggingface.co/AlexKay/xlm-roberta-large-qa-multilingual-finedtuned-ru
                  """)
else:
    st.markdown(hint_text)

