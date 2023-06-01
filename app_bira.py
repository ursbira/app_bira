import streamlit as st
import pandas as pd
import numpy as np


st.title('Variação em 10 meses - urs.bira')

st.sidebar.title('urs.bira Indicadores')
st.sidebar.header('Selecione')

df = pd.DataFrame(np.random.rand(10, 3), columns=[
    'Variação Preço', 'Taxa de Conversão', 'Taxa de Inadimplência'])

df_price = pd.DataFrame(np.random.rand(10, 1), columns=['Preço'])


check_scale = st.sidebar.checkbox('Escala Logarítmica')

button1 = st.sidebar.button('Gráfico 1')
button2 = st.sidebar.button('Gráfico 2')
button3 = st.sidebar.button('Gráfico 3')
button4 = st.sidebar.button('Tabela Indicadores Atuais')

if button1:
    st.header('Gráfico 1')
    st.line_chart(df)

if button2:
    st.header('Gráfico 2')
    st.bar_chart(df)

if button3:
    st.header('Gráfico 3')
    st.bar_chart(df_price)

if button4:
    st.header('Tabela Indicadores Atuais')
    st.table(df)
else:
    if check_scale:
        st.container()
        st.header('Valores em escala logarítmica')
    else:
        st.header('Valores em Reais mil')



# https://www.youtube.com/watch?v=2vb22jMwiiw