import streamlit as st
from datetime import time, datetime

st.header("st.slider")
st.subheader("Slider")

st.write("Milton Fernandes")

age = st.slider("Quantos anos você tem?", 0, 130, 25)
st.write(f"Eu tenho {age} anos")

st.subheader("Slider de Intervalo")

values = st.slider("Escolha um intervalo de valores", 0.0, 100.0, (25.0,75.0))
st.write("Valores:", values)

st.subheader('Slider de intervalo de tempo')

appointment = st.slider(
    "Agende um compromisso",
    value=(time(11,30), time(12,45))
    )

st.write("O compromisso foi agenda para:", appointment)

st.subheader('Slider de data e hora')

start_time = st.slider(
    "Quando vai começar?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm"
)

st.write("Início:", start_time)