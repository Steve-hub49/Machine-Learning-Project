import os
import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = os.environ['DATABASE_URL']
TABLE_NAME = os.environ['TABLE_NAME']

df = pd.read_csv('insurance_claims.csv', na_values=['?'])

# create an engine that can talk to the database
engine = create_engine(DATABASE_URL)
conn = engine.connect()

df.to_sql(TABLE_NAME, engine, if_exists='replace') 
# sqlalchemy will not detect table without PK. This seems to be the best solution (https://stackoverflow.com/q/50469391)
engine.execute(f'ALTER TABLE {TABLE_NAME} ADD PRIMARY KEY (policy_number);')