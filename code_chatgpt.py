import streamlit as st
import pandas as pd
import snowflake.connector

@st.cache_resource
def init_connection():
    return snowflake.connector.connect(
        **st.secrets["snowflake"], client_session_keep_alive=True
    )

conn = init_connection()

text_input = st.text_input('Enter your text here')
df = pd.DataFrame({'Text': [text_input]})
st.write(df)

snowflake.connector.pandas_tools.write_pandas(conn, df, '<table>')