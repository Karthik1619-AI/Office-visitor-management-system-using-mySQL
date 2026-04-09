import mysql.connector

def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",  # change this
        database="office_visitor_db"
    )
    return connection
