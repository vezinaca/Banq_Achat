#!/usr/bin/env python3

#aller chercher elements dans bd
#verifier sur le site
#updater bd

import mysql.connector
from Utilitaires_BANQ import *
from Book_search_scrape import *

def update_received_db(cnx, mycursor, valeurs):
	
	sql = "UPDATE orders SET received = %s WHERE isbn = %s"
	mycursor.execute(sql, valeurs)
	cnx.commit()
	print(mycursor.rowcount, "record updated.")



def update_last_checked_db(cnx, mycursor, valeurs):
	
	sql = "UPDATE orders SET last_checked = %s WHERE isbn = %s"
	mycursor.execute(sql, valeurs)
	cnx.commit()
	print(mycursor.rowcount, "record updated.")

if __name__ == '__main__':
	#main()
	#browser.quit()
	
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'}

	cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='banq', use_pure=True)
	my_cursor = cnx.cursor()

	creds = ('00115446', '19771314')
	connect_to_site(browser, url, creds)

	sql_select_all = """SELECT * FROM orders WHERE received=0"""
	my_cursor.execute(sql_select_all)
	record = my_cursor.fetchall()

	for row in record:
		
		isbn_du_livre_recherche = row[4]
		book_search_scrape_banq = Book_search_scrape("http://www.banq.qc.ca/techno/recherche/rms.html", 'q', isbn_du_livre_recherche, '#RMS_afficherIris .ValorisationListeDesc a')
		book_search_scrape_banq.set_response(headers)
		print('===============================')
		my_books_banq = book_search_scrape_banq.post_process(book_search_scrape_banq.response.text)

		#book_search_scrape_banq.print_dictionnary()
		#creds = getCredentials()
		

		#browser.get(formulaire_link)

		if (len(my_books_banq) == 0):
			print('The book ' + row[1] + ' by ' + row[2] + ' was NOT found in the BANQ catalogue.')
			#print('The book ' + book_search_scrape_isbn.list_of_dic_books[0].get('Titre') + ' by ' + book_search_scrape_isbn.list_of_dic_books[0].get('Auteur') + ' will be ordered.')
		else:
			print('The book ' + isbn_du_livre_recherche + ' by '  + ' was FOUND in the BANQ catalogue.')
			url_recherche_selenium = 'https://www.banq.qc.ca/techno/recherche/rms.html?q=' + isbn_du_livre_recherche
			browser.get(url_recherche_selenium)
			time.sleep(3)
			book_link = browser.find_element_by_xpath("//div[starts-with(@class,'ValorisationListeDesc')]/a")
			book_link.click()

			time.sleep(3)
			book_status = browser.find_element_by_xpath("//div[starts-with(@class,'_290')]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]")
			print("this book status: " + book_status.text)
			if ('loan' in book_status.text):
				print("oui c emprunte")
				reserver_button = browser.find_element_by_xpath("//div[starts-with(@class,'_290')]/div[1]/div[1]/div[1]/div[1]/button[1]")
				print("texte du boutton: " + reserver_button.text)
				reserver_button.click()
				time.sleep(8)
				confirm_popup_button = browser.find_element_by_xpath("//body/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]")
				confirm_popup_button.click()
				time.sleep(4)
				close_popup_button = browser.find_element_by_xpath("//body/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]")
				print("texte du close_popup_boutton: " + close_popup_button.text)
				close_popup_button.click()
			#table name, field, value of field, isbn
			#sql = "UPDATE orders SET last_checked = %s WHERE isbn = %s"
			#sql = "UPDATE %s SET %s = %s WHERE isbn = %s"
			val =[True, isbn_du_livre_recherche]
			#update_received_db(cnx, my_cursor, val)

		val = [datetime.now(), isbn_du_livre_recherche]
		update_last_checked_db(cnx, my_cursor, val)		

	cnx.close()