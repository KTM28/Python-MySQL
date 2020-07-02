import os
import pymysql
from os import path

# Get username and password from env.py
if os.path.exists("env.py"):
    import env

username = os.environ.get("username")
password = os.environ.get("password")
# Connect to the database
connection = pymysql.connect(
    host="localhost", user=username, password=password, db="Chinook"
)


try:
    # Run a Query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Genre;"
        cursor.execute(sql)  # execute that SQL command there and get result back
        for row in cursor:
            print(row)

finally:
    # Close the connection, regardless of wheteher the above was successful
    connection.close()
