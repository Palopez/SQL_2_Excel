# Created by pablo.lopez
#Global variables#
import pyodbc
import pandas as pd
export_file = 'export.xlsx'
#end of global variables#
#--#
#Connection to the database. Put credentials of the db. db name, user, password and driver type
cnxn = pyodbc.connect("Driver={SQL Server};SERVER=server_name;Database=database_name;UID=database_user;PWD=database_password")

script = """
SELECT * FROM database;
"""
df = pd.read_sql_query(script, cnxn)
writer = pd.ExcelWriter(export_file)
df.to_excel(writer, sheet_name='Sheet1', index = False)
writer.save()
