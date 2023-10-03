import streamlit as st
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import pd_writer
from snowflake.connector.pandas_tools import write_pandas

@st.cache_resource
def init_connection():
    return snowflake.connector.connect(
        **st.secrets["snowflake"], client_session_keep_alive=True
    )

conn = init_connection()

text_input = st.text_input('Enter your decimal here')
df = pd.DataFrame({'Decimal': [text_input]})
df = df.rename(columns={"Decimal": "SLEUTEL"})
st.write(df)

success, nchunks, nrows, _ = write_pandas(conn, df, 'MYTABLE')