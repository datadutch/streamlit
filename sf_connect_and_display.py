import streamlit as st
from snowflake.snowpark import Session
import json

st.title('❄️ How to connect Streamlit to a Snowflake database')

# connect to Snowflake
def create_session():
    with open('../config/sf-config.json') as f:
        connection_parameters = json.load(f)  
    session = Session.builder.configs(connection_parameters).create()
    return session

session = create_session()
st.success("Connected to Snowflake!")

# Load data table
def load_data(table_name):
    ## Read in data table
    st.write(f"Here's some example data from `{table_name}`:")
    table = session.table(table_name)

    ## Do some computation on it
    table = table.limit(100)
    
    ## Collect the results. This will run the query and download the data
    table = table.collect()
    return table

# Select and display data table
table_name = "DB_STREAMLIT.PUBLIC.EMPLOYEE"

## Display data table
df = load_data(table_name)

## Writing out data
for row in df:
    st.write(f"{row[0]}, {row[1]}")