import streamlit as st
import snowflake.connector

# Load Snowflake credentials from config.toml
snowflake_config = st.secrets["snowflake"]
account_name = snowflake_config["accountname"]
user_name = snowflake_config["username"]
password = snowflake_config["password"]
warehouse_name = snowflake_config["warehousename"]
database_name = snowflake_config["databasename"]
schema_name = snowflake_config["schemaname"]

# Connect to Snowflake
conn = snowflake.connector.connect(
    account=account_name,
    user=user_name,
    password=password,
    warehouse=warehouse_name,
    database=database_name,
    schema=schema_name
)

# Execute a query
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM my_table")
result = cur.fetchone()[0]

# Display the result
st.write(f"Result: {result}")