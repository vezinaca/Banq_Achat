#!/usr/bin/env python3

#aller chercher elements dans bd
#verifier sur le site
#updater bd

import mysql.connector
import smtplib
from Utilitaires_BANQ import *
from Book_search_scrape import *
from datetime import date

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

def send_email(email_string):

	smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login('racontemoidoncca@gmail.com', 'ZaqWsxcd')
	smtpObj.sendmail('racontemoidoncca@gmail.com', 'vezinaca@gmail.com',
	email_string)
	smtpObj.quit()
	print("email sent")
	
if __name__ == '__main__':
	#main()
	#browser.quit()

	browser = webdriver.Firefox(executable_path="/home/alienmint/Documents/Programmation/pythonPDF/Banq_Achat/gecko/geckodriver")

	email_string = 'Subject: New book availibility verification for ' + str(date.today()) + '\n'
	email_string = email_string + "\nGreetings bookworm, \n\nHere are the verifications:"
	
	
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'}

	cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='banq', use_pure=True)
	my_cursor = cnx.cursor()

	creds = ('00115446', '19771314')
	connect_to_site(browser, url, creds)
	
	kill_coronavirus_alert_message(browser)


	sql_select_all = """SELECT * FROM orders WHERE accepted=1"""
	my_cursor.execute(sql_select_all)
	record = my_cursor.fetchall()

	for row in record:
		
		titre = row[1]
		auteur = row[2]
		isbn_du_livre_recherche = row[4]
		book_search_scrape_banq = Book_search_scrape("http://www.banq.qc.ca/techno/recherche/rms.html", 'q', isbn_du_livre_recherche, '#RMS_afficherIris .ValorisationListeDesc a')
		book_search_scrape_banq.set_response(headers)
		print('===============================')
		my_books_banq = book_search_scrape_banq.post_process(book_search_scrape_banq.response.text)


		if (len(my_books_banq) == 0):
			print('The book ' + titre + ' (' + isbn_du_livre_recherche + ') by ' + auteur + ' was NOT found in the BANQ catalogue.')
			email_string = email_string + '\n\nThe book ' + titre + ' (' +  isbn_du_livre_recherche + ') by ' + auteur + ' was NOT found in the BANQ catalogue.'
			
		else:
			print('The book ' + titre + ' by ' + auteur + ' was FOUND in the BANQ catalogue.')
			email_string = email_string + '\n\nThe book ' + titre + ' (' + isbn_du_livre_recherche + ') by ' + auteur + ' was FOUND in the BANQ catalogue.'
			url_recherche_selenium = 'https://www.banq.qc.ca/techno/recherche/rms.html?q=' + isbn_du_livre_recherche
			browser.get(url_recherche_selenium)
			time.sleep(3)
			book_link = browser.find_element_by_xpath("//div[starts-with(@class,'ValorisationListeDesc')]/a")
			book_link.click()

			time.sleep(5)
			
			book_status = browser.find_element_by_xpath("//div[starts-with(@class,'_290')]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]")
			print("Book status: " + book_status.text)
			
			if ('Available' in book_status.text):
				
				email_string = email_string + "\n\t\t This book is currently available"
				print('The book ' + titre + ' (' + isbn_du_livre_recherche +  ") by " + auteur + ' is available in the BANQ catalogue.')

			# need to verify what is written on website when books says: 'en commande', reserve it anyways
			#if ('loan' in book_status.text):
			else:
				email_string = email_string + "\n\t\t This book is " + book_status.text + " but will be RESERVED."
				reserver_button = browser.find_element_by_xpath("//div[starts-with(@class,'_290')]/div[1]/div[1]/div[1]/div[1]/button[1]")
				#print("texte du boutton: " + reserver_button.text)
				reserver_button.click()
				time.sleep(7)
				confirm_popup_button = browser.find_element_by_xpath("//body/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]")
				confirm_popup_button.click()
				time.sleep(6)
				close_popup_button = browser.find_element_by_xpath("//body/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]")
				#print("texte du close_popup_boutton: " + close_popup_button.text)
				close_popup_button.click()

			#table name, field, value of field, isbn
			#sql = "UPDATE orders SET last_checked = %s WHERE isbn = %s"
			#sql = "UPDATE %s SET %s = %s WHERE isbn = %s"
			val =[True, isbn_du_livre_recherche]
			#update_received_db(cnx, my_cursor, val)

		val = [datetime.now(), isbn_du_livre_recherche]
		update_last_checked_db(cnx, my_cursor, val)	
	
	new_email_string = email_string.replace(u'\u2013','')
	send_email(new_email_string)
	cnx.close()
	browser.quit()