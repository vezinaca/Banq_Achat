#!/usr/bin/env python 3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from datetime import datetime
import time

import mysql.connector

url = 'http://banq.qc.ca/mon_dossier/mon_dossier.html'
browser = webdriver.Firefox(executable_path="/home/alienmint/Documents/Programmation/pythonPDF/gecko/geckodriver")

def connect_to_site(browser, url):
	browser.get(url)
	num_client = browser.find_element_by_id('NUM')
	num_client.send_keys('00115446')
	pwd = browser.find_element_by_id('PWD')
	pwd.send_keys('19771314')
	connection_button = browser.find_element_by_name('_eventId_proceed')
	connection_button.click()

def infinite_scroll():
	#infinite scroll
	# https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python

	SCROLL_PAUSE_TIME = 2

	# Get scroll height
	last_height = browser.execute_script("return document.body.scrollHeight")

	p = 1
	try:
		#while True:
		for i in range(5):
		    # Scroll down to bottom
		    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

		    # Wait to load page
		    time.sleep(SCROLL_PAUSE_TIME)
		    print(str(p) + ") " +'scrolling...')
		    p = p + 1

		    # Calculate new scroll height and compare with last scroll height
		    new_height = browser.execute_script("return document.body.scrollHeight")
		    if new_height == last_height:
		        break
		    last_height = new_height
	except KeyboardInterrupt:
		print('allo')


def is_html_element_present_click(browser, link_text, by_search):
	delay = 3 # seconds
	try:
	    link_verify = WebDriverWait(browser, delay).until(EC.presence_of_element_located((by_search, link_text)))
	    print(link_text + " page is ready")
	    link_verify.click()
	except TimeoutException:
		print ("Loading of " + link_text + "took too much time!")

def printList(my_list):
	i = 1
	for item in my_list:
		#print("=====")
		#print(type(item))
		print(str(i) + ") " +item.text + '\n')
		i = i +1
		#print("=====")

def delete_all_table_rows(table):
	pass

def insert_into_db(cnx, cursor, valeurs):
	
	sql = "INSERT INTO livre (title, author, type_document, borrowing_date, due_date) VALUES (%s, %s, %s, %s, %s)"
	mycursor.execute(sql, val)
	cnx.commit()
	print(mycursor.rowcount, "record inserted.")

if __name__ == "__main__":

	cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='banq')
	mycursor = cnx.cursor()
	#mycursor.execute("TRUNCATE TABLE livre")

	connect_to_site(browser, url)
	is_html_element_present_click(browser, 'Consulter mon dossier' , By.LINK_TEXT)
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
		
		insert_into_db(cnx, mycursor, val)	
		print(title.text)
		print(type_document_name.text)
		print(borrowing_date.text)
		print(due_date.text)

		#label = card.find_elements_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[@class='metaFields_1su17lh']/div[1]/div[@class='meta-label metaLabel_13uwct0']")
		#value = card.find_elements_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[@class='metaFields_1su17lh']/div[1]/div[@class='meta-values metaValue_tcono5']/span[1]")
		
	cnx.close()	
		