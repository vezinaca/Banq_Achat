#!/usr/bin/env python 3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

mon_dossier_link = "http://banq.qc.ca/mon_dossier/mon_dossier.html"
loans_link = "https://cap.banq.qc.ca/account/loans"
reservations_link = "https://cap.banq.qc.ca/account/reservations"

browser = webdriver.Firefox(executable_path="/home/alienmint/Documents/Programmation/pythonPDF/gecko/geckodriver")
# type (browser)


#browser.get('http://banq.qc.ca')
browser.get('http://banq.qc.ca/mon_dossier/mon_dossier.html')
#linkElem = browser.find_element_by_class_name('userOff')
#type(linkElem)
#linkElem.click()

#<a href="/accueil/index.html?language_id=1" xml:lang="en" lang="en">English</a>
#<a href="/accueil/index.html?language_id=3" lang="fr" xml:lang="fr">Français</a>



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

#time.sleep(5)
#browser.navigate().to(loans_link)
#browser.GoTo(loans_link)


#Il faudrait s'assurer que le site demeure en français.  (une fois rendu ici, il switch en anglais)
#Par contre, je ne trouve pas le lien (a href) lorsque j'inspecte en utilisant les dev tools de Google Chrome???

'''
Ensuite, j'aimerais aller dans la section des emprunts mais encore une fois, je ne trouve pas de lien avec les dev tools?
Ce n'est qu'une fois avoir cliqué sur le 'lien' que je trouve le href dans la barre d'adresse ("https://cap.banq.qc.ca/account/loans")
Cependant, je vois ceci comme <div>. 

<div>
<!-- react-text: 976 -->
Borrowed and renewed items
<!-- react-text: 976 -->
</div>



delay = 10 # seconds
try:
    link_borrowed_items = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.LINK_TEXT, 'Borrowed and renewed items')))
    print("page is ready")
    link_borrowed_items.click()
except TimeoutException:
	print ("Loading took too much time!")

'''
time.sleep(10)
e = browser.find_element_by_xpath("//*[contains(text(), 'Borrowed and renewed items')]")
#e = browser.find_element_by_partial_link_text('Borrowed and renewed items')
#print (len(e))
e.click()
#print (e.text)
#e.click()
