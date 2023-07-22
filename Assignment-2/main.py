from db_connector import MySQLConnector

# Replace these values with your database credentials
host = "your_host"
user = "your_username"
password = "your_password"
database = "your_database_name"

# Create an instance of the MySQLConnector class
connector = MySQLConnector(host, user, password, database)

# Connect to the database
connector.connect()

# Example: Insert a record into the "users" table
data_to_insert = {"name": "John Doe", "email": "john.doe@example.com", "age": 30}
connector.create("users", data_to_insert)

# Example: Update a record in the "users" table
data_to_update = {"age": 31}
condition = "name = 'John Doe'"
connector.update("users", data_to_update, condition)

# Example: Select records from the "users" table
columns_to_select = "name, email"
condition_to_select = "age > 25"
result = connector.select("users", columns_to_select, condition_to_select)
print(result)

# Example: Delete a record from the "users" table
condition_to_delete = "name = 'John Doe'"
connector.delete("users", condition_to_delete)

# Example: Auto-create query for insert
data_to_auto_create = {"name": "Alice", "email": "alice@example.com", "age": 28}
insert_query = connector.auto_create_query("users", data_to_auto_create)
print(insert_query)

# Example: Auto-create bulk insert query
data_list_to_auto_create_bulk = [
    {"name": "Bob", "email": "bob@example.com", "age": 25},
    {"name": "Eve", "email": "eve@example.com", "age": 23}
]
bulk_insert_query = connector.auto_create_bulk_insert_query("users", data_list_to_auto_create_bulk)
print(bulk_insert_query)

# Example: Run a stored procedure
procedure_name_to_run = "sp_update_age"
args_to_run = (30,)
connector.run_procedure(procedure_name_to_run, args_to_run)

# Disconnect from the database
connector.disconnect()
