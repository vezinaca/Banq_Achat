#!/usr/bin/env python3

import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='banq', use_pure=True)

my_cursor = cnx.cursor()




ids_of_wanted_books = ['6','9','10']

format_strings = ','.join(['%s'] * len(ids_of_wanted_books))
my_cursor.execute("SELECT title, author FROM thirtythreebooks WHERE id IN (%s)" % format_strings, tuple(ids_of_wanted_books))


record = my_cursor.fetchall()

print(len(record))


for row in record:
	print(row[0])
	print(row[1])