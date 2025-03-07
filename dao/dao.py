from flask import current_app
import mysql.connector
from mysql.connector.pooling import MySQLConnectionPool
from utility.utils import Utils


class DAO:
    def __init__(self):
        # Removed db reference, now using direct connection management
        from app import app  # Assuming app instance is created in app.py
        self.app = app
        self.pool = MySQLConnectionPool(
            pool_name="mypool",
            pool_size=15,
            host=self.app.config['MYSQL_HOST'],
            user=self.app.config['MYSQL_USER'],
            password=self.app.config['MYSQL_PASSWORD'],
            database=self.app.config['MYSQL_DB']
        )

    def get_db_connection(self):
        """ Returns a database connection object from the pool """
        return self.pool.get_connection()

    def insert(self, table_name: str, data: dict):
        """ Insert data into a table """
        data[f"{Utils.get_id_field(table_name)}"] = Utils.generate_id(
            table_name)

        columns = ', '.join(data.keys())
        # Prepare for parameterized query
        values = ', '.join(['%s'] * len(data))
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"

        current_app.logger.info(f"INSERT: {sql}")
        current_app.logger.info(f"INSERT DATA: {data}")

        conn = self.get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(sql, tuple(data.values()))
            conn.commit()
            return data
        except Exception as e:
            current_app.logger.error(f"INSERT ERROR: {e}")
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()


    def read(self, table_name, filters):
        """ Get a record from a table based on multiple search fields (filters) """
        conditions = ' AND '.join([f"{key} = %s" for key in filters.keys()])
        sql = f"SELECT * FROM {table_name} WHERE {conditions}"

        conn = self.get_db_connection()
        # Use dictionary cursor for readable results
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute(sql, tuple(filters.values()))
            result = cursor.fetchone()  # Fetch one row
            cursor.fetchall()  # Consume the remaining rows, if any
            return result
        except Exception as e:
            print(f"Error during read operation: {e}")
            raise
        finally:
            cursor.close()
            conn.close()

    def read_list(self, table_name, filters):
        """
        Get multiple records from a table based on multiple search fields (filters).
        """
        conditions = ' AND '.join([f"{key} = %s" for key in filters.keys()])
        sql = f"SELECT * FROM {table_name} WHERE {conditions}"

        conn = self.get_db_connection()
        cursor = conn.cursor(dictionary=True)  # Use dictionary cursor for readable results

        try:
            cursor.execute(sql, tuple(filters.values()))
            results = cursor.fetchall()  # Fetch all matching rows
            return results
        except Exception as e:
            print(f"Error during read_list operation: {e}")
            raise  # Re-raise the exception to let the caller handle it
        finally:
            cursor.close()
            conn.close()

    def read_all(self, query):
        """
        Get all records from a table based on a query.
        """
        conn = None
        cursor = None
        try:
            conn = self.get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query)
            results = cursor.fetchall()
            return results
        except Exception as e:
            # Log the exception here if needed
            current_app.logger.error(f"Error in read_all: {e}")
            raise  # Re-raise the exception to propagate it further
        finally:
            # Ensure resources are released properly
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def update(self, table_name, key, value, data):
        """ Update a record in a table based on key-value pair """
        set_clause = ', '.join([f"{column} = %s" for column in data.keys()])
        sql = f"UPDATE {table_name} SET {set_clause} WHERE {key} = %s"

        conn = self.get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(sql, tuple(data.values()) + (value,))
            conn.commit()
            return True
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()

    def delete(self, table_name, key, value):
        """ Delete a record from a table based on key-value pair (soft delete) """
        sql = f"UPDATE {table_name} SET is_active = 0 WHERE {key} = %s AND is_active = 1"

        conn = self.get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(sql, (value,))
            conn.commit()
            return True
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()
