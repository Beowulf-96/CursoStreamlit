import streamlit as st
st.title('Cadastro de Funcionário')
nome = st.text_input("Digite o nome:")
sobrenome = st.text_input("Digite o sobrenome:")
dia = st.number_input("Digite o dia do nascimento:")
mes = st.number_input("Digite o mês do nascimento:")
ano = st.number_input("Digite o ano do nascimento:")
st_civil = st.selectbox("Digite o estado civil:", ['Solteiro(a)', 'Casado(a)', 'Divorciado(a)', 'Viúvo(a)'])
sexo = st.selectbox("Digite o sexo:", ['Masculino', 'Feminino', 'Outro'])
salario = st.number_input("Digite o salário:")
aumento = 0
salario_final = 0
if salario <= 2500:
    st.write("Recebe aumento!")
    while aumento < 500:
        aumento += 100
    salario_final = salario + aumento
else:
    st.write("Não necessita de aumento!")
    salario_final = salario
if st.button('Confirmar Cadastro'):
    st.subheader('Dados do Funcionário:')
    st.write(f"Nome: {nome} {sobrenome}")
    st.write(f"Data de Nascimento: {dia}/{mes}/{ano}")
    st.write(f"Estado Civil: {est_civil}")
    st.write(f"Sexo: {sexo}")
    st.write(f"Salário Final: R${salario_final}")
