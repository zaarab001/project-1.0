import mysql.connector
from mysql.connector import Error

def connect():
	try:
		conn = msql.connector.connect
		(host='localhost', database='one_tech', user='root', password = '')
		if conn.is_connected():
			print('database connected')
		except Error as e:
			print(e)

		finally:
			conn.close()

	if __name__== '__main__':
		connect()
