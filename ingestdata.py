import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import psycopg2
import os

passw = os.getenv('PASSWORD')
user=os.getenv('USERNAME')


## First connect postgresql
engine=create_engine('postgresql://user:passw@localhost:5433/banking')

customer=pd.read_csv('data/Banking.csv')
#print(customer.head())

customer.columns = [x.lower().replace(' ','_') for x in customer.columns]
print(customer.head())

# ingest data 
customer.to_sql(name='customers',con=engine,if_exists="replace")
print('done')
