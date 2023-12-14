import yaml
import pandas as pd
from pandas import DataFrame
from sqlalchemy import create_engine
  

print("hELLOW")
def load_creds():
        with open('/workspaces/exploratory-data-analysis---customer-loans-in-finance632/.gitignore/credentials.yaml', 'r') as file:
            credentials = yaml.safe_load(file)
        return credentials
credentials = load_creds()
print(credentials)

""""

class RDSDatabaseConnector():

    def engine_creation(self):
        RDSDatabaseConnector.load_creds()
        engine = create_engine(self.credentials)

        conn = engine.connect('loan_payments') 
        sql_query = pd.read_sql_query ('''
                                       SELECT *
                                       FROM {table}
                                       ''', conn)
        df = pd.DataFrame(sql_query)
        return df
        
    def __init__(self, credentials):
        self._credentials = credentials
"""