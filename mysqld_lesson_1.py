#!/usr/bin/python3
""" A tutorial guide for MySQLdb.
    I am going to use command line argument
    to provide arguments to the script, hence
    the need for the sys module
"""
import MySQLdb
import sys

# ensures my script is not executed if imported
if __name__ == "__main__":
    user_name = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
# creates a connection object using context mangager
    with MySQLdb.connect(
            host="localhost", user=user_name,
            passwd=password, db=database
            ) as connection:
        cursor = connection.cursor()
        cursor.execute(
                "CREATE TABLE customer (id INT PRIMARY KEY, name VARCHAR(60))"
                )
        cursor.execute("INSERT INTO customer (id, name) VALUES (1, 'Daniel')")
        cursor.execute("SELECT * FROM customer")
        result = cursor.fetchall()
        for row in result:
            print(row[0], row[1])
