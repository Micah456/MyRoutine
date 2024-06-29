import os
import pyodbc
import traceback
from dotenv import load_dotenv

load_dotenv()
server = os.getenv("server")
database = os.getenv("database")
user_table = os.getenv("user_table")
routine_table = os.getenv("routine_table")
step_table = os.getenv("step_table")


conn_str = "Driver=SQL Server;Server=" + server + ";Database=" + database + ";Trusted_Connection=yes;"