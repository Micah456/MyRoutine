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

def create_object(table, object_dict):
    '''
    Creates a row in a specified table in the database using
    provided data
    @param table: Table to insert object into
    @param object_dict: dict containing data to insert into database
    @returns: True if successful, False if not or if user already exists
    '''
    print("######## DataTransfer: Create Object #########")
    columns = parse_keys_and_values(object_dict).get('columns')
    values = parse_keys_and_values(object_dict).get('values')
    statement = "INSERT INTO " + table + " (" + columns + ") VALUES (" + values + ")"
    print("####### DataTransfer: Create Object - Statement: \n" + statement + "\n##########")
    return execute_statement(statement)


def parse_keys_and_values(object_dict):
    '''
    Parses the object_dict to make two strings of keys and
    values to use in sql insert statements.
    This only supports int and str variables.
    @param object_dict: dict containing data to parse
    @returns: dict containing columns and values as strings
    for sql statements.
    '''
    keys = list(object_dict.keys())
    columns_str = ""
    for key in keys:
        columns_str += "[" + key + "], "
    columns_str = columns_str[0:len(columns_str)-2]
    # extra -2 to cut out last ', '
    values = str(list(object_dict.values()))
    values_str = values[1:len(values)-1]
    return {"columns": columns_str, "values": values_str}


def execute_statement(statement):
    ''' Executes an sql statement to the database 
        @param statement: string containing statement
        @returns: True if successful. False if not.
    '''
    try:
        cnxn = pyodbc.connect(conn_str)
        cursor = cnxn.cursor()
        cursor.execute(statement)
        cnxn.commit()
        return True
    except:
        print(traceback.format_exc)
        return False
    

def execute_multiple_statements(statement_list):
    ''' Executes multiple sql statements to the database.
        Each statement is printed before it is executed.
        @param statement_list: list of statement strings
        @returns: True if successful. False if not.
    '''
    try:
        cnxn = pyodbc.connect(conn_str)
        cursor = cnxn.cursor()
        for statement in statement_list:
            print("STATEMENT: " + statement)
            cursor.execute(statement)
        cnxn.commit()
        return True
    except:
        print(traceback.format_exc)
        return False
    