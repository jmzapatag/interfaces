import streamlit as st
from PIL import Image

st.title("Mi Primera App!!")

st.header("jijijija")
st.write("no me copies anto")
image = Image.open('ralsei.png')

st.image(image, width = 200)
