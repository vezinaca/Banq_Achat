#!/usr/bin/env python 3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

browser = webdriver.Firefox(executable_path="/home/alienmint/Documents/Programmation/pythonPDF/gecko/geckodriver")
# type (browser)


#browser.get('http://banq.qc.ca')
browser.get('http://banq.qc.ca/mon_dossier/mon_dossier.html')
#linkElem = browser.find_element_by_class_name('userOff')
#type(linkElem)
#linkElem.click()

num_client = browser.find_element_by_id('NUM')
print (num_client.location)
num_client.send_keys('00115446')
pwd = browser.find_element_by_id('PWD')
print (pwd.location)
pwd.send_keys('19771314')
#pwd.submit()

connection_button = browser.find_element_by_name('_eventId_proceed')
print(connection_button.location)
connection_button.click()


delay = 3 # seconds
try:
    link_consul_dossier = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.LINK_TEXT, 'Consulter mon dossier')))
    print("page is ready")
except TimeoutException:
	print ("Loading took too much time!")


#WebDriverWait(browser, 10).until(lambda browser: EC.presence_of_element_located((By.LINK_TEXT, 'Consulter mon dossier')) != None)

consul_dossier = browser.find_element_by_link_text('Consulter mon dossier')
consul_dossier.click()


#<input type="submit" name="_eventId_proceed" value="Connexion">