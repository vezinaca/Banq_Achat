#!/usr/bin/env python3

import mysql.connector

from PIL import Image
import glob
import os, shutil


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
#mycursor.execute("SELECT * FROM commande WHERE id=7")

#mycursor.execute("SELECT * FROM livre WHERE id=7")


#myresult = mycursor.fetchall()
#exit()
#myresult = mycursor.fetchone()

#exit()

#for x in myresult:
#    print(x)
#exit()

#https://stackoverflow.com/questions/52759667/properly-getting-blobs-from-mysql-database-with-mysql-connector-in-python/52992413
#sql_fetch_blob_query = """SELECT photo from python_employee where id = %s"""



#sql_fetch_blob_query = """SELECT img from livre where id = %s"""
sql_fetch_blob_query = """SELECT img from commande where id=7"""


print('blah')
mycursor.execute(sql_fetch_blob_query)
print('blah22222')
record = mycursor.fetchone()
write_file(record[0], "blahhhh222.jpg")
exit()

#for row in record:
 #   print(row)
    #write_file(row[0], "blahhhh222.jpg")
    #print("Name = ", row[1])
    #image = row[2]
    #file = row[3]
    #print("Storing employee image and bio-data on disk \n")
    #write_file(image, photo)
    #write_file(file, bioData)

'''
image_list = []
for filename in glob.glob('yourpath/*.gif'): #assuming gif
    im=Image.open(filename)
    image_list.append(im)
'''

sql_fetch_image = """Select image_name from livre where id=5"""
mycursor.execute(sql_fetch_image)
record = mycursor.fetchone()


image_file = Image.open(record[0]) 

width, height = image_file.size

my_size = image_file.size

print(my_size)

print ("shit")

sql_select_all = """SELECT * FROM livre WHERE id=2"""
mycursor.execute(sql_select_all)
record = mycursor.fetchone()

print (record[2])

def hasSpecialCharacter(name_of_file):
	chose = name_of_file.replace('/', '-')
	chose = name_of_file.replace('\\','-')
	print (chose)
	return chose
	'''if '/' in name_of_file:
		print("yes")
		name_of_file.replace('o', '-')
		print("in method: " + name_file)
	'''
'''
name_file = "project/object"

hasSlashCharacter(name_file)

print(name_file)

print(name_file.replace('p', '4'))

print("shadow\\fuck".replace('\\', "-"))
'''
def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces :
        # Check if string is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)
    
    return  mainString  

#print('after: ' + hasSpecialCharacter("/cross\\bakc/"))

mainStr = "Hello/ Th\\is is /a sample string"
 

#Replace multiple characters / strings from a string

# Replace all the occurrences of string in list by AA in the main list 
otherStr = replaceMultiple(mainStr, ['\\', '/'] , "-")

print(otherStr)



'''
folder = '/path/to/folder'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

'''


cnx.close()