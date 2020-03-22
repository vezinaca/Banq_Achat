#!/usr/bin/env python3

import mysql.connector
from datetime import datetime

'''
ids_of_wanted_books = ['6','9','10']
format_strings = ','.join(['%s'] * len(ids_of_wanted_books))
my_cursor.execute("SELECT title, author FROM thirtythreebooks WHERE id IN (%s)" % format_strings, tuple(ids_of_wanted_books))
record = my_cursor.fetchall()

print(len(record))

#datetime.now()
for row in record:
	print(row[0])
	print(row[1])
'''

def update_db(cnx, mycursor, valeurs):
	
	sql = "UPDATE %s SET %s = %s WHERE isbn = %s"
	mycursor.execute(sql, valeurs)
	cnx.commit()
	print(mycursor.rowcount, "record updated.")

def update_db_not(cnx, mycursor, valeurs):
	
	sql = "UPDATE orders SET last_checked = %s WHERE isbn = %s"
	mycursor.execute(sql, valeurs)
	cnx.commit()
	print(mycursor.rowcount, "record updated.")

if __name__ == '__main__':
	#main()
	cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='banq', use_pure=True)

	my_cursor = cnx.cursor()

	isbn_du_livre_recherche = '9781628929270'

	val =['orders', 'last_checked', datetime.now(), isbn_du_livre_recherche]
	update_db(cnx, my_cursor, val)
