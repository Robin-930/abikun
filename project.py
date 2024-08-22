import streamlit as st
owo = 'kkk'
st.title(":blue[Hackathon 2024]  😂", )
st.write()
hide_st_style ="""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>"""

st.markdown(hide_st_style, unsafe_allow_html=True)


owo = st.text_input('')

if st.button('say hello'):
    st.write('Hello there' , owo)
        

with open('gowtham.jpeg', 'rb') as file:
    st.download_button(file_name= 'gowtham.jpeg',
                       label= 'Gowtham pics',
                       data= file)
with open('anush.jpeg', 'rb') as file:
    st.download_button(file_name= 'anush.jpeg',
                       label= 'anush pics',
                       data= file)
    
