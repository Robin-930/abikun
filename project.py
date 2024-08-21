import streamlit as st
owo = 'kkk'
st.title("Robin fr life")

st.header("Ahoy!")
hide_st_style =""""""

st.markdown(hide_st_style, unsafe_allow_html=True)



if st.button('Say hello', type= 'secondary'):
    robin = input("gimme ur money")
    st.text_input(robin)
    
    st.write("why hello there")


with open('gowtham.jpeg', 'rb') as file:
    st.download_button(file_name= 'gowtham.jpeg',
                       label= 'Gowtham hot pics',
                       data= file)
with open('anush.jpeg', 'rb') as file:
    st.download_button(file_name= 'anush.jpeg',
                       label= 'anush hot pics',
                       data= file)
    
