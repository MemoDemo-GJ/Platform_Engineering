import mysql.connector

class MySQLConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Connected to MySQL-MariaDB database!")
        except mysql.connector.Error as e:
            print("Error connecting to MySQL-MariaDB database:", e)

    def disconnect(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("MySQL-MariaDB connection closed.")

    def create(self, table, data):
        try:
            placeholders = ', '.join(['%s'] * len(data))
            columns = ', '.join(data.keys())
            query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders});"
            self.cursor.execute(query, tuple(data.values()))
            self.connection.commit()
            print("Record inserted successfully!")
        except mysql.connector.Error as e:
            print("Error inserting data:", e)

    def update(self, table, data, condition):
        try:
            set_values = ', '.join([f"{column} = %s" for column in data.keys()])
            query = f"UPDATE {table} SET {set_values} WHERE {condition};"
            self.cursor.execute(query, tuple(data.values()))
            self.connection.commit()
            print("Record updated successfully!")
        except mysql.connector.Error as e:
            print("Error updating data:", e)

    def select(self, table, columns="*", condition=""):
        try:
            query = f"SELECT {columns} FROM {table}"
            if condition:
                query += f" WHERE {condition}"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except mysql.connector.Error as e:
            print("Error selecting data:", e)
            return []

    def delete(self, table, condition):
        try:
            query = f"DELETE FROM {table} WHERE {condition};"
            self.cursor.execute(query)
            self.connection.commit()
            print("Record deleted successfully!")
        except mysql.connector.Error as e:
            print("Error deleting data:", e)

    def auto_create_query(self, table, data):
        # Assuming data is a dictionary with key-value pairs for columns and values
        try:
            placeholders = ', '.join(['%s'] * len(data))
            columns = ', '.join(data.keys())
            query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders});"
            return query
        except Exception as e:
            print("Error auto-creating query:", e)
            return ""

    def auto_create_bulk_insert_query(self, table, data_list):
        # Assuming data_list is a list of dictionaries with key-value pairs for columns and values
        try:
            if not data_list:
                return ""
            columns = ', '.join(data_list[0].keys())
            placeholders = ', '.join(['%s'] * len(data_list[0]))
            query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            query_values = ', '.join(self.cursor.mogrify("(%s)" % ', '.join(['%s'] * len(data)), tuple(item.values())).decode('utf-8') for item in data_list)
            query += f" VALUES {query_values};"
            return query
        except Exception as e:
            print("Error auto-creating bulk insert query:", e)
            return ""

    def run_procedure(self, procedure_name, args=None):
        try:
            if args:
                args_str = ', '.join(['%s'] * len(args))
                self.cursor.callproc(procedure_name, args)
            else:
                self.cursor.callproc(procedure_name)
            self.connection.commit()
            print("Procedure executed successfully!")
        except mysql.connector.Error as e:
            print("Error executing procedure:", e)
