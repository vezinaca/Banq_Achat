#!/usr/bin/env python 3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import datetime
import requests
import sys, os.path

def get_response(url):
	res = requests.get(url)
	res.raise_for_status()
	return res

def create_local_html_file(html_file_name, response):
	
	if not os.path.isfile(html_file_name):
		html_file = open(html_file_name, 'wb')
		for chunk in response.iter_content(100000):
			html_file.write(chunk)

		html_file.close()


mon_dossier_link = "http://banq.qc.ca/mon_dossier/mon_dossier.html"
loans_link = "https://cap.banq.qc.ca/account/loans"
reservations_link = "https://cap.banq.qc.ca/account/reservations"


my_res = get_response(mon_dossier_link)

browser = webdriver.Firefox(executable_path="/home/alienmint/Documents/Programmation/pythonPDF/gecko/geckodriver")

browser.get('http://banq.qc.ca/mon_dossier/mon_dossier.html')
num_client = browser.find_element_by_id('NUM')
num_client.send_keys('00115446')
pwd = browser.find_element_by_id('PWD')
pwd.send_keys('19771314')

connection_button = browser.find_element_by_name('_eventId_proceed')
connection_button.click()

delay = 3 # seconds
try:
    link_consul_dossier = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.LINK_TEXT, 'Consulter mon dossier')))
    print("Consulter mon dossier page is ready")
except TimeoutException:
	print ("Loading took too much time!")


#WebDriverWait(browser, 10).until(lambda browser: EC.presence_of_element_located((By.LINK_TEXT, 'Consulter mon dossier')) != None)
consul_dossier = browser.find_element_by_link_text('Consulter mon dossier')
consul_dossier.click()


#Il faudrait s'assurer que le site demeure en français.  (une fois rendu ici, il switch en anglais)
#Par contre, je ne trouve pas le lien (a href) lorsque j'inspecte en utilisant les dev tools de Google Chrome???

delay = 8 # seconds
try:
    link_borrowing_history = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Borrowing history')]")))
    print("Borrowing history page is ready")
    link_borrowing_history.click()
except TimeoutException:
	print ("Loading Borrowing history page took too much time!")




#infinite scroll


SCROLL_PAUSE_TIME = 1.5

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

fichier_historique = 'historique_emprunt.txt'

try:
	while True:
	    # Scroll down to bottom
	    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	    # Wait to load page
	    time.sleep(SCROLL_PAUSE_TIME)
	    print('scroll scroll scroll')

	    # Calculate new scroll height and compare with last scroll height
	    new_height = browser.execute_script("return document.body.scrollHeight")
	    if new_height == last_height:
	        break
	    last_height = new_height
except KeyboardInterrupt:
	create_local_html_file('mon_historique.html', my_res)
	

