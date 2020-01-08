#!/usr/bin/env python 3

from Utilitaires_BANQ import *

import mysql.connector


def delete_all_table_rows(cursor, table):
	cursor.execute("TRUNCATE TABLE " + table)

def insert_into_db(cnx, cursor, valeurs):
	
	sql = "INSERT INTO livre (title, author, type_document, borrowing_date, due_date) VALUES (%s, %s, %s, %s, %s)"
	mycursor.execute(sql, val)
	cnx.commit()
	print(mycursor.rowcount, "record inserted.")

if __name__ == "__main__":

	cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='banq')
	my_cursor = cnx.cursor()
	#delete_all_table_rows(my_cursor, table)

	connect_to_site(browser, url)
	#is_html_element_present_click(browser, 'Consulter mon dossier' , By.LINK_TEXT)
	is_html_element_present_click(browser, "subscriber's account" , By.LINK_TEXT)
	time.sleep(4)
	is_html_element_present_click(browser, "//*[contains(text(), 'Borrowing history') or contains(text(), 'Historique des emprunts')]", By.XPATH)

	#infinite_scroll()
	time.sleep(4)
	#//input[starts-with(@id, 'activation:') and contains(@id, ':voId:1')]
	all_book_titles = browser.find_elements_by_xpath("//div[@class='cardContent_p5m42o']/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/span[1]") 
	all_cards_stacked = browser.find_elements_by_xpath("//div[starts-with(@class,'card_dzxwpk')]")

	print("size of all cards main: " + str(len(all_cards_stacked)))
	print ("size of all book titles: " + str(len(all_book_titles)))
	
	for card in all_cards_stacked:
		
		title = card.find_element_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/span[1]")
		#label = card.find_elements_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[@class='metaFields_1su17lh']/div[1]/div[@class='meta-label metaLabel_13uwct0']")
		meta_fields = card.find_elements_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[@class='metaFields_1su17lh']/div")
		
		borrowing_date = card.find_element_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[2]/div[@class='listContent_1nnce6d']/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[1]/div[1]")
		due_date = card.find_element_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[2]/div[@class='listContent_1nnce6d']/div[@class='cardContent_p5m42o']/div[1]/div[2]/div[1]/div[1]")
		
		borrowing_date_object = datetime.strptime(borrowing_date.text, '%m/%d/%Y')
		#borrowing_date_object = datetime.strptime(borrowing_date.text, '%d/%m/%Y')
		due_date_object = datetime.strptime(due_date.text, '%m/%d/%Y')
		#due_date_object = datetime.strptime(due_date.text, '%d/%m/%Y')
		
		formatted_borrowing_date = borrowing_date_object.strftime('%Y-%m-%d %H:%M:%S')
		formatted_due_date = due_date_object.strftime('%Y-%m-%d %H:%M:%S')


		#author exists
		if(len(meta_fields)>1):
			author = meta_fields[0]
			author_name = author.find_element_by_xpath("div[@class='meta-values metaValue_tcono5']/span[1]")
			type_document = meta_fields[1]
			type_document_name = type_document.find_element_by_xpath("div[@class='meta-values metaValue_tcono5']/span[1]")
			print(author_name.text)
			val = [str(title.text), str(author_name.text) , str(type_document_name.text), formatted_borrowing_date, formatted_due_date]
			
		#author doesn't exist
		else:
			type_document = meta_fields[0]
			type_document_name = type_document.find_element_by_xpath("div[@class='meta-values metaValue_tcono5']/span[1]")
			val = [str(title.text), "" , str(type_document_name.text), formatted_borrowing_date, formatted_due_date]
		
		#insert_into_db(cnx, my_cursor, val)	
		print(title.text)
		print(type_document_name.text)
		print(borrowing_date.text)
		print(due_date.text)

		#label = card.find_elements_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[@class='metaFields_1su17lh']/div[1]/div[@class='meta-label metaLabel_13uwct0']")
		#value = card.find_elements_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[@class='metaFields_1su17lh']/div[1]/div[@class='meta-values metaValue_tcono5']/span[1]")
		
	cnx.close()	
		