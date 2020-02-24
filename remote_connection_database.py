#!/usr/bin/env python3

import mysql.connector

from PIL import Image
import glob

'''
const URL = "localhost/fivemin_comix";
		const DB_HOST = "localhost";
		const DB_USER = "fivemin_comix";
		const DB_PWD = "Crisse123";
		const DB_NAME = "fivemin_comix";


self::$instance = new PDO(
				"mysql:host=".Config::DB_HOST.";dbname=".Config::DB_NAME."", 
				Config::DB_USER, 
				Config::DB_PWD);
                
}
'''

#host='67.205.105.240
User: fivemin_banq_me
Database: fivemin_fivemin_banq
pass: Otc[PvZ==,e[

cnx = mysql.connector.connect(user='fivemin_comix', password='Crisse123',
                              host='fiveminutesago.ca',
                              database='fivemin_comix',
                              port='3306')


mycursor = cnx.cursor()

sql_select_one = """SELECT * FROM livres WHERE numero=2"""
mycursor.execute(sql_select_one)
record = mycursor.fetchone()

print ('allo')
print (record[2])