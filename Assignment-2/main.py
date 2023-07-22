from db_connector import MySQLConnector

# Replace these values with your database credentials
host = "localhost"
user = "root"
password = ""
database = "sample_db"

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

# Auto create insert query
data_to_auto_create_insert = {"name": "Alice", "email": "alice@example.com", "age": 30}
insert_query, insert_values = connector.auto_create_insert("users", data_to_auto_create_insert)
connector.execute_insert(insert_query, insert_values)

# Example: Auto-create bulk insert query
data_list_to_auto_create_bulk = [
    {"name": "Bob", "email": "bob@example.com", "age": 25},
    {"name": "Eve", "email": "eve@example.com", "age": 23}
]
bulk_insert_query, bulk_insert_values = connector.auto_create_bulk_insert_query("users", data_list_to_auto_create_bulk)
connector.execute_bulk_insert(bulk_insert_query, bulk_insert_values)

# Example: Call the procedure to update the email address for user with id 1
procedure_name_to_run = "sp_update_email"
user_name_to_update = "Eve"
new_email = "new_email@example.com"
connector.run_procedure(procedure_name_to_run, (user_name_to_update, new_email))

# Disconnect from the database
connector.disconnect()
