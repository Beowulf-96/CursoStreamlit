import streamlit as st
import pandas as pd
st.header("Cabeçalho")
st.toggle("abc")
st.text_area("Enter text")
st.text_input("abc")
st.selectbox(
  'Qual sua cor favorita?',
  ('Azul', 'Vermelho', 'Verde'))
st.button("Botão Salvar")
st.multiselect(
  'Quais são as suas cores favoritas?',
  ['Verde', 'Amarelo', 'Vermelho', 'Azul'],
  ['Amarelo', 'Vermelho'])

st.checkbox('Sorvete')
st.checkbox('Café')
st.checkbox('Refrigerante')

st.color_picker("Pick A Color", "#00f900")
st.feedback("stars")

df = pd.DataFrame(
  [
    {"command": "st.selecbox", "rating": 4, "is_widget": True},
    {"command": "st.balloons", "rating": 5, "is_widget": False},
    {"command": "st.time_input", "rating": 3, "is_widget": True},
  ]
)
edited_df = st.data_editor(df)
