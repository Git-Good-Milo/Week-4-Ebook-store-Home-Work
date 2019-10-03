import pyodbc
# In this file well make our connection

server = 'localhost,1433'
database = 'Ebook'
username = 'SA'
password = 'Passw0rd2018'

# Estabilsh connection
conn_ebdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
#print(conn_nwdb)
cursor = conn_ebdb.cursor()