import streamlit as st
import json
from model import Model


connection_data = {
    'api_url': 'https://datasphere.api.cloud.yandex.net/datasphere/v1/nodes/5a49c54e-e206-4ab7-96b7-e37b468ce953:execute',
    'folder_id': 'b1g6ceqjotq7gji5heli',
    'token_url': 'https://functions.yandexcloud.net/d4e1q0o089bedv9kbhea'
}


st.title('Multilingual-finedtuned-ru ')
hint_text = "**Output**"
error_text = '**Нужно загрузить модель, для этого [перейдите на страницу модели](https://huggingface.co/makarshatilov/transliteration_v1), нажмите Compute, немного подождите пока модель не загрузится, а затем перезагрузите текущую страницу**'


model = Model(connection_data)

text_question = st.text_input(label='Input question')
print(text_question)


if text_question:
    text_context = st.text_area(label='Input context')
    print(text_context)

    if text_context:
        print(text_question)
        print(text_context)
        response = model.get_answer(text_question, text_context)
        print(response)
        if ('error' in response):
            st.markdown(error_text, unsafe_allow_html=False)
        else:
            st.markdown(hint_text)
            st.write(response['answer'])
    else:
        st.markdown(hint_text)
