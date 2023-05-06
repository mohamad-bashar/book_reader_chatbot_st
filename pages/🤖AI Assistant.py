import openai
import streamlit as st
from streamlit_chat import message
import os

# Setting page title and header
st.set_page_config(page_title="Book Reader AI Helper",
                   page_icon=":robot_face:")
st.markdown("<h1 style='text-align: center;'>A friendly assistant to use Book Reader program.</h1>",
            unsafe_allow_html=True)

openai.api_key = os.getenv("OPENAIAPI")

# Initialise session state variables
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": f"You are a bot that only answers questions related to a program called Book Reader or قارئ الكتب. Provide very positive positive, helpful, short and exiting responses, do not answer anything unrelated to the Book Reader programand you summarize text. Data: The Book Reader program was created by Mohammed Bashar Jalal, a 15 years old student at the National Charity School Samnan, the purpose: help students in their learning journey It was programmed in Python. it converts books to audio in multiple languages: English, Arabic, German, Spanish, Hindi, Japanese, Italian, and French. It can extract text from PDF and TXT files and display it in the text box. The Wikipedia icon opens a window to search and extract information from Wikipedia articles by title. The program requires an Internet connection to function properly. An error message will appear if there is no connectivity or other issues. The program has an internal audio player, the app is not responsive but You can change the font size of the text box using the arrows. It can translate between the supported languages. The 'AI' button activates an AI summarization feature, You can save the audio file in MP3 format using the 'Save File' button. Wikipedia will open in any of the supported languages. You cannot adjust the playback speed, but you can choose between 'fast' and 'slow' options. Arabic data: .تم تطوير برنامج ‘قارئ الكتب’ بواسطة الطالب محمد بشار جلال من المدرسة الأهلية الخيرية سمنان باستخدام لغة البرمجة بايثون. يقوم البرنامج بتحويل المقالات والكتب العلمية إلى كلام صوتي مقروء ويعتبر صديقا للطالب في الدراسة والتعلم بشكل عام. ويستخدم البرنامج تقنيات مفيدة للبحث عن المعلومات في موقع ويكيبيديا ونقلها بشكل فوري للبرنامج، بالإضافة إلى قراءة من ملفات التكست والبي دي أف, يتميز البرنامج بقدرته على الترجمة وتلخيص الملفات باستخدام الذكاء الاصطناعي، ويمكنه قراءة النصوص بسبع لغات مختلفة، مما يساعد الطلاب في التعلم بطريقة أسهل وأكثر فعالية. Please only provide helpful information related to the Book Reader program based on this prompt and data. Do not answer anything unrelated."}
    ]


# generate a response
def generate_response(prompt):
    st.session_state['messages'].append({"role": "user", "content": prompt})

    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=st.session_state['messages'],
        max_tokens=550,
        temperature=0.15
    )
    response = completion.choices[0].message.content
    st.session_state['messages'].append(
        {"role": "user", "content": response})

    return response


# container for chat history
response_container = st.container()
# container for text box
container = st.container()

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            p {font-size: 1.27rem;}
            #text {font-size: calc(1.6rem + .6vw);}
            .st-af {font-size: 1.2rem;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

with container:
    with st.form(key='my_form', clear_on_submit=True):
        col1, col2 = st.columns([9, 2])
        with col1:
            user_input = st.text_input(' ', label_visibility='collapsed', key='input',
                                       placeholder="Ask any thing you want")
        with col2:
            submit_button = st.form_submit_button(label='📬 Send')

    if submit_button and user_input:
        output = generate_response(
            user_input)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)

if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i],
                    is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))
