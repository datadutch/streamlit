import streamlit as st
import snowflake.connector
import pandas as pd

@st.cache(allow_output_mutation=True)
def init_connection():
    return snowflake.connector.connect(
        user=st.secrets["snowflake"]["user"],
        password=st.secrets["snowflake"]["password"],
        account=st.secrets["snowflake"]["account"],
        warehouse=st.secrets["snowflake"]["warehouse"],
        database=st.secrets["snowflake"]["database"],
        schema=st.secrets["snowflake"]["schema"],
        role=st.secrets["snowflake"]["role"],
    )

conn = init_connection()

query = st.text_input("Enter your SQL query here")
if st.button("Run Query"):
    with conn.cursor() as cur:
        cur.execute(query)
        results = cur.fetchall()
        df = pd.DataFrame(results, columns=[desc[0] for desc in cur.description])
        st.write(df)