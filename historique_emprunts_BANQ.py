#!/usr/bin/env python 3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

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

if __name__ == "__main__":
	connect_to_site(browser, url)
	is_html_element_present_click(browser, 'Consulter mon dossier' , By.LINK_TEXT)
	time.sleep(8)
	is_html_element_present_click(browser, "//*[contains(text(), 'Borrowing history') or contains(text(), 'Historique des emprunts')]", By.XPATH)
	#is_html_element_present_click(browser, "//*[contains(text(), 'Borrowed and renewed items')]", By.XPATH)
	
	#infinite_scroll()
	time.sleep(4)
	#//input[starts-with(@id, 'activation:') and contains(@id, ':voId:1')]
	#all_cards = browser.find_elements_by_xpath("//div[starts-with(@class, 'cardContent_')]") 
	#<div class="cardStacked_n7d4vb"><div class="cardContent_p5m42o">
	#all_cards = browser.find_elements_by_xpath("//div[@class='cardContent_p5m42o']") 
	all_book_titles = browser.find_elements_by_xpath("//div[@class='cardContent_p5m42o']/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/span[1]") 

	#all_cards_main = browser.find_elements_by_xpath("//div[@class='cardStacked_n7d4vb']")
	#<div class="card_dzxwpk"><div class="cardMediaNoActions_xe8xza-o_O-color_1bra37d" title="Experiencing Nirvana : grunge in Europe, 1989">
	#all_cards_stacked = browser.find_elements_by_xpath("//div[starts-with(@class,'cardStacked_')]")
	all_cards_stacked = browser.find_elements_by_xpath("//div[starts-with(@class,'card_dzxwpk')]")

	print("size of all cards main: " + str(len(all_cards_stacked)))
	print ("size of all book titles: " + str(len(all_book_titles)))

	#printList(all_book_titles)
	printList(all_cards_stacked)
	for card in all_cards_stacked:
		#the_cards = card.find_elements_by_xpath("//div[starts-with(@class,'cardContent_p5m42o')]")
		#<div class="cardMediaNoActions_xe8xza-o_O-color_1bra37d" title="Amsterdam - 2017">
		#username = driver.find_element_by_xpath("//input[@name='username']")
		#book_title = card.find_element_by_xpath("/div[2]/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/span[1]")
		#the_cards = card.find_elements_by_xpath("div[@class='cardMediaNoActions_xe8xza-o_O-color_1bra37d']")
		
		titles = card.find_elements_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/span[1]")
		#label = card.find_elements_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[@class='metaFields_1su17lh']/div[1]/div[@class='meta-label metaLabel_13uwct0']")
		meta_fields = card.find_elements_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[@class='metaFields_1su17lh']/div")
		if(len(meta_fields)>1):
			author = meta_fields.find_elements_by_xpath("div[1]/div[@class='meta-values metaValue_tcono5']")
			type_document = meta_fields.find_elements_by_xpath("div[2]/div[@class='meta-values metaValue_tcono5']")
			print('author: ' + author)
		else:
			type_document = meta_fields.find_elements_by_xpath("div[1]/div[@class='meta-values metaValue_tcono5']")

		print('type_document' + type_document)



		label = card.find_elements_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[@class='metaFields_1su17lh']/div[1]/div[@class='meta-label metaLabel_13uwct0']")
		value = card.find_elements_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[@class='metaFields_1su17lh']/div[1]/div[@class='meta-values metaValue_tcono5']/span[1]")
		
		#<div class="meta-label metaLabel_13uwct0"><!-- react-text: 957 -->Author<!-- /react-text -->
		#<div class="meta-values metaValue_tcono5"><span>Pavitt, Bruce, 1959- auteur</span></div>
		#<div class='metaFields_1su17lh'><div><div class="meta-label metaLabel_13uwct0"><!-- react-text: 957 -->Author<!-- 
		
		#print(str(len(titles)))
		#print(str(len(label)))
		#print(str(len(value)))
		print(str(len(meta_fields)))

		printList(titles)
		#printList(label)
		#printList(value)
	

'''

all_book_titles = browser.find_elements_by_xpath("//div[@class='cardContent_p5m42o']/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/span[1]") 
#all_book_authors = browser.find_elements_by_xpath("//div[@class='meta-values metaValue_tcono5']/span[1]") 

all_book_authors = browser.find_elements_by_xpath("//div[@class='metaFields_1su17lh']/div[1]/div[@class='meta-values metaValue_tcono5']/span[1]")
#all_book_types = browser.find_elements_by_xpath("//div[@class='metaFields_1su17lh']/div[2]/div[@class='meta-values metaValue_tcono5']/span[1]") 

all_borrowing_dates = browser.find_elements_by_xpath("//div[@class='listContent_1nnce6d']/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[1]/div[1]")
all_due_dates = browser.find_elements_by_xpath("//div[@class='listContent_1nnce6d']/div[@class='cardContent_p5m42o']/div[1]/div[2]/div[1]/div[1]")

#<div class="listContent_1nnce6d" style="padding: 8px 0px;"><div class="cardContent_p5m42o">

#both in metaFields_1su17lh
#<div class="meta-label metaLabel_13uwct0"> type of document / author
#<div class="meta-values metaValue_tcono5"><span>Printed Books</span></div> this can be name of author or printed books


print ("size of all book titles: " + str(len(all_book_titles)))
print ("size of all book authors: " + str(len(all_book_authors)))
print ("size of all borrowing dates: " + str(len(all_borrowing_dates)))
print ("size of all due dates: " + str(len(all_due_dates)))
#print ("size of all book types: " + str(len(all_book_types)))
fichier_historique = 'historique_emprunt.txt'

open(fichier_historique, 'w').close()



printList(all_book_titles)
print ("=======================================")
printList(all_book_authors)
print ("=======================================")
printList(all_borrowing_dates)
print ("=======================================")
printList(all_due_dates)

#printList(all_book_types)
'''

'''
file_to_write = open(fichier_historique, "a")
i = 1
for book in all_book_titles:
	file_to_write.write(str(i) + ") " + book.text + '\n')
	i = i + 1

file_to_write.close()

'''