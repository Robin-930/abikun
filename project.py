import streamlit as st
owo = 'kkk'
st.title("Robin fr life")
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
    
