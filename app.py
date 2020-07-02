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
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)  # execute that SQL command there and get result back
        result = cursor.fetchall()  # Getting the data back
        print(result)

finally:
    # Close the connection, regardless of wheteher the above was successful
    connection.close()
