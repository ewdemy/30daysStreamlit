import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

st.header("st.write")
st.write("Hello *world* :sunglasses:")
st.write(12345)

df = pd.DataFrame({
    "First Column": [1,2,3,4,5],
    "Second Column": ["A","B","C","D","E"]
})

st.write(df)

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
st.write(df2)
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)