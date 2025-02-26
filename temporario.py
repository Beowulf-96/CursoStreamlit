import streamlit as st
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
