This repository contains various files from the Streamlit 30 day challenge. 
Since it has been a while that I used them, I put them in a WIP folder.
Once validated, they will move a folder up

Later on, some python code was added to connect Streamlit to Snowflake
* JKT.py from the people at ENX
* SL_SF_Connect, connecting to SF and displaying records

Note: the above 2 both have different methods of connecting to SF and using difference config files, which offcourse are not in the GIT repo.

ToDo: put some empty example config files in the repo.

https://share.streamlit.io/streamlit/30days

https://share.streamlit.io/bidutch/streamlit/main/day5.py

The secrets ......

I see 3 options to make sure no secure information is stored in the python code:
* a JSON file with credentials
* ini file with credentials
* use of the Streamlit native secrets file (https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management)

Choose the method of your preference. It seems to me that once you start deploying Streamlit apps, the secrets option might be the best approach.

JSON file:

import json

def create_session():
    with open('..\config.json') as f:
        connection_parameters = json.load(f)  
    session = Session.builder.configs(connection_parameters).create()
    return session

This pattern is used in the file sf_connect.py

ini file:

# Config parser om credentials locaal op te halen
config_sf = configparser.ConfigParser()
config_sf.sections()
config_sf.read('C:\_NoBackup\Streamlit\config_sf.ini')
# mappen settings uit file naar variabele
sf_solution = 'jkooij'
sf_account = config_sf[sf_solution]['sfAccount']

secrets:

@st.cache_resource
def init_connection():
    return snowflake.connector.connect(
        **st.secrets["snowflake"], client_session_keep_alive=True
    )

conn = init_connection()
