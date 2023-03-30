import streamlit as st
import pandas as pd

text_input = st.text_input('Enter your text here')
df = pd.DataFrame({'Text': [text_input]})
st.write(df)