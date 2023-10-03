# .streamlit/secrets.toml

[connections.snowflake]
url = "snowflake://<user_login_name>@<account_identifier>/"

[connections.snowflake.create_engine_kwargs.connect_args]
authenticator = "externalbrowser"
warehouse = "xxx"
role = "xxx"
client_session_keep_alive = true