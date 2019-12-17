#!/usr/bin/env python 3

from selenium import webdriver

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



consul_dossier = browser.find_element_by_link_text('Consulter mon dossier')
consul_dossier.click()


#<input type="submit" name="_eventId_proceed" value="Connexion">