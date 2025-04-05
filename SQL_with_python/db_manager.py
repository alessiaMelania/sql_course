import logging
import sqlite3
import yaml
import os
import sys


def read_queries(path_queries: str) -> dict:
    with open(path_queries, 'r') as file:
        queries = yaml.safe_load(file)

    return queries


class SqliteManager:
    def __init__(self, database_path: str):
        self.database_path = database_path
        # Connect to the SQLite database (or create it if it doesn't exist)
        self.connection = self.start_connection()
        # In order to execute SQL statements and fetch results from SQL queries, we will need to use a database cursor.
        self.cursor = self.connection.cursor()

    def start_connection(self):
        try:
            # The returned connection object represents the connection to the on-disk database.
            return sqlite3.connect(self.database_path)
        except Exception as e:
            logging.error("Error occurred during connection, ", e)
            # exiting with a non-zero value is better for returning from an error
            sys.exit(1)

    def execute_query(self, query, value=()):
        try:
            return self.cursor.execute(query, value)
        except Exception as e:
            logging.error(f"Error occurred during query execution\n{query}\n", e)
            return

    def executemany_query(self, query, values=()):
        try:
            return self.cursor.executemany(query, values)
        except Exception as e:
            logging.error(f"Error occurred during query execution\n{query}\n", e)
            return

    def close_commit(self):
        self.connection.commit()
        # Close the database connection
        self.connection.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    # Get the pathname of the current working directory
    # print(os.getcwd())

    # Paths
    database_path = "sqlite_dbs/myFirst_db.db"
    path_queries = "queries_myFirst_db.yaml"

    # Read queries
    queries = read_queries(path_queries)

    # Connect to the SQLite database (or create it if it doesn't exist)
    db = SqliteManager(database_path)
    logging.info("Database created and connected successfully!")
    logging.info(f"{'-' * 40}\n")
    # -------------------------------------------------------------------------
    # Create Student tables
    #db.execute_query(queries["create_tables"]["students"])
    logging.info("Table 'Students' created successfully!")

    # Save (commit) the changes to the database.
    db.connection.commit()

    # Create Student tables version 2
    db.execute_query(queries["create_tables"]["students_v2"])
    logging.info("Table 'Students' created successfully!")

    # Save (commit) the changes to the database.
    db.connection.commit()
    logging.info(f"{'-' * 40}\n")
    # -------------------------------------------------------------------------

    # Insert a record into the Students table
    logging.info("Insert a record into the Students table")
    db.execute_query(queries["insert_data"]["insert_single_record"])
    logging.info("Record inserted successfully!")

    # Save (commit) the changes to the database.
    db.connection.commit()

    # Insert a record into the Students table version 2
    logging.info("Insert a record into the Students table version 2")
    query = queries["insert_data_query&values"]["insert_single_record"]["query"]
    value = queries["insert_data_query&values"]["insert_single_record"]["value"]

    db.execute_query(query, value)
    logging.info("Record inserted successfully!")

    # Save (commit) the changes to the database.
    db.connection.commit()
    logging.info(f"{'-'*40}\n")
    # -------------------------------------------------------------------------

    # Insert multiple records into the Students table
    logging.info("Insert multiple records into the Students table")
    db.execute_query(queries["insert_data"]["insert_multiple_records"])
    logging.info("Records inserted successfully!")

    # Save (commit) the changes to the database.
    db.connection.commit()

    # Insert multiple records into the Students table version 2
    logging.info("Insert multiple records into the Students table version 2")
    query = queries["insert_data_query&values"]["insert_multiple_records"]["query"]
    values = queries["insert_data_query&values"]["insert_multiple_records"]["values"]

    for item in values:
        db.execute_query(query, item)
        logging.info("Record inserted successfully!")

    # Save (commit) the changes to the database.
    db.connection.commit()

    # Insert multiple records into the Students table version 3
    logging.info("Insert multiple records into the Students table version 3")
    query = queries["insert_data_query&values"]["insert_multiple_records"]["query"]
    values = queries["insert_data_query&values"]["insert_multiple_records"]["values"]

    db.executemany_query(query, values)
    logging.info("Records inserted successfully!")

    # Save (commit) the changes to the database.
    db.connection.commit()
    logging.info(f"{'-' * 40}\n")
    # -------------------------------------------------------------------------


    # -------------------------------------------------------------------------


    # -------------------------------------------------------------------------


    # -------------------------------------------------------------------------

    db.close_commit()
    logging.info("Database closed successfully!")
    logging.info(f"{'-' * 40}\n")
