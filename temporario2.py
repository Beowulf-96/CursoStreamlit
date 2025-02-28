import streamlit as st

st.title("Cadastro de Aluno")

st.write("Preencha o formulário abaixo para cadastrar um aluno:")

with st.form(key='form_cadastro'):
    nome = st.text_input("Nome do Aluno")
    curso = st.text_input("Curso")
    email = st.text_input("Email")
    matricula = st.text_input("Número de Matrícula")
    Pai = st.text_input("Pai")
    Mãe = st.text_input("Mãe")
    cpf = st.text_input('Digite seu CPF:', '')

if cpf and len(cpf) != 11:
    st.error('CPF deve conter 11 dígitos.')

data_nascimento = st.date_input('Escolha sua data de nascimento:')

if st.button('Enviar'):
    if cpf and len(cpf) == 11:
        st.write(f'CPF: {cpf}')
        st.write(f'Data de Nascimento: {data_nascimento}')
    else:
        st.error('Preencha corretamente o CPF.')
    
   
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
