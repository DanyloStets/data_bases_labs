import mysql.connector
import pymysql

def create_connection():
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='root',
        database='local_flixbus'
    )
    return connection
