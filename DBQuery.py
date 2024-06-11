import psycopg2 

class DBQuery:
    def __init__(self, db_config):
        self.db_config = db_config
        self.connection = None
        self.cursor = None

    def connect(self, db_name):
        conn_str = self.db_config.get(db_name)
        if not conn_str:
            print(f"DataBase not found")
        self.connection = psycopg2.connect(conn_str)
        self.cursor = self.connection.cursor
        print(f"Connect to DataBase {db_name}")


    
    def select_query(self, values):
        inserted_ids = []
        query = """

        """
    