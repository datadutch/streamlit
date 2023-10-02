import streamlit as st
from snowflake.snowpark import Session
import json

st.title('❄️ How to connect Streamlit to a Snowflake database')

# connect to Snowflake
def create_session():
    with open('..\config.json') as f:
        connection_parameters = json.load(f)  
    session = Session.builder.configs(connection_parameters).create()
    return session

session = create_session()
st.success("Connected to Snowflake!")