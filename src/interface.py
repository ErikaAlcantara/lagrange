import streamlit as st
import numpy as np
import pandas as pd
from streamlit.server.server import Server
from lagrange import Lagrange


st.title("Interpolação Polinomial de Lagrange")
st.write("#")

st.write("## Pontos no cartesiano:")
st.write("#")


df = pd.DataFrame({

'x0   ': [-2],
'x1   ': [0],
'x3   ': [4]
})


df

df2 = pd.DataFrame({

'f(x0)': [2],
'f(x1)': [-2],
'f(x3)': [1]
})

df2
st.write("#")

col1, col2 = st.columns(2)
with col1:
    x = st.number_input("x: ", min_value = -99, max_value=99, value=0, step=1)
    lagrange = Lagrange(x)

with col2:
    st.write("#")
    st.write("P(x): " + str(lagrange.solve_polynomial()))


