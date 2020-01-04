#!/usr/bin/env python3

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

if __name__ == "__main__":
	connect_to_site(browser, url)
	is_html_element_present_click(browser, 'Consulter mon dossier' , By.LINK_TEXT)
	time.sleep(8)
	is_html_element_present_click(browser, "//*[contains(text(), 'Borrowing history') or contains(text(), 'Historique des emprunts')]", By.XPATH)
	#infinite_scroll()
	time.sleep(4)
	#//input[starts-with(@id, 'activation:') and contains(@id, ':voId:1')]
	#all_cards = browser.find_elements_by_xpath("//div[starts-with(@class, 'cardContent_')]") 
	#<div class="cardStacked_n7d4vb"><div class="cardContent_p5m42o">
	all_cards_main = browser.find_elements_by_xpath("//div[@class='cardStacked_n7d4vb']")
	all_cards = browser.find_elements_by_xpath("//div[@class='cardContent_p5m42o']") 
	all_book_titles = browser.find_elements_by_xpath("//div[@class='cardContent_p5m42o']/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/span[1]") 

	print("size of all cards: " + str(len(all_cards)))
	print("size of all cards main: " + str(len(all_cards_main)))

	print("size of all book titles: " + str(len(all_book_titles)))

