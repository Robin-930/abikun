import streamlit as st
owo = 'kkk'
st.title("Robin fr life")
if st.button('Say hello', type= 'secondary'):
    robin = input("gimme ur money")
    st.text_input(robin)
    
    st.write("why hello there")

with open('abhijith.jpeg', 'rb') as file:
    st.download_button(file_name= 'abhijith.jpeg',
                       label= 'abi hot pics',
                       data= file)