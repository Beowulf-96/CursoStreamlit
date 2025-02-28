import streamlit as st

st.title("Cadastro de Aluno")

st.write("Preencha o formulário abaixo para cadastrar um aluno:")

with st.form(key='form_cadastro'):
    nome = st.text_input("Nome do Aluno")
    idade = st.number_input("Idade", min_value=1, max_value=100, step=1)
    curso = st.text_input("Curso")
    email = st.text_input("Email")
    matricula = st.text_input("Número de Matrícula")
    
   
    semestre = st.selectbox("Semestre", ["1º Semestre", "2º Semestre", "3º Semestre", "4º Semestre", "5º Semestre"])

    submit_button = st.form_submit_button("Cadastrar Aluno")


    if submit_button:
       
        st.success("Aluno cadastrado com sucesso!")
           
        st.write(f"Nome: {nome}")
        st.write(f"Idade: {idade}")
        st.write(f"Curso: {curso}")
        st.write(f"Email: {email}")
        st.write(f"Matrícula: {matricula}")
        st.write(f"Semestre: {semestre}")
