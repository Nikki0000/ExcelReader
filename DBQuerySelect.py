from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import pandas as pd

class DBQuerySelect:
    def __init__(self, db_connection):
        self.engine = create_engine(db_connection)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def select_query(self, table_name):
        query = text(f'SELECT * FROM "{table_name}"')
        try:
            result = self.session.execute(query)
            data = result.fetchall()
            columns = result.keys()
            return pd.DataFrame(data, columns=columns)
        except Exception as e:
            print(f"Error select query: {e}")
            return None
    
    def save_to_excel(self, dataframe, output_file):
        try:
            dataframe.to_excel(output_file, index=False)
        except Exception as e:
            print(f"Error saving file: {e}")
    