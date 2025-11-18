import mysql.connector
import pymysql

def create_connection():
    connection = pymysql.connect(
        host='cloud-labs-db.mysql.database.azure.com',
        user='daniel',
        password='Danylo.2006',
        database='lab1',
	port=3306,
	ssl_ca="{/home/Daniel/DigiCertGlobalRootG2.crt.pem}",
	ssl_disabled=False
    )
    return connection
