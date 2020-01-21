#!/usr/bin/env python 3

from Utilitaires_BANQ import *

import mysql.connector
import urllib.request


def delete_all_table_rows(cursor, table):
	cursor.execute("TRUNCATE TABLE " + table)

# For inserting file as blob in database
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

#not used
def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)

def insert_into_db(cnx, mycursor, valeurs):
	sql = "INSERT INTO livre (title, author, type_document, borrowing_date, due_date, image_name, img) VALUES (%s, %s, %s, %s, %s, %s, %s)"
	mycursor.execute(sql, valeurs)
	cnx.commit()
	print(mycursor.rowcount, "record inserted.")
	
#Used to replace '/' and '\' that might appear in filename
def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces :
        # Check if string is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)
    
    return  mainString  

if __name__ == "__main__":

	cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='banq')
	my_cursor = cnx.cursor()
	delete_all_table_rows(my_cursor, "livre")

	creds = getCredentials()
	connect_to_site(browser, url, creds)

	#is_html_element_present_click(browser, 'Consulter mon dossier' , By.LINK_TEXT)
	is_html_element_present_click(browser, "subscriber's account" , By.LINK_TEXT)
	time.sleep(4)
	is_html_element_present_click(browser, "//*[contains(text(), 'Borrowing history') or contains(text(), 'Historique des emprunts')]", By.XPATH)

	infinite_scroll()
	time.sleep(4)
	#//input[starts-with(@id, 'activation:') and contains(@id, ':voId:1')]
	#//div[starts-with(@class,'card_dzxwpk'
	#all_book_titles = browser.find_elements_by_xpath("//div[@class='cardContent_p5m42o']/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/span[1]") 
	all_book_titles = browser.find_elements_by_xpath("//div[starts-with(@class,'cardContent_')]/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/span[1]") 
	all_cards_stacked = browser.find_elements_by_xpath("//div[starts-with(@class,'card_dzxwpk')]")


	print("size of all cards main: " + str(len(all_cards_stacked)))
	print ("size of all book titles: " + str(len(all_book_titles)))
	
	for card in all_cards_stacked:
		
		#title = card.find_element_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/span[1]")
		title = card.find_element_by_xpath("div[starts-with(@class,'cardStacked_')]/div[starts-with(@class,'cardContent_')]/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/span[1]")
		
		#label = card.find_elements_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[@class='metaFields_1su17lh']/div[1]/div[@class='meta-label metaLabel_13uwct0']")
		
		#meta_fields = card.find_elements_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[@class='metaFields_1su17lh']/div")
		meta_fields = card.find_elements_by_xpath("div[starts-with(@class,'cardStacked_')]/div[starts-with(@class,'cardContent_')]/div[1]/div[1]/div[starts-with(@class,'metaFields_')]/div")
		
		#borrowing_date = card.find_element_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[2]/div[@class='listContent_1nnce6d']/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[1]/div[1]")
		borrowing_date = card.find_element_by_xpath("div[starts-with(@class,'cardStacked_')]/div[starts-with(@class,'cardContent_')]/div[2]/div[starts-with(@class,'listContent_')]/div[starts-with(@class,'cardContent_')]/div[1]/div[1]/div[1]/div[1]")		
		
		#due_date = card.find_element_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[2]/div[@class='listContent_1nnce6d']/div[@class='cardContent_p5m42o']/div[1]/div[2]/div[1]/div[1]")
		due_date = card.find_element_by_xpath("div[starts-with(@class,'cardStacked_')]/div[starts-with(@class,'cardContent_')]/div[2]/div[starts-with(@class,'listContent_')]/div[starts-with(@class,'cardContent_')]/div[1]/div[2]/div[1]/div[1]")		
		#en
		borrowing_date_object = datetime.strptime(borrowing_date.text, '%m/%d/%Y')
		#fr
		#borrowing_date_object = datetime.strptime(borrowing_date.text, '%d/%m/%Y')
		#en
		due_date_object = datetime.strptime(due_date.text, '%m/%d/%Y')
		#fr
		#due_date_object = datetime.strptime(due_date.text, '%d/%m/%Y')
		
		formatted_borrowing_date = borrowing_date_object.strftime('%Y-%m-%d %H:%M:%S')
		formatted_due_date = due_date_object.strftime('%Y-%m-%d %H:%M:%S')

		img_div = card.find_element_by_xpath("div[starts-with(@class,'cardMediaNoActions_')]/div[1]")
		img_attribute = img_div.get_attribute("style")
		
		partial_link_text = parse_style_attribute(img_attribute)
		my_path = 'images/'
		#fullfilename = os.path.join(my_path, title.text.replace('/','-') + ".jpg")
		fullfilename = os.path.join(my_path, replaceMultiple(title.text, ['\\', '/', ' ', ','] , "_") + ".jpg")
		
		try:
			urllib.request.urlretrieve("https://cap.banq.qc.ca/" + partial_link_text, fullfilename)
		except FileNotFoundError:
			"can't find file"
		photoBinaryData = convertToBinaryData(fullfilename)

		#author exists
		if(len(meta_fields)>1):
			author = meta_fields[0]
			author_name = author.find_element_by_xpath("div[@class='meta-values metaValue_tcono5']/span[1]")
			type_document = meta_fields[1]
			type_document_name = type_document.find_element_by_xpath("div[@class='meta-values metaValue_tcono5']/span[1]")
			print(author_name.text)
			val = [str(title.text), str(author_name.text) , str(type_document_name.text), formatted_borrowing_date, formatted_due_date, str(fullfilename), photoBinaryData]
			
		#author doesn't exist
		else:
			type_document = meta_fields[0]
			type_document_name = type_document.find_element_by_xpath("div[@class='meta-values metaValue_tcono5']/span[1]")
			val = [str(title.text), "" , str(type_document_name.text), formatted_borrowing_date, formatted_due_date, str(fullfilename), photoBinaryData]
			
		insert_into_db(cnx, my_cursor, val)	
		print(title.text)
		print(type_document_name.text)
		print(borrowing_date.text)
		print(due_date.text)
		print(str(fullfilename))
		
		
	cnx.close()	
		