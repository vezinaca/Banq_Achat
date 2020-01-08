#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from datetime import datetime
import time

url = 'http://banq.qc.ca/mon_dossier/mon_dossier.html?language_id=1'
browser = webdriver.Firefox(executable_path="/home/alienmint/Documents/Programmation/pythonPDF/gecko/geckodriver")

def connect_to_site(browser, url):
	browser.get(url)
	num_client = browser.find_element_by_id('NUM')
	num_client.send_keys('00115446')
	pwd = browser.find_element_by_id('PWD')
	pwd.send_keys('19771314')
	connection_button = browser.find_element_by_name('_eventId_proceed')
	connection_button.click()

def is_html_element_present_click(browser, link_text, by_search):
	delay = 3 # seconds
	try:
	    link_verify = WebDriverWait(browser, delay).until(EC.presence_of_element_located((by_search, link_text)))
	    print(link_text + " page is ready")
	    link_verify.click()
	except TimeoutException:
		print ("Loading of " + link_text + "took too much time!")

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

def printList(my_list):
	i = 1
	for item in my_list:
		#print("=====")
		#print(type(item))
		print(str(i) + ") " +item.text + '\n')
		i = i +1
		#print("=====")