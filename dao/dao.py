from flask import current_app
import mysql.connector
from utility.utils import Utils


class DAO:
    def __init__(self):
        # Removed db reference, now using direct connection management
        from app import app  # Assuming app instance is created in app.py
        self.app = app

    def get_db_connection(self):
        """ Returns a database connection object """
        return mysql.connector.connect(
            host=self.app.config['MYSQL_HOST'],
            user=self.app.config['MYSQL_USER'],
            password=self.app.config['MYSQL_PASSWORD'],
            database=self.app.config['MYSQL_DB']
        )

    def insert(self, service: str, table_name: str, data: dict):
        """ Insert data into a table """
        data[f"{Utils.get_id_field(service)}"] = Utils.generate_id(service)

        columns = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))  # Prepare for parameterized query
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"

        current_app.logger.info(f"INSERT: {sql}")
        
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
        cursor = conn.cursor(dictionary=True)  # Use dictionary cursor for readable results
        cursor.execute(sql, tuple(filters.values()))
        result = cursor.fetchone()  # Use fetchall() for multiple results
        cursor.close()
        conn.close()
        return result

    def read_list(self, table_name, filters):
        """ Get all records based on a field and its value """
        conditions = ' AND '.join([f"{key} = %s" for key in filters.keys()])
        sql = f"SELECT * FROM {table_name} WHERE {conditions}"
        current_app.logger.info(f"READ LIST QUERY: {sql}")
        conn = self.get_db_connection()
        cursor = conn.cursor(dictionary=True)  # Use dictionary cursor for readable results
        cursor.execute(sql, tuple(filters.values()))
        results = cursor.fetchall()  # Fetch all rows
        cursor.close()
        conn.close()
        return results

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
        sql = f"UPDATE {table_name} SET is_active = 0 WHERE {key} = %s"
        
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
