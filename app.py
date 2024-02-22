import streamlit as st
from PIL import Image

st.title("Mi Primera App!!")

st.header("jijijija")
st.write("no me copies anto")
image = Image.open('ralsei.png')

st.image(image, caption ='Ralsei my beloved')


texto = st.text_input('hola', 'hola2')
st.write('El texto escrito es', texto)

st.subheader("ahora usemos dos columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las Interfaces multimodales mejoran la experiencia de usuario")
  resp = st.checkbox("Estoy ed acuerdo")
  if resp:
    st.write('Correcto!')
