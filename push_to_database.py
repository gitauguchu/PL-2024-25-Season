from scrape import *
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

functions = [league_table, top_scorers, detail_top, player_table, all_time_table, all_time_winner_club, top_scorers_seasons, goals_per_season]

#Retrieving the database connection string from environment variables
conn_string = os.getenv('CONN_STRING')
                 
#Creating a database engine
db = create_engine(conn_string)
#Establishing a database connection
conn = db.connect()

#Loop through the list of functions and push data to the database for fun in functions
for fun in functions:
    function_name = fun.__name__
    #Call the function to get the DataFrame
    result_df = fun()
    #Push the DataFrame to the database table with the function name as the table name
    result_df.to_sql(function_name, con = conn, if_exists = 'replace', index = False)
    print(f'Pushed data for {function_name}')

#Close the database connection
conn.close()