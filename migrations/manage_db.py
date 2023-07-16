import argparse
import os

import psycopg2


ROOT_DIR = os.path.dirname(__file__)


class DBManager:
    """
    Helper class to execute a script in a database.
    NOTE: does not handle automatically upgrading/downgrading.
    """
    def __init__(self, host: str, port: int, db_name: str, password: str):
        self.host = host
        self.port = port
        self.password = password
        self.db_name = db_name

    def reset_db(self):
        """ Drops and re-creates the instance database """
        conn = psycopg2.connect(
            host=self.host, port=self.port, dbname="postgres", user="postgres", password=self.password
        )
        cur = conn.cursor()

        # operations at database level cannot be run inside a transaction block
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

        # remove database if already exists
        cur.execute("SELECT 1 FROM pg_database WHERE datname=%s", (self.db_name,))
        if cur.fetchone():
            cur.execute(f"DROP DATABASE {self.db_name}")

        # create database
        cur.execute(f"CREATE DATABASE {self.db_name}")

    def run_sql_file(self, file_path: str):
        """ Connects to the instance database and executes the requested script file """
        conn = psycopg2.connect(
            host=self.host, port=self.port, dbname=self.db_name, user="postgres", password=self.password
        )
        cur = conn.cursor()

        file_path = os.path.join(ROOT_DIR, file_path)
        with open(file_path, "r", encoding="utf8") as fd:
            try:
                cur.execute(fd.read())
                conn.commit()
            except Exception as er:
                raise Exception(f"Failed to execute script {file_path} due to error {str(er)}")
            finally:
                cur.close()
                conn.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Creates a database and executes creation of rpn schema and tables.")
    parser.add_argument("--host", type=str, default="localhost", help="Database host to connect to")
    parser.add_argument("--port", type=int, default=5432, help="Database port to connect to")
    parser.add_argument("--dbname", type=str, default="test_rpn", help="Database name")
    parser.add_argument("--password", type=str, default="admin", help="Password of the postgres user")
    args = parser.parse_args()

    manager = DBManager(args.host, args.port, args.dbname, args.password)
    manager.reset_db()
    manager.run_sql_file("000_init_tables.sql")
