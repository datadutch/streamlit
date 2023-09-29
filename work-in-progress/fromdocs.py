# https://docs.streamlit.io/knowledge-base/tutorials/databases/snowflake
# fromdocs.py

import streamlit as st

# Initialize connection.
conn = st.experimental_connection('snowflake')

# Perform query.
df = conn.query('SELECT * from mytable;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.NAME} has a :{row.PET}:")