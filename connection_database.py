#!/usr/bin/env python3

import mysql.connector


def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)


cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='banq', use_pure=True)


mycursor = cnx.cursor()
#mycursor.execute("TRUNCATE TABLE livre")

'''

sql = "INSERT INTO livre (title, author, type_document, borrowing_date, due_date, image_name, img) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = ["The Great Gatsby", "Fitzgerald", "Printed Books", "2020-01-01", "2020-01-21", "/image/blah", "image_ofLser"]
mycursor.execute(sql, val)

cnx.commit()

print(mycursor.rowcount, "record inserted.")

'''
#mycursor.execute("SELECT * FROM livre WHERE type_document='Music CDs'")

mycursor.execute("SELECT * FROM livre WHERE id=7")


#myresult = mycursor.fetchall()
#exit()
myresult = mycursor.fetchone()

#exit()

#for x in myresult:
#  print(x)


#https://stackoverflow.com/questions/52759667/properly-getting-blobs-from-mysql-database-with-mysql-connector-in-python/52992413

#sql_fetch_blob_query = """SELECT photo from python_employee where id = %s"""



#sql_fetch_blob_query = """SELECT img from livre where id = %s"""
sql_fetch_blob_query = """SELECT img from livre where id=7"""

print('blah')
mycursor.execute(sql_fetch_blob_query)
print('blah22222')
record = mycursor.fetchone()
write_file(record[0], "blahhhh222.jpg")
#for row in record:
 #   print(row)
    #write_file(row[0], "blahhhh222.jpg")
    #print("Name = ", row[1])
    #image = row[2]
    #file = row[3]
    #print("Storing employee image and bio-data on disk \n")
    #write_file(image, photo)
    #write_file(file, bioData)


cnx.close()