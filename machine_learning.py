import os
import numpy as np
import pandas as pd
from sqlalchemy import create_engine


DATABASE_URL = os.environ['DATABASE_URL']
TABLE_NAME = os.environ['TABLE_NAME']

pd.options.display.max_columns = 50

engine = create_engine(DATABASE_URL)
conn = engine.connect()
p3csv = pd.read_sql(TABLE_NAME, conn)
# print(p3csv.head())

# print(p3csv.isna().sum())

y = p3csv['fraud_reported']
print(y)

X = p3csv.drop(columns = ['fraud_reported'])
X

state = X['policy_state'].value_counts()
state

csl = X['policy_csl'].value_counts()
csl

deductable = X['policy_deductable'].value_counts()
deductable

umbrella = X['umbrella_limit'].value_counts()
umbrella

fraudumbrella = p3csv.loc[(p3csv['fraud_reported'] == 'Y') & (p3csv['umbrella_limit'] > 0)]
fraudumbrella

umbrella_limit = fraudumbrella['umbrella_limit'].value_counts()
umbrella_limit

