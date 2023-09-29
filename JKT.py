import configparser 
import pandas as pd 
import numpy as np
from snowflake.connector import connect
import sys
import os
import getpass
from streamlit.web import cli as stcli
from streamlit import runtime
import streamlit as st 

st.set_page_config(layout="wide")

# Config parser om credentials locaal op te halen
config_sf = configparser.ConfigParser()
config_sf.sections()
config_sf.read('C:\_NoBackup\Streamlit\config_sf.ini')
# mappen settings uit file naar variabele
sf_solution = 'jkooij'
sf_account = config_sf[sf_solution]['sfAccount']
sf_user = config_sf[sf_solution]['sfUser']
sf_database = config_sf[sf_solution]['sfDatabase']
sf_warehouse = config_sf[sf_solution]['sfWarehouse']
sf_role = config_sf[sf_solution]['sfRole']
sf_schema = config_sf[sf_solution]['sfSchema']
sfAuthenticator = config_sf[sf_solution]['sfAuthenticator']

#connect to snowflake
con = connect(
user = sf_user,
account = sf_account,
authenticator= sfAuthenticator,
)

cur = con.cursor()
cur.execute (f'use role {sf_role}')
cur.execute (f'use warehouse {sf_warehouse}')
cur.execute (f'use database {sf_database}')


def main():


    # first configure the streamlit page
    row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1,2.3,.1,1.3,.1))

    with row0_1:
        st.title('FlatFile uploader')

    with row0_2:
        st.text("")
        st.subheader('Selecteer te verwerken flatfiles')
    row3_spacer1, row3_1, row3_spacer2 = st.columns((.1,3.2,.1)) 

    with row3_1:
        st.markdown("Via de pagina wordt het mogelijk om een Flatfile te uploaden naar S3 voor verwerking in het EDP")
        st.markdown("Links kan een Flatfile tabel worden gekozen. De inhoud van deze tabel wordt op het scherm getoond")
        st.markdown("Daaronder kan een Flatfile worden geupload. Deze inhoud wordt ook getoond op het scherm")

    st.sidebar.text('')
    st.sidebar.text('')
    st.sidebar.text('')
    st.sidebar.markdown('**Kies de Flatfile tabel**')

    # Number input
    number = st.number_input('Insert a number', value=50)
    st.write('The current number is ', number)

    # Get all Flatfile tables to choose from

    sqlGetFF = "SELECT distinct TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'CDWH_2_STG_FF'"
    df_sqlFFTables = fetchPD(cur, sqlGetFF)

    selecteerFF = st.sidebar.selectbox('Kies hieronder een Flatfile tabel', df_sqlFFTables)

    st.Write = (selecteerFF, 'geselecteerd')
    

    # Toon nu de data
    row6_spacer1, row6_1, row6_spaces2 = st.columns((.2,7.1, .2))

    with row6_1:
        st.subheader('Geselecteerde tabel:', selecteerFF)

    #st.dataframe(df_sqlFFTables)
    
def fetchPD(cur, sql):
    cur.execute(sql)
    result=cur.fetchall()
    col_names = []
    for elt in cur.description:
        col_names.append(elt[0])
    pandadf=pd.DataFrame(result, columns=col_names)
    return pandadf

if __name__ == '__main__':
    if runtime.exists():
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
